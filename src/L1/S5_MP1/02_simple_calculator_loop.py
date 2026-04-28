# Filename: src/L1/S5_MP1/02_simple_calculator_loop.py
# Mini Project 1: Simple Calculator (loop version)

from calculator_utils import is_valid_number_text

print("=== Mini Project 1: Simple Calculator (Loop) ===")
print("Operations: +  -  *  /")
print("Type q to quit.\n")


while True:
    operation = input("Choose operation (+, -, *, /) or q to quit: ").strip().lower()

    if operation == "q":
        print("Exiting calculator. Great job completing Mini Project 1!")
        break

    # Why: operation validation before numeric prompts gives faster, clearer feedback.
    if operation not in {"+", "-", "*", "/"}:
        print("Invalid operation. Choose +, -, *, /, or q.\n")
        continue

    first_raw = input("Enter first number: ").strip()
    second_raw = input("Enter second number: ").strip()

    # Why: validating text first prevents conversion failures and keeps the loop stable.
    first_is_number = is_valid_number_text(first_raw)
    second_is_number = is_valid_number_text(second_raw)

    if not first_is_number or not second_is_number:
        print("Invalid number input. Use digits like 10, -3, or 4.5.\n")
        continue

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
        # Why: division guard avoids a crash and teaches explicit edge-case handling.
        if second == 0:
            print("Cannot divide by zero.\n")
        else:
            result = first / second
            print(f"Result: {first} / {second} = {result}\n")
