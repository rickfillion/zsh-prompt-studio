#!/usr/bin/env python3
"""Build prompt-studio.html from src/studio.html.

Subsets Symbols Nerd Font Mono down to the glyphs the studio uses and
inlines it as a base64 woff2, so the preview shows real Nerd Font icons
without the viewer installing anything.

Usage: python3 build.py path/to/SymbolsNerdFontMono-Regular.ttf
Needs: pip install fonttools brotli
"""
import base64
import io
import pathlib
import re
import sys

from fontTools import subset

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "studio.html"
OUT = ROOT / "prompt-studio.html"


def used_codepoints(text):
    cps = {int(h, 16) for h in re.findall(r"\\u([0-9a-fA-F]{4})", text)}
    cps |= {ord(ch) for ch in text}
    return sorted(c for c in cps if 0xE000 <= c <= 0xF8FF)


def main():
    font_path = sys.argv[1]
    src = SRC.read_text(encoding="utf-8")
    cps = used_codepoints(src)

    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = []
    opts.notdef_outline = True
    font = subset.load_font(font_path, opts)
    cmap = font.getBestCmap()
    missing = [f"{c:04x}" for c in cps if c not in cmap]
    if missing:
        print("warning: not in font:", " ".join(missing))

    sub = subset.Subsetter(opts)
    sub.populate(unicodes=cps)
    sub.subset(font)
    buf = io.BytesIO()
    subset.save_font(font, buf, opts)
    data = base64.b64encode(buf.getvalue()).decode()

    OUT.write_text(src.replace("/*NERD_FONT_DATA*/", data), encoding="utf-8")
    print(f"{len(cps)} glyphs, font {len(buf.getvalue()) // 1024} KB -> {OUT.name}")


if __name__ == "__main__":
    main()
