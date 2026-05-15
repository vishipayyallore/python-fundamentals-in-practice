# Filename: src/L1/S2/03_type_conversion.py
# Session 2: Conversion — why "10" + "5" is not 15, and when int() saves you

print("=== What happens without conversion (strings) ===\n")
num1 = "10"
num2 = "5"
print("num1 = '10', num2 = '5' (both strings — like input() gives you).")
print("Using +: ", repr(num1 + num2), "  ← not 15; it concatenates text!")
print("👉 Ask: 15 or 105? Then you feel why type matters.\n")

print("=== Fix: convert, then do math ===")
num1 = int(num1)
num2 = int(num2)
print("After int():", num1 + num2, "  ← now real addition.\n")

print("👉 input() always returns a string → convert when you need numbers (Session 1 + Session 2).\n")

# More conversion patterns
print("=== Type conversion reference ===\n")

print("1. TO int:")
age_str = "25"
print(f"   int({repr(age_str)}) → {int(age_str)}")

print("\n2. TO float:")
price_str = "19.99"
print(f"   float({repr(price_str)}) → {float(price_str)}")

print("\n3. TO str:")
age = 25
print(f"   str({age}) → {repr(str(age))}")

print("\n4. TO bool (samples):")
print(f"   bool(1)={bool(1)}, bool(0)={bool(0)}, bool('')={bool('')}, bool('hi')={bool('hi')}")

# int() can fail: int("hello") — mention in class, not required to demo crash in script
print("\n=== Practical: simulated input (always str) ===")
age_input = "25"
age = int(age_input)
print(f"   As if from input: {repr(age_input)} → int → {age}, age + 5 = {age + 5}")

print("\n=== Combine text and numbers ===")
name = "Alice"
age = 25
print("I am " + str(age) + " years old")
print(f"I am {age} years old  (f-string — usually easier)")
