#!/usr/bin/env python3
"""Step 2a: measure a reference image's colors and suggest palette roles.

Usage:
  python extract_style.py ref.png WORK_DIR [--k 8]

Writes:
  WORK_DIR/ref_palette.json   clusters (hex, share, lightness, saturation) + role suggestion
  WORK_DIR/style.draft.json   a starting style.json (Claude refines by looking at the image)

The numbers only describe colors. Mood, illustration style, decorations and
typography feel must be read from the image by Claude (see
references/style_extraction.md) and written into style.json.
"""
import argparse
import colorsys
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import rgb_to_hex, mix, contrast, save_json  # noqa: E402


def kmeans(X, k, iters=25, seed=0):
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(X), k, replace=False)].astype(float)
    for _ in range(iters):
        d = ((X[:, None, :] - C[None]) ** 2).sum(-1)
        lab = d.argmin(1)
        for j in range(k):
            pts = X[lab == j]
            if len(pts):
                C[j] = pts.mean(0)
    return C, lab


def analyze(path, k=8):
    im = Image.open(path).convert("RGB")
    im.thumbnail((320, 320))
    X = np.asarray(im).reshape(-1, 3).astype(float)
    C, lab = kmeans(X, k)
    total = len(X)
    clusters = []
    for j in range(k):
        share = float((lab == j).sum()) / total
        if share < 0.004:
            continue
        r, g, b = C[j] / 255
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        clusters.append({"hex": rgb_to_hex(C[j]), "share": round(share, 3),
                         "lightness": round(l, 3), "saturation": round(s, 3), "hue": round(h * 360)})
    clusters.sort(key=lambda c: -c["share"])
    # vertical gradient probe (top / bottom band averages)
    arr = np.asarray(im).astype(float)
    top = rgb_to_hex(arr[: max(1, arr.shape[0] // 8)].reshape(-1, 3).mean(0))
    bottom = rgb_to_hex(arr[-max(1, arr.shape[0] // 8):].reshape(-1, 3).mean(0))
    return clusters, top, bottom


def suggest(clusters, top, bottom):
    light = [c for c in clusters if c["lightness"] > 0.78]
    dark = sorted([c for c in clusters if c["lightness"] < 0.45], key=lambda c: c["lightness"])
    vivid = sorted([c for c in clusters if 0.3 <= c["lightness"] <= 0.7],
                   key=lambda c: -c["saturation"] * (0.5 + c["share"]))
    bg = max(light, key=lambda c: c["share"])["hex"] if light else "F5F7F6"
    text = dark[0]["hex"] if dark else "222222"
    primary = vivid[0]["hex"] if vivid else (dark[-1]["hex"] if dark else "2F6F5E")
    # accent: most saturated color whose hue is far from primary
    ph = next((c["hue"] for c in clusters if c["hex"] == primary), 0)
    acc = [c for c in clusters if c["saturation"] > 0.35 and min(abs(c["hue"] - ph), 360 - abs(c["hue"] - ph)) > 40]
    accent = max(acc, key=lambda c: c["saturation"])["hex"] if acc else mix(primary, "FFD166", 0.7)
    while contrast(primary, "FFFFFF") < 4.5:
        primary = mix(primary, "000000", 0.08)
    primary_dark = mix(primary, "000000", 0.3)
    if contrast(primary_dark, "FFFFFF") < 4.5:
        primary_dark = mix(primary, "000000", 0.5)
    return {
        "primary": primary, "primary_dark": primary_dark, "accent": accent,
        "bg_top": top, "bg_bottom": mix(top, "FFFFFF", 0.82), "surface": "FFFFFF",
        "tint": mix("FFFFFF", primary, 0.14), "text": text if contrast(text, bg) >= 7 else mix(text, "000000", 0.4),
        "muted": mix(text, "FFFFFF", 0.3), "on_primary": "FFFFFF", "line": mix("FFFFFF", primary, 0.25),
    }


def swatch(clusters, out):
    from PIL import ImageDraw
    w = 900
    im = Image.new("RGB", (w, 140), "white")
    d = ImageDraw.Draw(im)
    x = 0
    for c in clusters:
        cw = max(40, int(w * c["share"]))
        d.rectangle([x, 0, x + cw, 100], fill="#" + c["hex"])
        d.text((x + 4, 108), c["hex"], fill="black")
        x += cw
        if x > w:
            break
    im.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref")
    ap.add_argument("work")
    ap.add_argument("--k", type=int, default=8)
    a = ap.parse_args()
    work = Path(a.work)
    work.mkdir(parents=True, exist_ok=True)
    import shutil
    ref_copy = work / ("ref" + Path(a.ref).suffix.lower())
    if Path(a.ref).resolve() != ref_copy.resolve():
        shutil.copyfile(a.ref, ref_copy)
    clusters, top, bottom = analyze(a.ref, a.k)
    pal = suggest(clusters, top, bottom)
    save_json({"clusters": clusters, "top_band": top, "bottom_band": bottom, "suggested": pal},
              work / "ref_palette.json")
    swatch(clusters, work / "ref_swatch.png")
    draft = {
        "name": "from-reference",
        "reference": ref_copy.name,
        "palette": pal,
        "fonts": {"heading_ea": "Microsoft YaHei", "body_ea": "Microsoft YaHei",
                  "heading_latin": "Arial", "body_latin": "Arial", "display_latin": "Arial"},
        "shape": {"radius": 0.16, "shadow": True, "card_alpha": 0.86},
        "decor": {"header": True, "leaf": True, "brush": True, "title_mark": True,
                  "sparkles": True, "closing_dark": True},
        "background": {"style": "gradient", "decor": ["blobs", "bokeh", "arcs"], "cover_decor": ["blobs", "clouds", "hills"]},
        "illustration": {
            "style_prompt": "TODO: describe the reference's illustration style in English",
            "negative": "text, letters, words, captions, watermark, logo, signature, frame, border, UI text",
        },
    }
    save_json(draft, work / "style.draft.json")
    print("clusters:")
    for c in clusters:
        print(f"  #{c['hex']}  share={c['share']:.2f}  L={c['lightness']:.2f}  S={c['saturation']:.2f}")
    print("suggested roles:", pal)
    print(f"wrote {work/'ref_palette.json'}, {work/'style.draft.json'}, {work/'ref_swatch.png'}")


if __name__ == "__main__":
    main()
