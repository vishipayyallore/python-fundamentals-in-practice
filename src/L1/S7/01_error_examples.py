"""Session 7: common Python errors and beginner-friendly fixes."""

# Filename: src/L1/S7/01_error_examples.py

import sys

HELP_TEXT = """01_error_examples.py

Purpose
    Show how common Python exceptions look and pair each one with a simple fix.

Usage
    python src/L1/S7/01_error_examples.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Error Examples Demo ===\n")

    # Example 1: NameError
    print("--- NameError Example ---")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")
        print("Fix: Define the variable before using it\n")

    # Example 2: TypeError
    print("--- TypeError Example ---")
    try:
        print("Hello" + 5)
    except TypeError as e:
        print(f"TypeError: {e}")
        print("Fix: Convert to same type - 'Hello' + str(5)\n")

    # Example 3: ValueError
    print("--- ValueError Example ---")
    try:
        print(int("hello"))
    except ValueError as e:
        print(f"ValueError: {e}")
        print("Fix: Make sure string contains a valid number\n")

    # Example 4: IndexError
    print("--- IndexError Example ---")
    try:
        my_list = [1, 2, 3]
        print(my_list[10])
    except IndexError as e:
        print(f"IndexError: {e}")
        print("Fix: Use valid index (0 to len-1)\n")

    # Example 5: ZeroDivisionError
    print("--- ZeroDivisionError Example ---")
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        print("Fix: Check if divisor is zero before dividing\n")

    # Example 6: KeyError
    print("--- KeyError Example ---")
    try:
        my_dict = {"name": "Alice"}
        print(my_dict["age"])
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Fix: Check if key exists or use .get() method\n")

    print("=== End of Error Examples ===")
    return 0


raise SystemExit(main(sys.argv))
