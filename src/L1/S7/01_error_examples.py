"""Session 7: guided tour of common runtime errors and how to read them."""

# Filename: src/L1/S7/01_error_examples.py

import sys

HELP_TEXT = """01_error_examples.py

Purpose
    Show NameError, TypeError, ZeroDivisionError, and ValueError in action.
    Each demo catches one error so the script can continue — focus on the message.

Usage
    python src/L1/S7/01_error_examples.py
"""


def demo_name_error() -> None:
    print("--- NameError ---")
    print("Happens when Python cannot find a variable name.")
    try:
        print(unknown_label)  # noqa: F821 — intentional for teaching
    except NameError as err:
        print(f"Message: {err}")
    print("Fix: define the variable before you use it.\n")


def demo_type_error() -> None:
    print("--- TypeError ---")
    print("Happens when an operation does not support the types you gave it.")
    try:
        total = "5" + 3
        print(total)
    except TypeError as err:
        print(f"Message: {err}")
    print('Fix: convert types first, e.g. int("5") + 3.\n')


def demo_zero_division() -> None:
    print("--- ZeroDivisionError ---")
    print("Happens when you divide by zero.")
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError as err:
        print(f"Message: {err}")
    print("Fix: check the divisor before dividing.\n")


def demo_value_error() -> None:
    print("--- ValueError ---")
    print("Happens when a function gets the right type but an invalid value.")
    try:
        converted = int("not-a-number")
        print(converted)
    except ValueError as err:
        print(f"Message: {err}")
    print('Fix: validate input before calling int() on text.\n')


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: Common runtime errors ===\n")
    print("Read the last line of each message — it usually names the problem.\n")

    demo_name_error()
    demo_type_error()
    demo_zero_division()
    demo_value_error()

    print("Tip: scroll up in your terminal to see the full traceback when you run broken code.")
    return 0


raise SystemExit(main(sys.argv))
