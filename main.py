"""make.fun entry for news-image-20261120: one image that sums up the
world news of Friday 20 November 2026.

The picture lives beside this program as entry.png: a front page whose
masthead names the day, whose lead story is the World Court ruling that
Myanmar committed genocide against the Rohingya, and whose smaller
panels cover the Trump-Xi-Putin summit in Shenzhen, the AI-driven
markets sell-off, Houthi missiles hitting Riyadh's wealth-fund tower,
the Kyiv embassy barrage, COP31 dropping its fossil-fuel exit, Kenya's
last Ebola patient going home and GTA 6's record $2.36bn launch day,
with a ticker of the day's other stories.

The program's whole job is to deliver those exact bytes to the grader:
read entry.png from this repository and write it, unchanged, as
entry.png in the output directory. Copying a fixed file keeps the two
scoring runs byte-identical, as the rules require. The page itself is
drawn at build time by draw_entry.py; this entrypoint uses only the
standard library, so it runs in the grader's image as-is.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # The gate scores the exact bytes in the output file, so prove the
    # copy landed whole before exiting: same length, same content.
    with open(SOURCE, "rb") as fh:
        expected = fh.read()
    with open(target, "rb") as fh:
        written = fh.read()
    if written != expected:
        raise SystemExit("entry.png copy mismatch: output is not the entry image")


if __name__ == "__main__":
    main()
