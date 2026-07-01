"""Session 7: essential built-in functions for everyday scripts."""

# Filename: src/L1/S7/03_builtin_functions.py

import sys

HELP_TEXT = """03_builtin_functions.py

Purpose
    Demonstrate len(), max(), min(), sum(), abs(), and round() on small datasets.

Usage
    python src/L1/S7/03_builtin_functions.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: Built-in functions ===\n")

    scores = [88, 92, 75, 91, 84]
    print(f"scores = {scores}")
    print(f"len(scores)  -> {len(scores)} items")
    print(f"max(scores)  -> {max(scores)}")
    print(f"min(scores)  -> {min(scores)}")
    print(f"sum(scores)  -> {sum(scores)}")
    print(f"average      -> {sum(scores) / len(scores):.1f}\n")

    temperatures = [-3.2, 0.0, 4.5, -1.1]
    print(f"temperatures = {temperatures}")
    print(f"max(temperatures) -> {max(temperatures)}")
    print(f"min(temperatures) -> {min(temperatures)}\n")

    deltas = [-7, 3, -2, 5]
    print(f"deltas = {deltas}")
    print("abs() removes the sign:")
    for value in deltas:
        print(f"  abs({value}) -> {abs(value)}")
    print()

    prices = [19.995, 4.444, 2.675]
    print("round() for display-friendly money values:")
    for price in prices:
        print(f"  round({price}, 2) -> {round(price, 2)}")

    return 0


raise SystemExit(main(sys.argv))
