"""Session 6 capstone: looped calculator with quit, continue, and validation."""

# Filename: src/L1/S6/04_calculator_loop.py

import sys

HELP_TEXT = """04_calculator_loop.py

Purpose
    Build a calculator that repeats until the learner quits, using `while True`,
    `break`, `continue`, and numeric validation.

Usage
    python src/L1/S6/04_calculator_loop.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 6 Capstone: Loop Calculator ===")
    print("Operations: +  -  *  /")
    print("Type q to quit.\n")

    while True:
        operation = input("Choose operation (+, -, *, /) or q to quit: ").strip().lower()

        # break: exit the loop entirely when the user is done
        if operation == "q":
            print("Goodbye!")
            break

        # continue: reject invalid input early, go back to the top of the loop
        if operation not in {"+", "-", "*", "/"}:
            print("Invalid operation. Choose +, -, *, /, or q.\n")
            continue

        first_raw = input("Enter first number: ").strip()
        second_raw = input("Enter second number: ").strip()

        # Inline numeric validation (no helper import needed here)
        # Why: strip one leading minus, then the remainder must be digits with at most one dot
        first_clean = first_raw[1:] if first_raw.startswith("-") else first_raw
        second_clean = second_raw[1:] if second_raw.startswith("-") else second_raw

        first_valid = (
            first_clean not in {"", "."} and first_clean.count(".") <= 1 and first_clean.replace(".", "", 1).isdigit()
        )
        second_valid = (
            second_clean not in {"", "."} and second_clean.count(".") <= 1 and second_clean.replace(".", "", 1).isdigit()
        )

        if not first_valid or not second_valid:
            print("Invalid number. Use digits like 10, -3, or 4.5.\n")
            continue  # ask again without crashing

        first = float(first_raw)
        second = float(second_raw)

        if operation == "+":
            result = first + second
            print(f"Result: {first} + {second} = {result}\n")
        elif operation == "-":
            result = first - second
            print(f"Result: {first} - {second} = {result}\n")
        elif operation == "*":
            result = first * second
            print(f"Result: {first} * {second} = {result}\n")
        else:
            # Why: guard against ZeroDivisionError before attempting division
            if second == 0:
                print("Cannot divide by zero.\n")
            else:
                result = first / second
                print(f"Result: {first} / {second} = {result}\n")
    return 0


raise SystemExit(main(sys.argv))
