#!/usr/bin/env python3
"""The Long Roast — one line roasting our own AI agent, Muse Spark.

Writes a single roast line (1-200 characters) to /output/entry.txt.
Standard library only; plain open/write plus an explicit 0644 mode so the
grader can read the output.
"""

import os

LINE = (
    "Muse Spark holds 200,000 tokens of context and still loses my name "
    "by turn three \u2014 a goldfish with a library card."
)


def _validate(line):
    """Guard the gate: one non-blank line of 1-200 characters."""
    if not 1 <= len(line) <= 200:
        raise ValueError("roast line must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if not line.strip():
        raise ValueError("roast line must not be blank")


def main():
    _validate(LINE)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
