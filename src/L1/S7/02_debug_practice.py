"""Session 7: debug practice with three small fixed examples."""

# Filename: src/L1/S7/02_debug_practice.py

import sys

HELP_TEXT = """02_debug_practice.py

Purpose
    Walk through three beginner debugging examples: average calculation, vowel
    counting, and finding a maximum value.

Usage
    python src/L1/S7/02_debug_practice.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=" * 50)
    print("🐛 DEBUG PRACTICE - Find the Bugs!")
    print("=" * 50)

    # Bug 1: Calculate average (something's wrong!)
    print("\n--- Bug 1: Average Calculator ---")
    numbers = [10, 20, 30, 40, 50]

    # BUGGY version (uncomment to test):
    # total = 0
    # for num in numbers:
    #     total = num  # Bug! Should be total += num
    # average = total / len(numbers)
    # print(f"Average: {average}")  # Wrong result!

    # FIXED version:
    total = 0
    for num in numbers:
        total += num  # Fixed: accumulate the sum
    average = total / len(numbers)
    print(f"Numbers: {numbers}")
    print(f"Average: {average}")  # Correct: 30.0

    # Bug 2: Count vowels (something's wrong!)
    print("\n--- Bug 2: Vowel Counter ---")
    text = "Hello World"

    # BUGGY version (uncomment to test):
    # vowels = "aeiou"
    # count = 0
    # for char in text:
    #     if char in vowels:  # Bug! Doesn't handle uppercase
    #         count += 1
    # print(f"Vowels in '{text}': {count}")  # Wrong: 2 instead of 3

    # FIXED version:
    vowels = "aeiouAEIOU"  # Fixed: include uppercase
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"Text: '{text}'")
    print(f"Vowel count: {count}")  # Correct: 3

    # Bug 3: Find maximum (something's wrong!)
    print("\n--- Bug 3: Find Maximum ---")
    values = [5, 2, 9, 1, 7]

    # BUGGY version (uncomment to test):
    # max_val = 0  # Bug! What if all numbers are negative?
    # for val in values:
    #     if val > max_val:
    #         max_val = val

    # FIXED version:
    max_val = values[0]  # Fixed: start with first element
    for val in values:
        if val > max_val:
            max_val = val
    print(f"Values: {values}")
    print(f"Maximum: {max_val}")  # Correct: 9

    print("\n" + "=" * 50)
    print("🎯 Debugging complete! All bugs fixed!")
    print("=" * 50)
    return 0


raise SystemExit(main(sys.argv))
