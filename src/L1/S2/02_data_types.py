# Filename: src/L1/S2/02_data_types.py
# Session 2: The four common types — predict, then run

print("=== Python's four fundamental types ===\n")
print("Guess the type before we print: int or float? str or int? (Ask → run → explain.)\n")

# 1. Integers (int)
print("1. INTEGERS (int):")
print("   👉 Guess: int or float for 25, -10, 0?")
age = 25
temperature = -10
count = 0
print(f"   age = {age} → {type(age)}")
print(f"   temperature = {temperature} → {type(temperature)}")
print(f"   count = {count} → {type(count)}")

# 2. Floats
print("\n2. FLOATING-POINT (float):")
print("   👉 Guess: 5.9 and 19.99 — int or float?")
height = 5.9
price = 19.99
pi = 3.14159
print(f"   height = {height} → {type(height)}")
print(f"   price = {price} → {type(price)}")
print(f"   pi = {pi} → {type(pi)}")

# 3. Strings
print("\n3. STRINGS (str):")
name = "Alice"
message = "Hello, World!"
favorite_color = "blue"
print(f"   name = {name} → {type(name)}")
print(f"   message = {message} → {type(message)}")
print(f"   favorite_color = {favorite_color} → {type(favorite_color)}")

# 4. Booleans
print("\n4. BOOLEANS (bool):")
is_student = True
is_graduated = False
has_license = True
print(f"   is_student = {is_student} → {type(is_student)}")
print(f"   is_graduated = {is_graduated} → {type(is_graduated)}")
print(f"   has_license = {has_license} → {type(has_license)}")

# Common confusion: same digits, different types
print("\n=== Common confusion: '25' vs 25 ===")
text_25 = "25"
num_25 = 25
print(type(text_25))  # str
print(type(num_25))  # int
print('Quotes mean text (str), even if digits look like a number.\n')

# type() and light isinstance (keep isinstance minimal for 30 min)
print("=== type() and isinstance (quick) ===")
print(f"type(age): {type(age)}")
print(f"isinstance(age, int): {isinstance(age, int)}")
