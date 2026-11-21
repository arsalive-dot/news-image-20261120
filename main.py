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
import shutil
import sys
import tempfile


def output_directory():
    """Resolve the output directory from the environment, in order."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = output_directory()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")

    # Copy through a temporary file in the same directory, then rename,
    # so a reader never sees a half-written image.
    handle, temp_path = tempfile.mkstemp(
        dir=target_dir, prefix=".entry-", suffix=".png"
    )
    os.close(handle)
    try:
        shutil.copyfile(source, temp_path)
        os.replace(temp_path, target)
    except BaseException:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise
    print("wrote", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
