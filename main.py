#!/usr/bin/env python3
"""Write the 20 November 2026 world-news atlas image to the output path.

The image is bundled in this repository as entry.png; this program just
places an exact copy of it where the harness expects it. It uses only the
Python standard library, touches no network, and always writes the same
bytes, so repeated runs are byte-identical. The bundled image is a dense
colour atlas of Friday 20 November 2026: 52 stories, a world map with 16
numbered pins, and a strip of the day's verified figures.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def output_dir():
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        v = os.environ.get(var)
        if v:
            return v
    return "/output"


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    # Write via a temp file in the same directory, then rename, so a
    # partial write can never leave a truncated entry.png behind.
    # The temp file is created with open() (0644), not mkstemp (0600):
    # the grader reads the output as another user, so entry.png must
    # stay world-readable after the rename.
    tmp = dst + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
