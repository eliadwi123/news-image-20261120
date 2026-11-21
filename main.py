#!/usr/bin/env python3
"""make.fun entry: news-image-20261120.

Writes the entry image to /output/entry.png. The image (a one-page
poster summing up the world news of Friday 20 November 2026) is held
in this repository as base64 text in news.b64; this program decodes
it and writes the exact bytes out. No network, fully deterministic:
every run writes identical bytes.
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    with open(os.path.join(HERE, "news.b64"), "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
