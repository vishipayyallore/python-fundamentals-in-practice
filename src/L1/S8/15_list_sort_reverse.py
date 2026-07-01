"""Session 8 optional: sort() and reverse() on numbers and strings."""

# Filename: src/L1/S8/15_list_sort_reverse.py

import sys

HELP_TEXT = """15_list_sort_reverse.py

Purpose
    Practice sort() and reverse() with numbers and strings.

Usage
    python src/L1/S8/15_list_sort_reverse.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: sort & reverse ===\n")

    numbers = [42, 7, 19, 3]
    print(f"numbers: {numbers}")
    numbers.sort()
    print(f"after sort(): {numbers}")
    numbers.reverse()
    print(f"after reverse(): {numbers}\n")

    words = ["banana", "apple", "cherry"]
    print(f"words: {words}")
    words.sort()
    print(f"after sort(): {words}")
    return 0


raise SystemExit(main(sys.argv))
