"""Session 8 optional: len() on strings — spaces count."""

# Filename: src/L1/S8/05_string_len.py

import sys

HELP_TEXT = """05_string_len.py

Purpose
    Use len() on strings; remember spaces and punctuation are characters too.

Usage
    python src/L1/S8/05_string_len.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: len() on strings ===\n")

    samples = ["hi", "hello", "hello world", "a b c"]
    for text in samples:
        print(f"len({text!r}) -> {len(text)}")
    return 0


raise SystemExit(main(sys.argv))
