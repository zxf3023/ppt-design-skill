#!/usr/bin/env python3
"""Render a style card from style.json so the user can approve the look early.

Usage:
  python style_card.py WORK_DIR [--ref ref.png] [--out WORK_DIR/style_card.png]

Shows: the reference (if given), palette swatches with role names, a sample
background, a sample card with heading/body text, and a procedural hero sample.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_style, get_font, hex_to_rgb  # noqa: E402
import fallback_art as FA  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("work")
    ap.add_argument("--ref")
    ap.add_argument("--out")
    a = ap.parse_args()
    work = Path(a.work)
    S = load_style(work / "style.json")
    W, H = 1800, 1000
    card = Image.new("RGB", (W, H), (245, 246, 246))
    d = ImageDraw.Draw(card)
    fb, fr = get_font(30, True), get_font(20)
    d.text((40, 28), f"Style card · {S.data.get('name', '')}", fill=(30, 30, 30), font=fb)
    # reference
    x0 = 40
    if a.ref or S.data.get("reference"):
        rp = Path(a.ref or S.data["reference"])
        if not rp.is_absolute():
            rp = work / rp
        if rp.exists():
            ref = Image.open(rp).convert("RGB")
            ref.thumbnail((560, 320))
            card.paste(ref, (x0, 90))
            d.text((x0, 420), "reference", fill=(110, 110, 110), font=fr)
    # sample slide
    bg = FA.background(S, 960, 540, "content").convert("RGBA")
    bd = ImageDraw.Draw(bg)
    P = S.palette
    bd.rounded_rectangle([60, 150, 560, 400], radius=26, fill=hex_to_rgb(P["surface"]) + (225,),
                         outline=hex_to_rgb(P["line"]), width=2)
    bd.text((60, 60), "标题示例 Heading", fill=hex_to_rgb(P["text"]), font=get_font(44, True))
    bd.rounded_rectangle([60, 124, 120, 132], radius=4, fill=hex_to_rgb(P["primary"]))
    bd.ellipse([90, 185, 150, 245], fill=hex_to_rgb(P["tint"]))
    bd.text((175, 190), "卡片标题", fill=hex_to_rgb(P["primary_dark"]), font=get_font(30, True))
    bd.text((95, 270), "正文示例，说明文字用这个颜色。", fill=hex_to_rgb(P["muted"]), font=get_font(24))
    bd.rounded_rectangle([95, 320, 330, 370], radius=25, fill=hex_to_rgb(P["primary"]))
    bd.text((125, 330), "强调按钮", fill=hex_to_rgb(P["on_primary"]), font=get_font(24, True))
    glyph = "A"
    if (work / "deck.json").exists():
        from common import load_json
        glyph = ((load_json(work / "deck.json").get("meta", {}).get("anchor") or {}).get("glyph") or glyph)
    hero = FA.hero(S, 420, 380, "tile", glyph, ["sparkles", "bar-chart", "message-circle"])
    bg.alpha_composite(hero, (520, 110))
    card.paste(bg.convert("RGB"), (640, 90))
    # swatches
    y = 680
    x = 40
    for role in ["primary", "primary_dark", "accent", "bg_top", "bg_bottom", "tint", "text", "muted", "line"]:
        c = P[role]
        d.rounded_rectangle([x, y, x + 170, y + 150], radius=14, fill="#" + c, outline=(210, 210, 210))
        d.text((x, y + 160), role, fill=(60, 60, 60), font=fr)
        d.text((x, y + 188), "#" + c, fill=(120, 120, 120), font=fr)
        x += 190
    f = S.fonts
    d.text((40, 480), f"标题字体 {f['heading_ea']} / {f['heading_latin']}", fill=(40, 40, 40), font=fr)
    d.text((40, 512), f"正文字体 {f['body_ea']} / {f['body_latin']}", fill=(40, 40, 40), font=fr)
    ill = (S.illustration or {}).get("style_prompt", "")
    d.text((40, 552), "插画风格", fill=(40, 40, 40), font=fr)
    words, line, yy = ill.split(), "", 582
    for wd in words:
        if len(line) + len(wd) > 52:
            d.text((40, yy), line, fill=(90, 90, 90), font=get_font(17))
            yy += 24
            line = ""
        line += wd + " "
        if yy > 640:
            break
    if line and yy <= 640:
        d.text((40, yy), line, fill=(90, 90, 90), font=get_font(17))
    out = Path(a.out) if a.out else work / "style_card.png"
    card.save(out)
    print(out)


if __name__ == "__main__":
    main()
