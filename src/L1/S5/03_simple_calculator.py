"""Mini Project 1: single-run calculator with validated numeric input."""

# Filename: src/L1/S5/03_simple_calculator.py

import os
import sys

HELP_TEXT = """03_simple_calculator.py

Purpose
    Run a single calculator operation after validating the chosen operator and
    both number inputs.

Usage
    python src/L1/S5/03_simple_calculator.py
"""

# Allow imports from this folder regardless of working directory
sys.path.insert(0, os.path.dirname(__file__))

from calculator_utils import is_valid_number_text


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Mini Project 1: Simple Calculator ===")
    print("Supported operations: +  -  *  /")

    operation = input("Choose operation (+, -, *, /): ").strip()

    # Why: fail fast on unknown operations so the program stays predictable.
    if operation not in {"+", "-", "*", "/"}:
        print("Invalid operation. Please choose one of: +, -, *, /")
        return 0

    first_raw = input("Enter first number: ").strip()
    second_raw = input("Enter second number: ").strip()

    # Why: input() returns text; we validate text before float conversion to avoid runtime crashes.
    first_is_number = is_valid_number_text(first_raw)
    second_is_number = is_valid_number_text(second_raw)

    if not first_is_number or not second_is_number:
        print("Invalid number input. Use digits like 10, -3, or 4.5.")
        return 0

    first = float(first_raw)
    second = float(second_raw)

    if operation == "+":
        result = first + second
        print(f"Result: {first} + {second} = {result}")
    elif operation == "-":
        result = first - second
        print(f"Result: {first} - {second} = {result}")
    elif operation == "*":
        result = first * second
        print(f"Result: {first} * {second} = {result}")
    else:
        # Why: dividing by zero is undefined, so we block it with a clear message.
        if second == 0:
            print("Cannot divide by zero.")
        else:
            result = first / second
            print(f"Result: {first} / {second} = {result}")
    return 0


raise SystemExit(main(sys.argv))
