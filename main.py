#!/usr/bin/env python3
"""make.fun entry: The One-Line Laugh (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one funny line — a single sentence of 81 characters — to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local
testing). Deterministic: no network, no randomness, no external files.
"""

import os
import sys

LINE = "I set my alarm for 6am to be productive, but my snooze button filed for overtime."

# Gate the entry before writing: the judge only accepts UTF-8 text of
# 1-200 characters, a single sentence, not only whitespace.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
assert LINE.strip(), "entry must not be only whitespace"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character line to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
