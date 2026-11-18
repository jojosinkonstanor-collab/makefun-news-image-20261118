#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118.

Writes the 18 November 2026 world-news front page to /output/entry.png.

The image itself (asset/entry.png) is drawn once, offline, by draw.py in the
workspace using Pillow: a newspaper front page with the masthead
"THE WORLD IN ONE PICTURE", the date "WEDNESDAY, 18 NOVEMBER 2026", a lead
panel on the Quad summit in Manila, and five further panels (Nvidia earnings,
the Siberian military plane crash, the Iran-backed Trump assassination plot
sentence, the election of Matan Kahana as speaker of Israel's parliament,
and the US losing its measles-free status). All text is rendered by Pillow,
so no glyph is ever garbled by an image generator.

This program does the only thing the grader needs: it copies that exact
image to the output directory. It uses only the Python standard library,
touches no network, and writes byte-identical output on every run.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "asset" / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing asset: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
