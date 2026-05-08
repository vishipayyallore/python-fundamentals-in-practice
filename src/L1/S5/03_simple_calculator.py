# Filename: src/L1/S5/03_simple_calculator.py
# Mini Project 1: Simple Calculator (single run)
# Run from any directory: python src/L1/S5/03_simple_calculator.py

import os
import sys

# Allow imports from this folder regardless of working directory
sys.path.insert(0, os.path.dirname(__file__))

from calculator_utils import is_valid_number_text

print("=== Mini Project 1: Simple Calculator ===")
print("Supported operations: +  -  *  /")


operation = input("Choose operation (+, -, *, /): ").strip()

# Why: fail fast on unknown operations so the program stays predictable.
if operation not in {"+", "-", "*", "/"}:
    print("Invalid operation. Please choose one of: +, -, *, /")
else:
    first_raw = input("Enter first number: ").strip()
    second_raw = input("Enter second number: ").strip()

    # Why: input() returns text; we validate text before float conversion to avoid runtime crashes.
    first_is_number = is_valid_number_text(first_raw)
    second_is_number = is_valid_number_text(second_raw)

    if not first_is_number or not second_is_number:
        print("Invalid number input. Use digits like 10, -3, or 4.5.")
    else:
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
