# Filename: src/L1/S4/02_boolean_logic.py

print("=== Boolean Logic Demo ===\n")

# Using 'and'
print("--- AND operator ---")
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(f"Age: {age}, Has License: {has_license}")
print(f"Can drive? {can_drive}")

# Using 'or'
print("\n--- OR operator ---")
is_weekend = False
is_holiday = True

can_relax = is_weekend or is_holiday
print(f"Weekend: {is_weekend}, Holiday: {is_holiday}")
print(f"Can relax? {can_relax}")

# Using 'not'
print("\n--- NOT operator ---")
is_raining = False
go_outside = not is_raining
print(f"Is raining: {is_raining}")
print(f"Go outside? {go_outside}")

# Combined example
print("\n=== Discount Calculator ===")
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

# Seniors (65+) OR members get discount
if age >= 65 or is_member:
    print("🎉 You get a 20% discount!")
else:
    print("Regular price applies.")

# Special combo: young member
if age < 25 and is_member:
    print("🌟 BONUS: Young member extra 5% off!")
