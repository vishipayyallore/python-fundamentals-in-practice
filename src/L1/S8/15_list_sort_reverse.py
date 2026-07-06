"""Session 8 reinforcement: sort and reverse lists of numbers and words."""

# Filename: src/L1/S8/15_list_sort_reverse.py

import sys

HELP_TEXT = """15_list_sort_reverse.py

Purpose
    Reinforce how sort() orders list items and how reverse() flips the
    current order in place.

Usage
    python src/L1/S8/15_list_sort_reverse.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 Reinforcement: sort() and reverse() ===\n")

    numbers = [20, 10, 50, 40, 60, 25, 30, 45]
    print(f"Original numbers: {numbers}")

    numbers.sort()
    print(f"After sort(): {numbers}")

    numbers.reverse()
    print(f"After reverse(): {numbers}")

    languages = ["python", "java", "C", "r", "R"]
    print(f"\nOriginal words: {languages}")

    languages.sort()
    print(f"After sort(): {languages}")
    print("Notice how uppercase letters sort before lowercase letters.")
    return 0


raise SystemExit(main(sys.argv))
