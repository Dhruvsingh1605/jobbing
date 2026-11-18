#!/usr/bin/env python3
"""Check a resume PDF has the expected page count and its last page is well filled.

Usage: python page_fill.py resume.pdf [--pages 1] [--target 97]
Exit code 0 = pass, 1 = fail. Needs poppler (pdfinfo, pdftoppm), Pillow, numpy.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image


def page_count(pdf: str) -> int:
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return -1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--pages", type=int, default=1, help="expected page count")
    ap.add_argument("--target", type=float, default=97.0, help="min %% of last page height used")
    a = ap.parse_args()

    pages = page_count(a.pdf)
    last_page = max(pages, 1)
    with tempfile.TemporaryDirectory() as d:
        prefix = Path(d) / "p"
        subprocess.run(["pdftoppm", "-r", "100", "-f", str(last_page), "-l", str(last_page),
                        "-png", a.pdf, str(prefix)], check=True)
        img_path = sorted(Path(d).glob("p*.png"))[0]
        g = np.asarray(Image.open(img_path).convert("L"))

    ink_rows = np.where((g < 200).any(axis=1))[0]
    if len(ink_rows) == 0:
        print("FAIL: last page is blank")
        return 1
    fill = (ink_rows[-1] + 1) / g.shape[0] * 100
    print(f"pages={pages} (expected {a.pages})  last page content_to={fill:.1f}%  empty_bottom={100 - fill:.1f}%")

    ok = True
    if pages != a.pages:
        print(f"FAIL: {pages} pages; must be exactly {a.pages}")
        ok = False
    if fill < a.target:
        print(f"FAIL: last page only {fill:.1f}% filled; target >= {a.target}% (add JD-relevant content or spacing)")
        ok = False
    if ok:
        print("PASS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
