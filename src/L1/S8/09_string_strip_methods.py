"""String trimming with strip(), lstrip(), and rstrip()."""

# Filename: src/L1/S8/09_string_strip_methods.py

import sys

HELP_TEXT = """09_string_strip_methods.py

Purpose
    Demonstrate how strip(), lstrip(), and rstrip() remove leading and/or
    trailing characters, most commonly whitespace.

Usage
    python src/L1/S8/09_string_strip_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    padded = "   example text   "
    print(f"padded       -> {padded!r}")
    print("strip()      ->", repr(padded.strip()))
    print("lstrip()     ->", repr(padded.lstrip()))
    print("rstrip()     ->", repr(padded.rstrip()))

    decorated = "***python***"
    print(f"\ndecorated    -> {decorated!r}")
    print("strip('*')   ->", repr(decorated.strip("*")))

    code = "eelevel-up-ee"
    print(f"\ncode         -> {code!r}")
    print("strip('e')   ->", repr(code.strip("e")))
    print("rstrip('e')  ->", repr(code.rstrip("e")))

    return 0


raise SystemExit(main(sys.argv))
