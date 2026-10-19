#!/usr/bin/env python3
"""Generation step 2: check a drafted deck.json before any design work, and render it
as outline.md for the user to confirm.

Usage:
  python outline_check.py WORK_DIR            check + write WORK_DIR/outline.md
  python outline_check.py WORK_DIR --strict   exit 1 on WARN as well as ERROR

Checks (rules are explained in references/generate.md)
  titles     every content slide has a title that states a point; bare topic labels such as
             "Background" "Notes" "Summary" are flagged; length 4-22 characters
  ghost      prints all titles in order: read them alone, they should tell the story
  density    on-screen text per slide against meta.density (low: oral/talk, high: reading/report)
  items      list length against the density limit, split the slide if exceeded
  notes      speaker notes present and roughly 40-260 characters when meta.notes is on
  pages      page count against analysis.json
  flow       the same slide type three times in a row; long decks without section slides;
             a closing slide that only says thanks
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_json, strip_marks  # noqa: E402
import capacity  # noqa: E402
import layouts as LY  # noqa: E402

LIMITS = {  # on-screen characters (notes excluded) and list length per slide
    "low": {"chars": 100, "items": 4},
    "high": {"chars": 200, "items": 6},
}
TOPIC_WORDS = ["介绍", "概述", "简介", "总结", "背景", "目录", "注意事项", "优势", "方法", "原理", "概况",
               "现状", "分析", "说明", "要点", "内容", "问题", "结论", "谢谢", "感谢", "Q&A", "结束"]
NON_SCREEN = {"n", "type", "layout", "notes", "page", "emphasis", "icon", "purpose", "show_footer", "source",
              "chart", "kind", "highlight_col", "image", "at", "frame", "flow", "tone", "boxed", "stamps"}
NO_TITLE_TYPES = {"cover", "closing", "section", "toc", "question", "big_quote"}


def screen_text(obj, key=None):
    """All on-screen strings of a slide (notes and metadata excluded)."""
    if key in NON_SCREEN:
        return []
    if isinstance(obj, str):
        return [strip_marks(obj)]
    if isinstance(obj, list):
        return [t for x in obj for t in screen_text(x)]
    if isinstance(obj, dict):
        return [t for k, v in obj.items() for t in screen_text(v, k)]
    return []


def clen(s):
    """Length in reading units: a CJK character or a latin word counts as one."""
    return len(re.findall(r"[一-鿿]", s)) + len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\.\-]*", s))


def looks_like_topic(title):
    t = strip_marks(title).strip()
    if not t:
        return False
    for w in TOPIC_WORDS:
        # "X-intro" / "notes" / "summary" alone = a label; allow them inside a longer claim
        if t.endswith(w) and clen(t) <= len(w) + 6:
            return True
    return t.startswith(("什么是", "如何", "怎么")) and clen(t) <= 8 and not re.search(r"[，,：:]", t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("work")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    work = Path(a.work)
    deck = load_json(work / "deck.json")
    meta = deck.get("meta", {})
    capacity.set_projection(meta.get("projection"))
    slides = deck.get("slides", [])
    density = meta.get("density", "low")
    lim = LIMITS.get(density, LIMITS["low"])
    notes_on = meta.get("notes", True)
    issues = []

    def add(level, n, msg):
        issues.append((level, n, msg))

    # titles + ghost deck
    ghost = []
    for s in slides:
        n, typ = s.get("n"), s.get("type", "")
        title = s.get("title") or s.get("headline") or s.get("question") or s.get("quote") or ""
        ghost.append((n, typ, strip_marks(title)))
        if typ in NO_TITLE_TYPES:
            continue
        if not title:
            add("ERROR", n, "missing title")
            continue
        L = clen(strip_marks(title))
        if looks_like_topic(title):
            add("WARN", n, f"title looks like a topic label; turn it into a conclusion: {title}")
        if L < 4 or L > 22:
            add("WARN", n, f"title length {L}, recommended 4 to 22: {title}")
    # density + items + notes
    for s in slides:
        n, typ = s.get("n"), s.get("type", "")
        txt = screen_text(s)
        total = sum(clen(t) for t in txt)
        cap = lim["chars"] * (1.4 if typ in ("cover", "closing") else 1)
        if total > cap:
            add("WARN", n, f"on-screen text ~{total} units, over the {density} density cap of {int(cap)}; split the slide or move the detail into notes")
        items = s.get("items", [])
        if len(items) > lim["items"]:
            add("WARN", n, f"{len(items)} items, over the {density} density cap of {lim['items']}; split into two slides")
        if notes_on and typ not in ("section", "toc"):
            nt = strip_marks(s.get("notes", ""))
            if not nt:
                add("WARN", n, "no speaker notes")
            elif clen(nt) < 40 or clen(nt) > 260:
                add("WARN", n, f"notes ~{clen(nt)} units; 40 to 260 units recommended per slide")
    # layout capacity: does the content fit the layout it will get?
    for s in slides:
        lay = s.get("layout") or LY.TYPE_TO_LAYOUTS.get(s.get("type"), ["list_icons"])[0]
        probs = capacity.check(s, lay)
        if probs:
            alts = [a for a in LY.TYPE_TO_LAYOUTS.get(s.get("type"), [])[1:] + ["list_icons", "grid_cards"]
                    if a != lay and not capacity.check(s, a)]
            hint = f"; try {alts[0]} instead" if alts and not s.get("layout") else "; trim the text or split the slide"
            add("WARN", s.get("n"), f"{lay} overflows: " + "; ".join(probs[:3]) + hint)
    # pages
    an = work / "analysis.json"
    if an.exists():
        p = load_json(an).get("pages", {})
        if p and not (p.get("min", 0) <= len(slides) <= p.get("max", 999)):
            add("WARN", 0, f"{len(slides)} slides, the source analysis suggests {p.get('min')} to {p.get('max')}")
    # flow
    for i in range(2, len(slides)):
        t = [slides[j].get("type") for j in (i - 2, i - 1, i)]
        if t[0] == t[1] == t[2] and t[0] not in ("section",):
            add("WARN", slides[i].get("n"), f"three {t[0]} slides in a row; switch the type or layout")
    if len(slides) > 15 and not any(s.get("type") == "section" for s in slides):
        add("WARN", 0, "over 15 slides; add section dividers (type: section)")
    if slides and slides[-1].get("type") == "closing":
        h = strip_marks(slides[-1].get("headline") or slides[-1].get("title") or "")
        if re.fullmatch(r"(谢谢|感谢)(观看|收听|聆听|大家)?[！!。]?|Thanks?.*|Q&A", h.strip()):
            add("WARN", slides[-1].get("n"), "the closing slide only says thanks; use a conclusion or call to action")
    if slides and slides[0].get("type") != "cover":
        add("WARN", slides[0].get("n"), "the first slide is not a cover")

    # outline.md for the user
    out = [f"# {meta.get('title', '')} outline", ""]
    out.append(f"Scenario {meta.get('scenario', '')} · Audience {meta.get('audience', '')} · Density {density} · {len(slides)} slides")
    if meta.get("storyline"):
        out += ["", f"Storyline: {meta['storyline']}"]
    out += ["", "## Titles only (ghost deck)", ""] + [f"{n}. {t}" for n, _, t in ghost]
    out += ["", "## Slide by slide", ""]
    for s in slides:
        title = s.get("title") or s.get("headline") or s.get("question") or s.get("quote") or ""
        out.append(f"### {s.get('n')} · {s.get('type', '')} · {strip_marks(title)}")
        if s.get("purpose"):
            out.append(f"- Purpose: {s['purpose']}")
        body = [t for t in screen_text(s) if t != strip_marks(title)]
        if body:
            out.append("- On screen: " + " / ".join(body))
        if s.get("notes"):
            out.append("- Speaker notes: " + strip_marks(s["notes"]))
        out.append("")
    (work / "outline.md").write_text("\n".join(out), encoding="utf-8")

    print("Ghost deck (titles only)")
    for n, typ, t in ghost:
        print(f"  {n:>2}. [{typ}] {t}")
    print()
    order = {"ERROR": 0, "WARN": 1}
    for level, n, msg in sorted(issues, key=lambda x: (order[x[0]], x[1] or 0)):
        where = f"slide {n}" if n else "overall"
        print(f"[{level}] {where}: {msg}")
    errs = sum(1 for i in issues if i[0] == "ERROR")
    warns = len(issues) - errs
    print(f"\nERROR {errs}  WARN {warns}   wrote {work/'outline.md'}")
    sys.exit(1 if errs or (a.strict and warns) else 0)


if __name__ == "__main__":
    main()
