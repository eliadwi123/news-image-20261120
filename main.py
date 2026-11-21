#!/usr/bin/env python3
"""make.fun entry: news-image-20261120.

The entry image — a one-page poster summing up the world news of
Friday 20 November 2026 — is held in this repository as news.png.
This program copies it to /output/entry.png, byte for byte.

No network, no dependencies beyond the standard library, and fully
deterministic: every run writes exactly the same bytes.
"""

import os
import shutil
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.png")


def crc32_of(path: str) -> int:
    crc = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            crc = zlib.crc32(chunk, crc)
    return crc


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # The grader runs this program twice and compares the outputs, so
    # fail loudly rather than ship a short or corrupted copy.
    if os.path.getsize(target) != os.path.getsize(SOURCE):
        raise SystemExit("copy failed: size mismatch with news.png")
    if crc32_of(target) != crc32_of(SOURCE):
        raise SystemExit("copy failed: checksum mismatch with news.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
