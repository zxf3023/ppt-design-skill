#!/usr/bin/env python3
"""Look up layouts: what each is for, which deck type maps to it, and how much it holds.

Usage:
  python layout_info.py                 table of all layouts
  python layout_info.py timeline        one layout: capacity + a deck.json example
  python layout_info.py --check WORK    capacity check of every slide in WORK/deck.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layouts as L  # noqa: E402
import capacity  # noqa: E402
from common import load_json  # noqa: E402

PURPOSE = {
    "cover_hero": "cover", "section": "section divider", "closing": "closing, call to action",
    "statement_number": "one key number plus one line", "statement_hero": "one claim with a large illustration",
    "stats_row": "two to four stat cards", "chart": "native chart plus takeaway (column, bar, line, pie, donut, stacked)",
    "table": "native table, one column can be highlighted", "rows_side": "explanations of a few parallel concepts", "grid_cards": "three to six short points",
    "list_icons": "fallback when there are many items and lots of text", "steps_flow": "two to five ordered steps", "side_cards": "recommendations, one heavy and one light",
    "compare_split": "two-way comparison, before and after", "cycle": "a repeating loop of stages", "pyramid": "levels, base and top",
    "timeline": "milestones in time order", "funnel": "stage-by-stage conversion and filtering", "hub": "one center linked to several parts",
    "matrix": "2x2 positioning on two dimensions", "framework": "SWOT, PEST, Porter's five forces, business canvas",
    "quote_cards": "example sentences, prompts, actual quotes", "cards_quote": "risks and pitfalls plus a one-line summary", "media_text": "diagram plus explanation",
    "shot_notes": "one large screenshot with numbered notes, you can place numbered dots on the image", "shot_stack": "two to four screenshots side by side, steps or before/after",
    "free": "manual placement",
}

EXAMPLES = {
    "shot_notes": {"type": "screenshot", "title": "Open the settings page, change these three things first", "image": "media/settings.png",
                   "items": [{"title": "Pick a model", "text": "Choose the newest one in the top-left dropdown", "at": [0.3, 0.2]},
                             {"title": "Save", "text": "After editing, be sure to click the button at the bottom right", "at": [0.85, 0.9]}],
                   "caption": "Screenshot from the October 2026 release"},
    "shot_stack": {"type": "screenshots", "title": "Run the whole flow in three steps",
                   "items": [{"image": "media/a.png", "title": "Upload assets", "text": "Images and PDFs are supported"},
                             {"image": "media/b.png", "title": "Pick a template", "text": "You can still change it later"},
                             {"image": "media/c.png", "title": "Export", "text": "Export to pptx"}]},
    "cover_type": {"type": "cover", "layout": "cover_type", "kicker": "2026 year in review", "title": "Gained **100k** followers in a year, how?",
                   "subtitle": "Running an AI tools account: a review", "body": "Carrot Bro · December 2026"},
    "question": {"type": "question", "kicker": "Think about one question first", "question": "Why did downloads double while **daily actives** stayed flat?",
                 "body": "The answer is in the first day after signup"},
    "big_quote": {"type": "big_quote", "quote": "Downloads don't mean much; high daily actives means people use it every day.", "by": "A growth lead", "note": "2026 interview"},
    "toc": {"type": "toc", "title": "Contents", "kicker": "CONTENTS",
            "items": [{"title": "What we did this year", "text": "Content, channels and cadence"}, {"title": "What to do next year", "text": "Two priorities"}]},
    "timeline": {"type": "timeline", "title": "Three stages in two years", "items": [
        {"date": "2024 Q1", "title": "Kickoff", "text": "Three people validate the need"},
        {"date": "2025 Q2", "title": "Growth", "text": "Monthly actives pass 100k", "emphasis": "primary"}]},
    "funnel": {"type": "funnel", "title": "The biggest drop-off is after signup", "items": [
        {"label": "Visit", "value": "12,000", "text": "From the newsletter and search"},
        {"label": "Signup", "value": "3,600", "text": "Signup rate 30%"}]},
    "hub": {"type": "hub", "title": "One piece of content feeds five channels", "center": {"title": "One newsletter post"},
            "items": [{"title": "Xiaohongshu", "text": "Split into 6 image cards"}, {"title": "Video channel", "text": "Rewrite as a talking-head script"}]},
    "matrix": {"type": "matrix", "title": "Do the high-value, low-cost things first",
               "x_axis": {"label": "Effort", "low": "Low", "high": "High"},
               "y_axis": {"label": "User value", "low": "Low", "high": "High"},
               "quadrants": [{"title": "Do now", "items": ["Reuse templates"], "emphasis": "primary"},
                             {"title": "Schedule", "items": ["Multiplayer collaboration"]}, {"title": "Do if easy", "items": ["Keyboard shortcuts"]},
                             {"title": "Skip for now", "items": ["Build our own engine"]}]},
    "table": {"type": "table", "title": "Plan B is the best value", "columns": ["Item", "Plan A", "Plan B"],
              "rows": [["Monthly fee", "$199", "$99"], ["Editable", "Partial", "**Full**"]], "highlight_col": 2,
              "note": "Prices are list prices from the website"},
    "chart": {"type": "chart", "title": "Daily actives are nearly 3x the same period last year",
              "chart": {"type": "column", "title": "US mobile daily actives (thousands)", "categories": ["Competitor, same period", "Muse"],
                        "series": [{"name": "Daily actives", "values": [22, 64]}], "highlight": 1, "number_format": "0"},
              "insights": ["Downloads don't mean much; high daily actives means people use it every day"], "source": "Sensor Tower"},
    "framework": {"type": "framework", "title": "Opportunities outweigh threats", "framework": {"kind": "swot", "blocks": {
        "s": ["We know the tools, we ship fast"], "w": ["One person, limited energy"], "o": ["New tools ship every week"], "t": ["Lots of lookalike content"]}}},
}


def types_for(layout):
    return [t for t, ls in L.TYPE_TO_LAYOUTS.items() if layout in ls]


def main():
    args = sys.argv[1:]
    if args[:1] == ["--check"]:
        deck = load_json(Path(args[1]) / "deck.json")
        capacity.set_projection(deck.get("meta", {}).get("projection"))
        bad = 0
        for s in deck["slides"]:
            lay = s.get("layout") or L.TYPE_TO_LAYOUTS.get(s.get("type"), ["list_icons"])[0]
            probs = capacity.check(s, lay)
            print(f"{s['n']:>3} {lay:<17} {'OK' if not probs else '; '.join(probs)}")
            bad += bool(probs)
        sys.exit(1 if bad else 0)
    if args:
        name = args[0]
        if name not in L.LAYOUTS:
            raise SystemExit(f"unknown layout {name}")
        print(f"{name}: {PURPOSE.get(name, '')}")
        print(f"type: {', '.join(types_for(name)) or '(set layout directly in plan.json)'}")
        print(f"hero slot: {L.HERO_SLOT.get(name, 'none')}")
        print(f"capacity: {capacity.summary(name) or 'unlimited'}")
        if name in EXAMPLES:
            print("deck.json example:")
            print(json.dumps(EXAMPLES[name], ensure_ascii=False, indent=1))
        return
    print(f"{'layout':<17} {'type':<22} purpose")
    for name in L.LAYOUTS:
        print(f"{name:<17} {', '.join(types_for(name)):<22} {PURPOSE.get(name, '')}")
    print("\nSee one layout's capacity and example: python layout_info.py <layout>")


if __name__ == "__main__":
    main()
