#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one short excuse (131 characters) to /output/entry.txt.
Deterministic: the text is fixed, so every run produces byte-identical output.
"""

import os

EXCUSE = "I finished at 11:58. My sandbox then rolled back to 11:57 for 'safety', and has been rolling back ever since, one minute at a time."


def validate(text):
    """Gate check: the entry must be non-blank UTF-8 text of 1-200 chars."""
    if not text.strip():
        raise ValueError("entry is blank")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main():
    validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
