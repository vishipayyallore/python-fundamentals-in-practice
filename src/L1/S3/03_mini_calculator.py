# Filename: src/L1/S3/03_mini_calculator.py
# Session 3: Puts S1 input + S2 types + S3 operators in one place

print("👉 This combines everything so far: input, numbers, and many operations on the same data.\n")
print("=== Mini calculator ===\n")
print("(Enter numbers like 10 or 5.5 — plain digits/decimal.)\n")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform all operations
print(f"\n--- Results for {num1} and {num2} ---")
print(f"Addition:       {num1} + {num2} = {num1 + num2}")
print(f"Subtraction:    {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division by zero
if num2 != 0:
    print(f"Division:       {num1} / {num2} = {num1 / num2}")
    print(f"Floor division: {num1} // {num2} = {num1 // num2}")
    print(f"Modulo:         {num1} % {num2} = {num1 % num2}")
else:
    print("Division:       Cannot divide by zero!")
    print("Floor division: Cannot divide by zero!")
    print("Modulo:         Cannot divide by zero!")

# Guard: 0 raised to a negative exponent is undefined (ZeroDivisionError)
if num1 == 0 and num2 < 0:
    print("Power:          Cannot raise 0 to a negative power!")
else:
    print(f"Power:          {num1} ** {num2} = {num1**num2}")

print("\n👉 We just performed many operations on the same two values — that is real program behavior.\n")
print("👉 Which operation do you use most in real life? (No wrong answer — just notice.)\n")

print("✨ Calculation complete!")
