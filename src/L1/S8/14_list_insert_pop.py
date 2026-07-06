"""Session 8 reinforcement: target specific list positions with insert and pop."""

# Filename: src/L1/S8/14_list_insert_pop.py

import sys

HELP_TEXT = """14_list_insert_pop.py

Purpose
    Reinforce how insert() adds a value at a chosen index and how pop()
    removes and returns a value.

Usage
    python src/L1/S8/14_list_insert_pop.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 Reinforcement: insert() and pop() ===\n")

    numbers = [10, 20, 30, 40, 50, 60]
    print(f"Start: {numbers}")

    numbers.insert(2, 195)
    print(f"After insert(2, 195): {numbers}")

    removed_value = numbers.pop(2)
    print(f"pop(2) returned: {removed_value}")
    print(f"After pop(2): {numbers}")

    last_value = numbers.pop()
    print(f"pop() returned the last value: {last_value}")
    print(f"After pop(): {numbers}")
    return 0


raise SystemExit(main(sys.argv))
