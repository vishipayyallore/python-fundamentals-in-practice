# Filename: src/L1/S7/06_print_sep_end.py
"""Session 1 revisited — print() with sep and end.

Plain print(items) joins pieces with spaces and ends with a newline by default.
Knowing these two parameters keeps debug prints readable when you inspect
multiple values on one line or want to avoid extra blank lines.
"""

import sys

HELP_TEXT = """06_print_sep_end.py

Purpose
    Demonstrate how print() handles multiple values, separators, and line endings.
    Knowing these keeps debug prints readable.

Usage
    python src/L1/S7/06_print_sep_end.py

Topics Covered
    - Printing multiple values with commas
    - sep to change what goes between pieces
    - end to suppress or extend the trailing newline
    - Common beginner comma mistake
"""


def demo_multiple_values() -> None:
    lesson_number = 7
    sentence = "Current lesson"
    print("=== Multiple values in print() ===")
    print(sentence, lesson_number)


def demo_sep() -> None:
    lesson_number = 7
    sentence = "Current lesson"
    print("\n=== Using sep ===")
    print(sentence, lesson_number, sep="-")
    print(sentence, lesson_number, sep=" | ")


def demo_end() -> None:
    lesson_number = 7
    sentence = "Current lesson"
    print("\n=== Using end ===")
    print(sentence, lesson_number, sep="-", end="  <-- same line ->  ")
    print(sentence, lesson_number, sep="-")


def demo_common_mistake() -> None:
    print("\n=== Common beginner mistake ===")
    print("Wrong:  print(sentence lesson_number)")
    print("Right:  print(sentence, lesson_number)")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_multiple_values()
    demo_sep()
    demo_end()
    demo_common_mistake()
    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
