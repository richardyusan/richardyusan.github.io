#!/usr/bin/env python3
"""Generate images/og-image.png (1200x630), the preview image shown when the
site is shared on Google, LinkedIn, WhatsApp, X, etc.

Run by .github/workflows/jekyll.yml before each build (Pillow + DejaVu fonts
are available on the runner). Edit NAME / TAGLINE / PILLS below to change it.

Usage: python3 scripts/make-og-image.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAME = "Richard Yusan"
TAGLINE = "Economist who tinkers with computers"
PILLS = ["Economic research", "Game ports", "Reverse engineering", "Open source"]
DOMAIN = "richardyusan.github.io"

W, H = 1200, 630
BG = (250, 250, 248)
ACCENT = (37, 99, 235)
DARK = (31, 41, 55)
GREY = (100, 110, 125)
CHIP = (226, 234, 252)

FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    for name in (["DejaVuSans-Bold.ttf", "segoeuib.ttf"] if bold else ["DejaVuSans.ttf", "segoeui.ttf"]):
        for d in (FONT_DIR, "C:/Windows/Fonts"):
            p = os.path.join(d, name)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # accent bar + initials badge
    d.rectangle([0, 0, 16, H], fill=ACCENT)
    cx, cy, r = W - 200, 170, 110
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACCENT)
    initials = "".join(w[0] for w in NAME.split()[:2])
    f_ini = font(96, bold=True)
    tw = d.textlength(initials, font=f_ini)
    d.text((cx - tw / 2, cy - 62), initials, font=f_ini, fill=(255, 255, 255))

    d.text((80, 90), NAME, font=font(84, bold=True), fill=DARK)
    d.text((82, 210), TAGLINE, font=font(40), fill=GREY)
    d.line([80, 330, W - 80, 330], fill=(225, 228, 232), width=2)

    f_pill = font(30, bold=True)
    x, y = 80, 375
    for p in PILLS:
        w = d.textlength(p, font=f_pill) + 48
        if x + w > W - 80:
            x, y = 80, y + 78
        d.rounded_rectangle([x, y, x + w, y + 60], 30, fill=CHIP)
        d.text((x + 24, y + 12), p, font=f_pill, fill=ACCENT)
        x += w + 18

    f_dom = font(30, bold=True)
    dw = d.textlength(DOMAIN, font=f_dom)
    d.rounded_rectangle([80, H - 100, 80 + dw + 64, H - 46], 27, fill=DARK)
    d.text((112, H - 92), DOMAIN, font=f_dom, fill=(255, 255, 255))

    out = os.path.join(ROOT, "images", "og-image.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
