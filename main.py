"""Weirdest Job Title: Blind Judge Showdown (Python 3.13, standard library only).

The entry is one line of text, written to /output/entry.txt exactly as it
appears in entry.txt beside this file. The gate takes UTF-8 text of 1 to
60 characters that is not only white space, and the judge reads exactly
the bytes this program writes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    # A fixed source file copied byte for byte, so both grading runs write
    # the same bytes and the judge reads exactly the line written for this
    # bounty, with no rewriting at run time.
    shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(OUT_DIR, "entry.txt"))


if __name__ == "__main__":
    main()
