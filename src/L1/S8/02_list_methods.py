"""Session 8: adding, replacing, removing, finding, and sorting list items."""

# Filename: src/L1/S8/02_list_methods.py

import sys

HELP_TEXT = """02_list_methods.py

Purpose
    Demonstrate common ways to add, replace, remove, find, and sort list
    items.

Usage
    python src/L1/S8/02_list_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== List Methods Demo ===\n")

    # Adding items
    print("--- Adding Items ---")
    fruits = ["apple"]
    print(f"Start: {fruits}")

    fruits = fruits + ["apricot"]
    print(f"After fruits + ['apricot']: {fruits}")

    fruits.append("banana")
    print(f"After append('banana'): {fruits}")

    fruits.insert(1, "blueberry")
    print(f"After insert(1, 'blueberry'): {fruits}")

    fruits.extend(["cherry", "date"])
    print(f"After extend(['cherry', 'date']): {fruits}")

    print("\n--- Replacing Items ---")
    fruits[0] = "avocado"
    print(f"After fruits[0] = 'avocado': {fruits}")

    fruits[1:3] = ["blackberry", "clementine"]
    print(f"After fruits[1:3] = ['blackberry', 'clementine']: {fruits}")

    # Removing items
    print("\n--- Removing Items ---")
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Start: {fruits}")

    fruits.remove("banana")
    print(f"After remove('banana'): {fruits}")

    removed = fruits.pop()
    print(f"pop() returned: {removed}")
    print(f"After pop(): {fruits}")

    removed = fruits.pop(0)
    print(f"pop(0) returned: {removed}")
    print(f"After pop(0): {fruits}")

    del fruits[0]
    print(f"After del fruits[0]: {fruits}")

    fruits.clear()
    print(f"After clear(): {fruits}")

    # Finding items
    print("\n--- Finding Items ---")
    numbers = [10, 20, 30, 20, 40, 20]
    print(f"numbers = {numbers}")
    print(f"index(30) = {numbers.index(30)}")
    print(f"count(20) = {numbers.count(20)}")

    # Sorting
    print("\n--- Sorting ---")
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {unsorted}")

    unsorted.sort()
    print(f"After sort(): {unsorted}")

    unsorted.sort(reverse=True)
    print(f"After sort(reverse=True): {unsorted}")

    unsorted.reverse()
    print(f"After reverse(): {unsorted}")

    # sorted() vs sort()
    print("\n--- sorted() vs sort() ---")
    original = [3, 1, 4, 1, 5]
    new_list = sorted(original)
    print(f"Original: {original}")
    print(f"sorted(original): {new_list}")
    return 0


raise SystemExit(main(sys.argv))
