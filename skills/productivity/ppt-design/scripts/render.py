#!/usr/bin/env python3
"""Render a .pptx to PNG images (one per slide) and an optional contact sheet.

Usage:
  python render.py deck.pptx OUT_DIR [--dpi 80] [--sheet sheet.png] [--cols 3]

Needs LibreOffice (soffice) and pdftoppm (poppler). Uses a throwaway LibreOffice
profile and headless 'svp' backend so it does not hang in sandboxes.
"""
import argparse
import glob
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import normalize_pptx, find_soffice, find_pdftoppm  # noqa: E402


SERIF_NAMES = ["Source Han Serif SC", "思源宋体", "Noto Serif SC", "STZhongsong", "华文中宋", "STSong", "华文宋体",
               "SimSun", "宋体", "Songti SC"]
SANS_NAMES = ["Microsoft YaHei", "微软雅黑", "PingFang SC", "Source Han Sans SC", "思源黑体", "HarmonyOS Sans SC",
              "Alibaba PuHuiTi"]


def _font_aliases(work):
    """Preview only: map Windows/Mac Chinese font names to the Noto CJK fonts installed here,
    so a serif heading previews as serif instead of falling back to a sans face."""
    base = Path("/etc/fonts/fonts.conf")
    if not base.exists():
        return None
    def block(names, target):
        return "".join(f'<alias binding="same"><family>{n}</family><prefer><family>{target}</family></prefer></alias>'
                       for n in names)
    xml = ('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig>'
           f'<include ignore_missing="yes">{base}</include>'
           + block(SERIF_NAMES + ["Georgia"], "Noto Serif CJK SC") + block(SANS_NAMES, "Noto Sans CJK SC") + "</fontconfig>")
    p = Path(work) / "fonts.conf"
    p.write_text(xml, encoding="utf-8")
    return p


def to_pdf(pptx, outdir, timeout=240):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="pb_render_"))
    src = work / "deck.pptx"
    normalize_pptx(pptx, src)
    profile = Path(tempfile.mkdtemp(prefix="lo_profile_"))
    env = os.environ.copy()
    if sys.platform.startswith("linux"):
        env["SAL_USE_VCLPLUGIN"] = "svp"  # headless backend, avoids hangs in sandboxes
        conf = _font_aliases(work)
        if conf:
            env["FONTCONFIG_FILE"] = str(conf)
    exe = find_soffice()
    if not exe:
        raise SystemExit("LibreOffice (soffice) not found. Run scripts/setup_check.py --install, "
                         "or skip previews (the .pptx itself is still built).")
    cmd = [exe, f"-env:UserInstallation={profile.as_uri()}", "--headless",
           "--convert-to", "pdf", "--outdir", str(work), str(src)]
    subprocess.run(cmd, env=env, timeout=timeout, capture_output=True)
    pdf = work / "deck.pdf"
    if not pdf.exists():
        raise SystemExit("PDF conversion failed. Try opening/resaving the pptx, then retry.")
    dst = outdir / "deck.pdf"
    shutil.copyfile(pdf, dst)
    shutil.rmtree(profile, ignore_errors=True)
    return dst


def pdf_to_png(pdf, outdir, dpi=80, prefix="slide"):
    """PDF -> PNG per page. Uses pdftoppm (poppler) if present, else PyMuPDF."""
    outdir = Path(outdir)
    for f in outdir.glob(f"{prefix}-*.png"):
        f.unlink()
    tool = find_pdftoppm()
    out = []
    if tool:
        subprocess.run([tool, "-r", str(dpi), "-png", str(pdf), str(outdir / prefix)], check=True)
        files = sorted(outdir.glob(f"{prefix}-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
        for i, f in enumerate(files, 1):
            nf = outdir / f"{prefix}-{i:02d}.png"
            if f != nf:
                f.rename(nf)
            out.append(nf)
        return out
    try:
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz  # older PyMuPDF
    except ImportError:
        raise SystemExit("Need pdftoppm (poppler) or PyMuPDF to turn the PDF into images: "
                         "pip install pymupdf")
    doc = fitz.open(str(pdf))
    for i, page in enumerate(doc, 1):
        nf = outdir / f"{prefix}-{i:02d}.png"
        page.get_pixmap(dpi=dpi).save(str(nf))
        out.append(nf)
    return out


def contact_sheet(images, out, cols=3, pad=12, bg=(120, 120, 120), label=True):
    from PIL import Image, ImageDraw
    ims = [Image.open(p).convert("RGB") for p in images]
    if not ims:
        return None
    w, h = ims[0].size
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * pad, rows * h + (rows + 1) * pad), bg)
    d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        x, y = pad + (i % cols) * (w + pad), pad + (i // cols) * (h + pad)
        sheet.paste(im.resize((w, h)), (x, y))
        if label:
            d.rectangle([x, y, x + 26, y + 18], fill=(0, 0, 0))
            d.text((x + 5, y + 3), str(i + 1), fill=(255, 255, 255))
    sheet.save(out)
    return out


def render(pptx, outdir, dpi=80, sheet=None, cols=3, prefix="slide"):
    pdf = to_pdf(pptx, outdir)
    pngs = pdf_to_png(pdf, outdir, dpi, prefix)
    if sheet:
        contact_sheet(pngs, sheet, cols)
    return pngs


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("outdir")
    ap.add_argument("--dpi", type=int, default=80)
    ap.add_argument("--sheet")
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--prefix", default="slide")
    a = ap.parse_args()
    for p in render(a.pptx, a.outdir, a.dpi, a.sheet, a.cols, a.prefix):
        print(p)
    if a.sheet:
        print("sheet:", a.sheet)
