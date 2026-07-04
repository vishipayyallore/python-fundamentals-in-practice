"""Session 8: list creation, indexing, slicing, and nested list access."""

# Filename: src/L1/S8/01_list_basics.py

import sys

HELP_TEXT = """01_list_basics.py

Purpose
    Demonstrate how to create lists, inspect them, access items by index,
    reach nested list values, slice ranges, and convert a tuple into a list.

Usage
    python src/L1/S8/01_list_basics.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== List Basics Demo ===\n")

    # Creating lists
    print("--- Creating Lists ---")
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    study_topics = ["variables", "conditions", "loops", "functions"]
    mixed = [42, "hello", 3.14, True, study_topics]
    empty = []
    tuple_values = ("practice", 25, False, study_topics)
    converted = list(tuple_values)

    print(f"Numbers: {numbers}")
    print(f"Fruits: {fruits}")
    print(f"Mixed: {mixed}")
    print(f"Empty: {empty}")
    print(f"Tuple converted to list: {converted}")

    # List properties
    print("\n--- List Properties ---")
    print(f"Length of fruits: {len(fruits)}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")

    # Indexing
    print("\n--- Indexing ---")
    print(f"fruits[0] = {fruits[0]}")
    print(f"fruits[1] = {fruits[1]}")
    print(f"fruits[-1] = {fruits[-1]}")
    print(f"mixed[4][0] = {mixed[4][0]}")

    # Slicing
    print("\n--- Slicing ---")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"numbers = {numbers}")
    print(f"numbers[2:5] = {numbers[2:5]}")
    print(f"numbers[:4] = {numbers[:4]}")
    print(f"numbers[6:] = {numbers[6:]}")
    print(f"numbers[::2] = {numbers[::2]}")
    print(f"numbers[::-1] = {numbers[::-1]}")

    print("\n--- Safe Error Demo ---")
    try:
        print(fruits[10])
    except IndexError as error:
        print(f"Accessing fruits[10] raises: {error}")

    # Modifying
    print("\n--- Modifying ---")
    colors = ["red", "green", "blue"]
    print(f"Original: {colors}")
    colors[1] = "yellow"
    print(f"After colors[1] = 'yellow': {colors}")
    return 0


raise SystemExit(main(sys.argv))
