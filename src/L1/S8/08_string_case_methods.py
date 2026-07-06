"""String case helpers: swapcase, capitalize, upper, lower, title."""

# Filename: src/L1/S8/08_string_case_methods.py

import sys

HELP_TEXT = """08_string_case_methods.py

Purpose
    Demonstrate common string case-conversion helpers and compare what each
    method changes.

Usage
    python src/L1/S8/08_string_case_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    sentence = "i enjoy learning python"
    print(f"original      -> {sentence!r}")
    print("swapcase()    ->", repr(sentence.swapcase()))
    print("capitalize()  ->", repr(sentence.capitalize()))
    print("upper()       ->", repr(sentence.upper()))
    print("lower()       ->", repr(sentence.lower()))
    print("title()       ->", repr(sentence.title()))

    heading = "python FUNDAMENTALS session eight"
    print(f"\nheading       -> {heading!r}")
    print("title()       ->", repr(heading.title()))
    print("title().upper() ->", repr(heading.title().upper()))

    return 0


raise SystemExit(main(sys.argv))
