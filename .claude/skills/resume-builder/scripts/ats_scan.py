#!/usr/bin/env python3
"""Keyword coverage audit of a resume PDF against a JD keyword list.

Usage: python ats_scan.py resume.pdf keywords.json
keywords.json = {"group_name": ["keyword", "alt1|alt2", ...], ...}
A keyword written "a|b" counts as a hit if any alternative appears.
Matching is case-insensitive substring on pdftotext output (whitespace collapsed).
"""
import json
import re
import subprocess
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    pdf, kw_path = sys.argv[1], sys.argv[2]
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    # undo hyphenated line breaks, collapse whitespace
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text).lower()

    groups = json.load(open(kw_path))
    total_hit = total = 0
    for group, kws in groups.items():
        hits, misses = [], []
        for kw in kws:
            alts = [k.strip().lower() for k in kw.split("|") if k.strip()]
            (hits if any(alt in text for alt in alts) else misses).append(kw)
        total_hit += len(hits)
        total += len(kws)
        pct = 100 * len(hits) / len(kws) if kws else 0
        print(f"\n[{group}] {len(hits)}/{len(kws)} ({pct:.0f}%)")
        if misses:
            print("  MISSING: " + ", ".join(misses))
    overall = 100 * total_hit / total if total else 0
    print(f"\nOVERALL: {total_hit}/{total} = {overall:.0f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
