#!/usr/bin/env python3
"""Writes the single sentence that could have replaced an entire pointless meeting."""

import os

SENTENCE = (
    "After forty-five minutes, six people, and one dead whiteboard marker, "
    "the meeting's only outcome was scheduling another meeting to decide "
    "what this one was even for."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
