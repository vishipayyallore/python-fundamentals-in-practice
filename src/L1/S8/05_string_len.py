"""String length — len() counts every character, including spaces."""

# Filename: src/L1/S8/05_string_len.py

import sys

HELP_TEXT = """05_string_len.py

Purpose
    Show that len() measures the number of characters in a string and that
    spaces inside the string count just like any letter or digit.

Usage
    python src/L1/S8/05_string_len.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    role = "python coach"
    n = len(role)
    print(f"role        = {role!r}")
    print(f"len(role)   = {n}  (spaces inside count as characters)")

    print()
    print(f'len("")         = {len("")}   <- empty string has zero characters')
    print(f'len("Python")   = {len("Python")}')
    print(f'len("hi there") = {len("hi there")}  (space at index 2 is counted)')

    return 0


raise SystemExit(main(sys.argv))
