#!/usr/bin/env python3
"""Five-dimension design self-review: measure the evidence, leave the judgement to the reviewer.

Usage:
  python review.py WORK_DIR

Reads out/layout_dump.json, out/qa_report.json, deck.json and style.json, and writes
out/review.md: one evidence table per dimension (numbers a script can count), empty
score slots, and the rubric from references/critique.md in short form. Claude then
looks at out/sheet.png and the page PNGs, fills in the scores and the Keep / Fix /
Quick-win lists, fixes what is cheap, and reports the verdict when delivering.

Dimensions: unity (one direction throughout), hierarchy (what to read first),
detail (alignment, spacing, small defects), message (does each page land its point),
rhythm (variety and pacing across the deck).
"""
import argparse
import statistics as st
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_json, load_style, clen, CANVAS_W  # noqa: E402

CONTENT_ROLES_SKIP = ("background", "decor", "chrome")
NEUTRALS = {"FFFFFF", "000000", "1A1A1A", "111111"}  # ink_on() picks these for text on fills


def content_texts(sd):
    return [e for e in sd["elements"] if e["t"] == "text" and e.get("role") not in CONTENT_ROLES_SKIP]


def near_misses(values, tol_lo=0.03, tol_hi=0.18):
    """Pairs of edges that almost line up: closer than tol_hi but not equal. Usually a slip."""
    vs = sorted(set(round(v, 2) for v in values))
    return [(a, b) for a, b in zip(vs, vs[1:]) if tol_lo < b - a < tol_hi]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("work")
    a = ap.parse_args()
    work = Path(a.work)
    out = work / "out"
    dump = load_json(out / "layout_dump.json")
    deck = load_json(work / "deck.json")
    style = load_style(work / "style.json")
    qa = load_json(out / "qa_report.json") if (out / "qa_report.json").exists() else {"issues": [], "counts": {}}
    slides = dump["slides"]
    n = len(slides)

    # ---- unity
    sizes = Counter()
    fonts = Counter()
    raw_colors = Counter()
    radii = Counter()
    for sd in slides:
        for e in sd["elements"]:
            if e.get("role") in CONTENT_ROLES_SKIP:
                continue
            if e["t"] == "text":
                sizes[e["size"]] += 1
                fonts[e.get("font", "body")] += 1
            for k in ("color", "fill"):
                v = str(e.get(k) or "")
                if (v and v.lstrip("#").isalnum() and len(v.lstrip("#")) == 6 and v.split("@")[0] not in style.palette
                        and v.lstrip("#").upper() not in NEUTRALS):
                    raw_colors[v] += 1
            # cards only: pills (radius = h/2), hairlines and tiny marks are not cards
            if (e["t"] == "rect" and e.get("radius") and e["w"] > 1.0 and e["h"] > 0.6
                    and e["radius"] < min(e["w"], e["h"]) / 2 - 0.01):
                radii[round(e["radius"], 2)] += 1
    unity = [
        ("Distinct font sizes in the deck (excluding header and footer)", len(sizes), "Under 8 is good; past 10 it falls apart"),
        ("Font roles in use", ", ".join(f"{k}×{v}" for k, v in fonts.most_common()), "display should only appear on covers, big numbers and section numbers"),
        ("Colors outside the palette", len(raw_colors), "should be 0"),
        ("Distinct card corner radii", len(radii), "1 to 2"),
    ]

    # ---- hierarchy
    hier_rows, weak = [], []
    for sd in slides:
        ts = content_texts(sd)
        if not ts:
            continue
        big = max(t["size"] for t in ts)
        body = st.median([t["size"] for t in ts])
        per = len({t["size"] for t in ts})
        ratio = big / body if body else 0
        hier_rows.append((sd["n"], big, body, round(ratio, 2), per))
        if ratio < 1.5 or per > 5:
            weak.append(sd["n"])
    hierarchy = [
        ("Pages where max/median font size < 1.5 or more than 5 sizes on one page", weak or "none", "The focal point is weak, or the sizes are too fragmented"),
    ]

    # ---- detail
    miss = []
    for sd in slides:
        ts = content_texts(sd)
        lefts = [t["x"] for t in ts if t.get("align", "l") == "l"]
        m = near_misses(lefts)
        if m:
            miss.append(f"{sd['n']}: {', '.join(f'{x:.2f}/{y:.2f}' for x, y in m[:3])}")
    warn_by = Counter(i["check"] for i in qa.get("issues", []) if i["level"] == "WARN")
    detail = [
        ("Left edges that almost line up (inches)", "; ".join(miss) if miss else "none", "Misalignments of 0.03 to 0.18 inches are usually mistakes"),
        ("QA warning breakdown", ", ".join(f"{k}×{v}" for k, v in warn_by.most_common()) or "none", "handle contrast, rail, accent first"),
        ("QA errors", qa.get("counts", {}).get("ERROR", 0), "must be 0"),
    ]

    # ---- message
    dens, no_notes = [], []
    for s in deck["slides"]:
        from outline_check import screen_text
        c = sum(clen(t) for t in screen_text(s))
        dens.append((s["n"], c))
        if not s.get("notes") and s.get("type") not in ("cover", "section", "toc", "closing"):
            no_notes.append(s["n"])
    heavy = [f"{k}({c})" for k, c in dens if c > 160]
    convey = [
        ("Pages with more than 160 on-screen characters", ", ".join(heavy) or "none", "A text-heavy page should be split or moved to a more structured layout"),
        ("Content pages with no speaker notes", no_notes or "none", "The script requires notes on every page"),
        ("Average title length", round(st.mean(clen(s.get("title") or s.get("headline") or s.get("question") or s.get("quote") or "") for s in deck["slides"]), 1),
         "A takeaway title is usually 10 to 20 characters"),
    ]

    # ---- rhythm
    layouts = [sd["layout"] for sd in slides]
    runs = [layouts[i] for i in range(2, n) if layouts[i] == layouts[i - 1] == layouts[i - 2]]
    counts = [c for _, c in dens]
    heroes = sum(1 for sd in slides for e in sd["elements"] if e["t"] == "image" and e.get("role") not in ("background", "decor"))
    rhythm = [
        ("Distinct layouts / pages", f"{len(set(layouts))} / {n}", "at least half"),
        ("Three pages in a row with the same layout", runs or "none", "should be none"),
        ("Text length variation (stdev / mean)", round(st.pstdev(counts) / max(1, st.mean(counts)), 2) if counts else 0,
         "0.3 to 0.7 breathes well; lower reads like a ledger, higher swings between dense and sparse"),
        ("Illustration count", heroes, "Cover, section and closing pages are enough; not every page needs one"),
    ]

    def table(rows):
        lines = ["| Check | Result | Reference |", "|---|---|---|"]
        lines += [f"| {a} | {b} | {c} |" for a, b, c in rows]
        return "\n".join(lines)

    md = [f"# Design self-review: {deck.get('meta', {}).get('title', work.name)}", "",
          "Look at out/sheet.png and the page PNGs first, then score against the numbers below. "
          "Each item is 0 to 10: 0 to 4 fails, 5 to 6 is usable, 7 to 8 is solid, 9 to 10 is excellent. "
          "Don't average the scores away; if something is weak, say so.", "",
          "## 1 Unity: is the whole deck one direction throughout", "", table(unity), "", "Score:", "",
          "## 2 Hierarchy: can a stranger see at a glance what to read first", "", table(hierarchy), "",
          "| Page | Max size | Median size | Ratio | Size count |", "|---|---|---|---|---|",
          *[f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in hier_rows], "", "Score:", "",
          "## 3 Detail: alignment, spacing, small defects", "", table(detail), "", "Score:", "",
          "## 4 Message: does each page land its point", "", table(convey), "", "Score:", "",
          "## 5 Rhythm: does the deck rise and fall as you flip through", "", table(rhythm), "", "Score:", "",
          "## Verdict", "", "One-line judgement:", "",
          "Keep (done right, don't touch):", "", "Fix (issues that hurt the look, fix before delivery):", "",
          "Quick wins (a few minutes each, clearly visible):", ""]
    (out / "review.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {out / 'review.md'}")
    print(f"  {len(sizes)} font sizes, {len(set(layouts))}/{n} layouts, weak hierarchy on {weak or 'none'}, "
          f"alignment suspects on {len(miss)} pages, QA errors {qa.get('counts', {}).get('ERROR', 0)}")


if __name__ == "__main__":
    main()
