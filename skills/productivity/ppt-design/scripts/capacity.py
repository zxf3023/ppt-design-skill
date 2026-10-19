"""How much each layout can hold, so overflow is caught while writing the outline.

Units are reading units: one CJK character or one latin word = 1 (see common.clen).
Each entry:
  items      (min, max) number of entries in slide["items"]
  item       per-item field -> max units
  fields     top-level (or dotted, e.g. "side.title") field -> max units
  lists      field -> (min, max, max units per entry) for plain string lists
Used by outline_check.py (warnings), plan_deck.py (pick a layout that fits) and layout_info.py.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import clen  # noqa: E402

T = {"title": 22}
CAPACITY = {
    "cover_hero": {"fields": {"title": 16, "subtitle": 18, "body": 30, "kicker": 14}, "items": (0, 4), "item": {"text": 12}},
    "statement_number": {"fields": {**T, "number": 4, "body": 44}, "lists": {"lines": (1, 3, 12)}},
    "rows_side": {"fields": {**T, "side.title": 12, "side.body": 40}, "items": (2, 4), "item": {"title": 8, "text": 26}},
    "stats_row": {"fields": {**T, "takeaway": 36}, "items": (2, 4), "item": {"value": 6, "label": 12}},
    "media_text": {"fields": {**T, "point": 22, "body": 44, "callout": 50, "diagram.title": 14}},
    "side_cards": {"fields": {**T, "side.title": 12, "side.body": 40}, "items": (1, 3), "item": {"title": 18, "text": 44}},
    "quote_cards": {"fields": {**T, "lead": 30}, "items": (1, 4), "item": {"text": 50}},
    "statement_hero": {"fields": {**T, "headline": 16, "body": 44, "pill": 22}},
    "cards_quote": {"fields": T, "items": (1, 3), "item": {"title": 14, "text": 32}, "lists": {"quote_lines": (1, 3, 12)}},
    "list_icons": {"fields": T, "items": (1, 6), "item": {"title": 12, "text": 60}},
    "grid_cards": {"fields": T, "items": (2, 6), "item": {"title": 10, "text": 28}},
    "steps_flow": {"fields": {**T, "takeaway": 36}, "items": (2, 5), "item": {"title": 8, "text": 30}},
    "compare_split": {"fields": {**T, "left.title": 10, "right.title": 10},
                      "lists": {"left.items": (1, 5, 20), "right.items": (1, 5, 20)}},
    "cycle": {"fields": {**T, "center": 6}, "items": (3, 6), "item": {"title": 8, "text": 20}},
    "pyramid": {"fields": T, "items": (2, 5), "item": {"title": 8, "text": 26}},
    "section": {"fields": {"title": 16, "subtitle": 30, "number": 3}},
    "cover_type": {"fields": {"title": 24, "subtitle": 26, "body": 30, "kicker": 16}, "items": (0, 4), "item": {"text": 8}},
    "cover_center": {"fields": {"title": 16, "subtitle": 16, "body": 34, "kicker": 30, "takeaway": 34}},
    "rank_grid": {"fields": T, "items": (3, 10), "item": {"title": 8, "text": 10}, "lists": {"findings.items": (0, 4, 26)}},
    "question": {"fields": {"question": 30, "kicker": 12, "body": 40}},
    "shot_notes": {"fields": {**T, "caption": 30}, "items": (0, 5), "item": {"title": 10, "text": 30}},
    "shot_stack": {"fields": T, "items": (1, 4), "item": {"title": 10, "text": 20}},
    "explain": {"fields": {**T, "takeaway": 40}},
    "big_quote": {"fields": {"quote": 70, "by": 20, "note": 30}},
    "toc": {"fields": {"title": 6, "kicker": 3}, "items": (0, 6), "item": {"title": 14, "text": 22}},
    "toc_row": {"fields": {"title": 10, "kicker": 3}, "items": (0, 5), "item": {"title": 8, "text": 16}},
    "closing": {"fields": {"headline": 18, "body": 30, "cta": 12}},
    "timeline": {"fields": T, "items": (3, 6), "item": {"date": 8, "title": 8, "text": 20}},
    "funnel": {"fields": T, "items": (3, 5), "item": {"label": 8, "value": 8, "text": 26}},
    "hub": {"fields": {**T, "center.title": 8}, "items": (3, 6), "item": {"title": 8, "text": 18}},
    "matrix": {"fields": {**T, "x_axis.label": 8, "y_axis.label": 6}, "quadrants": (4, 4, 8, 3, 14)},
    "table": {"fields": {**T, "note": 40}, "table": {"columns": (2, 6), "rows": (1, 8), "cell": 16}},
    "chart": {"fields": T, "chart": {"categories": (2, 8), "series": (1, 3)}, "lists": {"insights": (0, 3, 32)}},
    "framework": {"fields": T, "framework": {"swot": (1, 4, 16), "pest": (1, 4, 14), "five_forces": (1, 3, 14),
                                             "canvas": (1, 3, 14)}},
}


def _get(d, dotted):
    for k in dotted.split("."):
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def _txt(x):
    return x if isinstance(x, str) else (x.get("text", "") if isinstance(x, dict) else str(x))


# projection mode (deck.meta.projection) raises the font floor, so every text limit shrinks
SCALE = {"v": 1.0}


def set_projection(on):
    SCALE["v"] = 0.65 if on else 1.0


def _m(mx):
    return max(2, int(mx * SCALE["v"]))


def check(slide, layout):
    """Return a list of human-readable problems ("" when it fits)."""
    cap = CAPACITY.get(layout)
    if not cap:
        return []
    out = []
    for f, mx in cap.get("fields", {}).items():
        v = _get(slide, f)
        if isinstance(v, str) and clen(v) > _m(mx):
            out.append(f"{f} is ~{clen(v)} units, {layout} holds at most {_m(mx)}")
    if "items" in cap:
        lo, hi = cap["items"]
        items = slide.get("items", [])
        if not (lo <= len(items) <= hi):
            out.append(f"{len(items)} items, {layout} needs {lo} to {hi}")
        for i, it in enumerate(items, 1):
            if not isinstance(it, dict):
                continue
            for f, mx in cap.get("item", {}).items():
                v = it.get(f)
                if v is not None and clen(str(v)) > _m(mx):
                    out.append(f"item {i} field {f} is ~{clen(str(v))} units, max {_m(mx)}")
    for f, (lo, hi, mx) in cap.get("lists", {}).items():
        v = _get(slide, f)
        if v is None:
            continue
        v = v if isinstance(v, list) else [v]
        if not (lo <= len(v) <= hi):
            out.append(f"{f} has {len(v)} entries, needs {lo} to {hi}")
        for i, x in enumerate(v, 1):
            if clen(_txt(x)) > _m(mx):
                out.append(f"{f} entry {i} is ~{clen(_txt(x))} units, max {_m(mx)}")
    if "quadrants" in cap:
        lo, hi, tmx, imax, iw = cap["quadrants"]
        q = slide.get("quadrants", [])
        if len(q) != 4:
            out.append(f"quadrants needs exactly 4, got {len(q)}")
        for i, qq in enumerate(q, 1):
            if clen(qq.get("title", "")) > _m(tmx):
                out.append(f"quadrant {i} title max {_m(tmx)} units")
            its = qq.get("items", [])
            if len(its) > imax:
                out.append(f"quadrant {i} has {len(its)} items, max {imax}")
            for x in its:
                if clen(_txt(x)) > _m(iw):
                    out.append(f"quadrant {i} has an entry of ~{clen(_txt(x))} units, max {_m(iw)}")
    if "table" in cap:
        t = cap["table"]
        cols, rows = slide.get("columns", []), slide.get("rows", [])
        if not (t["columns"][0] <= len(cols) <= t["columns"][1]):
            out.append(f"table has {len(cols)} columns, needs {t['columns'][0]} to {t['columns'][1]}")
        if not (t["rows"][0] <= len(rows) <= t["rows"][1]):
            out.append(f"table has {len(rows)} rows, needs {t['rows'][0]} to {t['rows'][1]}, split the slide if more")
        long_cells = [c for r in rows for c in r if clen(str(c)) > _m(t["cell"])]
        if long_cells:
            out.append(f"{len(long_cells)} cells exceed {_m(t['cell'])} units")
    if "chart" in cap:
        c = cap["chart"]
        spec = slide.get("chart") or {}
        cats, ser = spec.get("categories", []), spec.get("series", [])
        if not (c["categories"][0] <= len(cats) <= c["categories"][1]):
            out.append(f"chart has {len(cats)} categories, needs {c['categories'][0]} to {c['categories'][1]}")
        if not (c["series"][0] <= len(ser) <= c["series"][1]):
            out.append(f"chart has {len(ser)} series, needs {c['series'][0]} to {c['series'][1]}")
        for sr in ser:
            if len(sr.get("values", [])) != len(cats):
                out.append(f"series {sr.get('name', '')} has a different number of values than categories")
        if spec.get("type") in ("pie", "doughnut") and len(ser) > 1:
            out.append("pie and doughnut charts can only have one series")
    if "framework" in cap:
        fw = slide.get("framework") or {}
        kind = fw.get("kind")
        lim = cap["framework"].get(kind)
        if not lim:
            out.append(f"framework.kind must be one of {', '.join(cap['framework'])}")
        else:
            lo, hi, mx = lim
            for k, v in (fw.get("blocks") or {}).items():
                v = v if isinstance(v, list) else [v]
                if len(v) > hi:
                    out.append(f"{kind} {k} has {len(v)} entries, max {hi}")
                for x in v:
                    if clen(_txt(x)) > _m(mx):
                        out.append(f"{kind} {k} has an entry of ~{clen(_txt(x))} units, max {_m(mx)}")
    return out


def summary(layout):
    cap = CAPACITY.get(layout, {})
    parts = []
    if "items" in cap:
        lo, hi = cap["items"]
        its = ", ".join(f"{k}≤{v}" for k, v in cap.get("item", {}).items())
        parts.append(f"items {lo}-{hi} ({its})")
    for f, (lo, hi, mx) in cap.get("lists", {}).items():
        parts.append(f"{f} {lo}-{hi} entries (each ≤{mx})")
    if "quadrants" in cap:
        parts.append("4 quadrants (title ≤8, each cell ≤3 entries, ≤14 units each)")
    if "table" in cap:
        t = cap["table"]
        parts.append(f"{t['columns'][0]}-{t['columns'][1]} columns, {t['rows'][0]}-{t['rows'][1]} rows, cells ≤{t['cell']}")
    if "chart" in cap:
        parts.append("2-8 categories, 1-3 series, ≤3 insights")
    if "framework" in cap:
        parts.append("≤4 entries per cell, ≤16 units each (canvas: ≤3 per cell, ≤14 units each)")
    fl = ", ".join(f"{k}≤{v}" for k, v in cap.get("fields", {}).items())
    if fl:
        parts.append(fl)
    return "; ".join(parts)
