"""Session 6: for loops, range(), and a small nested-loop pattern."""

# Filename: src/L1/S6/01_for_loops.py

import sys

HELP_TEXT = """01_for_loops.py

Purpose
    Demonstrate `for` loops with `range()` and show how a nested loop can build
    a simple text pattern.

Usage
    python src/L1/S6/01_for_loops.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 6: for loops ===\n")

    # Why for-loop: use it when the number of repeats is known.
    print("Count from 1 to 5:")
    for number in range(1, 6):
        print(number)

    print("\nEven numbers from 2 to 10:")
    for even in range(2, 11, 2):
        print(even)

    print("\nCountdown with for-loop:")
    for left in range(5, 0, -1):
        print(f"T-minus {left}")
    print("🚀 Lift off!")

    # Nested loop: outer loop = rows, inner loop = columns.
    # Why nested loops matter: they help build grid/pattern style output.
    print("\nSimple pattern:")
    for row in range(1, 4):
        line = ""
        for _ in range(row):
            line += "*"
        print(line)
    return 0


raise SystemExit(main(sys.argv))
