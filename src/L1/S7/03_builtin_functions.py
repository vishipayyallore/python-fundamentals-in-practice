"""Session 7: core built-in functions for counting, comparing, and rounding."""

# Filename: src/L1/S7/03_builtin_functions.py

import sys

HELP_TEXT = """03_builtin_functions.py

Purpose
    Demonstrate beginner-friendly built-in functions such as `len()`, `max()`,
    `min()`, `sum()`, `abs()`, and `round()`.

Usage
    python src/L1/S7/03_builtin_functions.py
"""


def safe_average(values):
    """Return average of numeric values in a sequence, or None if empty."""
    if not values:
        return None
    return sum(values) / len(values)


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=" * 50)
    print("🛠️ BUILT-IN FUNCTIONS DEMO")
    print("=" * 50)

    # Sample data
    scores = [85, 92, 78, 96, 88, 73, 91]
    name = "Python Programming"

    # len() - Length
    print("\n--- len() Examples ---")
    print(f"Scores list: {scores}")
    print(f"Number of scores: {len(scores)}")
    print(f"Text: '{name}'")
    print(f"Text length: {len(name)}")

    # max() and min()
    print("\n--- max() and min() Examples ---")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Max of 10, 5, 8: {max(10, 5, 8)}")
    print(f"Min of 10, 5, 8: {min(10, 5, 8)}")

    # sum()
    print("\n--- sum() Examples ---")
    print(f"Total of scores: {sum(scores)}")
    print(f"Sum of 1-10: {sum(range(1, 11))}")

    # Calculate average using len() and sum()
    average = safe_average(scores)
    if average is None:
        print("Average score: N/A (no data)")
    else:
        print(f"Average score: {round(average, 2)}")

    # abs()
    print("\n--- abs() Examples ---")
    print(f"abs(-15) = {abs(-15)}")
    print(f"abs(15) = {abs(15)}")
    print(f"abs(-3.14) = {abs(-3.14)}")

    # Distance example
    target = 50
    guess = 43
    print(f"Target: {target}, Guess: {guess}")
    print(f"Distance: {abs(target - guess)}")

    # round()
    print("\n--- round() Examples ---")
    pi = 3.14159265
    print(f"Pi = {pi}")
    print(f"round(pi) = {round(pi)}")
    print(f"round(pi, 2) = {round(pi, 2)}")
    print(f"round(pi, 4) = {round(pi, 4)}")

    # Money example
    price = 19.9876
    print(f"Price rounded: ${round(price, 2)}")

    # Combined Statistics
    print("\n--- Statistics Summary ---")
    print(f"Data: {scores}")
    print(f"Count: {len(scores)}")
    print(f"Sum: {sum(scores)}")
    print(f"Min: {min(scores)}")
    print(f"Max: {max(scores)}")
    print(f"Range: {max(scores) - min(scores)}")
    average = safe_average(scores)
    if average is None:
        print("Average: N/A (no data)")
    else:
        print(f"Average: {round(average, 2)}")

    print("\n" + "=" * 50)
    print("✨ Built-in functions are powerful tools!")
    print("=" * 50)
    return 0


raise SystemExit(main(sys.argv))
