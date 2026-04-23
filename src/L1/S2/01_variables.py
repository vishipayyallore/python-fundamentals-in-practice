# Filename: src/L1/S2/01_variables.py
# Session 2: Variables — practice: names, reuse, memory

# --- Hook: where is the value? Why print twice? ---
print("=== Hook: same name, two prints ===")
name = input("Enter your name: ")
print(name)
print(name)

print("\n👉 Variables store values in memory so you can reuse them under one name.\n")

# --- Reuse with a literal (same idea, no typing) ---
print("=== Reuse example (literal) ===")
name = "Alice"
print(name)
print(name)
print(f"Hello, {name}")

# Add more names — same `name` still "Alice" here
age = 25
height = 5.9
is_student = True

# Display the variables
print("\n=== Variable examples ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")

# Show variable types
print("\n=== Variable types (what kind of value) ===")
print(f"name is {type(name)}")
print(f"age is {type(age)}")
print(f"height is {type(height)}")
print(f"is_student is {type(is_student)}")

# Variables can be reassigned
print("\n=== Reassigning variables ===")
age = 26  # Changed from 25 to 26
print(f"Updated age: {age}")

# Dynamic typing: same name can point to a different type later
print("\n=== Dynamic typing example ===")
value = 25
print(f"value = {value}, type = {type(value)}")

value = "Now I'm a string!"
print(f"value = {value}, type = {type(value)}")
