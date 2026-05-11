# Filename: src/L1/S3/01_arithmetic.py
# Session 3: Arithmetic — predict first, then run

print("👉 Predict before running (ask: 15/4 vs 15//4; then run):\n")
print("What is 15 / 4  ?  (true division)")
print("What is 15 // 4 ?  (floor division)\n")

print("=== Arithmetic operators (a=15, b=4) ===\n")
a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Addition:       a + b = {a + b}")
print(f"Subtraction:    a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(
    f"Division:       a / b = {a / b}   👉 / always gives float in Python 3, even 10/2 → 5.0"
)
print(f"Floor division: a // b = {a // b}")
print(f"Modulo:         a % b = {a % b}")
print(f"Exponentiation: a ** 2 = {a ** 2}")

print("\n=== Common confusion: / vs // ===")
print("10 / 2  =", 10 / 2)  # 5.0
print("10 // 2 =", 10 // 2)  # 5

print("\n=== Practical examples ===\n")

# Even or odd
number = 17
remainder = number % 2
if remainder == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# Square root via **
num = 144
sqrt = num**0.5
print(f"Square root of {num} is {sqrt}")

# Precedence — prediction loop: 14 or 20?
print("\n=== Operator precedence (predict, then run) ===\n")
print("👉 What is 2 + 3 * 4?  (14 or 20?)\n")
print(f"2 + 3 * 4   = {2 + 3 * 4}   # * before +")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}  # parens first")
print(f"2 ** 3 ** 2  = {2**3**2}   # ** groups right-to-left in Python")
