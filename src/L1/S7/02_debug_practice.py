"""Session 7: print-debugging exercises — predict, run, fix."""

# Filename: src/L1/S7/02_debug_practice.py

import sys

HELP_TEXT = """02_debug_practice.py

Purpose
    Practice finding bugs with print() checkpoints before changing logic.

Usage
    python src/L1/S7/02_debug_practice.py
"""


def sum_even_numbers(values: list[int]) -> int:
    """Return the sum of even integers in values."""
    total = 0
    for item in values:
        # Why print here: see each value and whether the even test passes.
        print(f"DEBUG item={item!r}, even={item % 2 == 0}")
        if item % 2 == 0:
            total += item
    return total


def average_of_three(first: float, second: float, third: float) -> float:
    """Return the arithmetic mean of three numbers."""
    # Why print: confirm inputs before the formula — catches swapped arguments early.
    print(f"DEBUG inputs: first={first}, second={second}, third={third}")
    count = 3
    total = first + second + third
    print(f"DEBUG total={total}, count={count}")
    return total / count


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: Print debugging practice ===\n")

    sample = [1, 2, 3, 4, 5, 6]
    print(f"sum_even_numbers({sample}) = {sum_even_numbers(sample)}\n")

    print(f"average_of_three(10, 20, 30) = {average_of_three(10, 20, 30)}\n")

    print("Remove or comment out DEBUG lines once you trust the logic.")
    return 0


raise SystemExit(main(sys.argv))
