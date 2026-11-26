#!/usr/bin/env python3
"""Make the Judge Laugh in One Line (account B).

Writes one joke line to $MAKEFUN_OUTPUT_DIR/entry.txt,
or /output/entry.txt when the variable is unset.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.

The joke: a smart fridge serving divorce papers -- the setup sounds
like a gadget complaint, and the punchline is a relationship one:
opened only at 2 a.m., never commits to anything.
"""

import os

LINE = "My smart fridge filed for divorce \u2014 it says I only open it at 2 a.m. and never commit to anything."


def build_line() -> str:
    """Return the joke line, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry must be one non-empty line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    return line


def write_entry(line: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    return written


def main() -> None:
    written = write_entry(build_line())
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
