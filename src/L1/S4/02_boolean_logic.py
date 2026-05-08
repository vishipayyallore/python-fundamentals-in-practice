# Filename: src/L1/S4/02_boolean_logic.py
# Session 4: Boolean logic — practice script

print("=== Boolean Logic Demo ===\n")
print("(Use digits for age; yes/no for the other prompts.)\n")

# Using 'and' — interactive so you reason about real values
print("--- AND operator ---")
age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ").lower() == "yes"

can_drive = age >= 18 and has_license
print(f"Age: {age}, Has License: {has_license}")
print(f"Can drive? {can_drive}")
print(
    "Evaluate: (age >= 18) and (has_license) — mentally check each part, then the whole 'and'."
)
print("(Both must be True for 'and' to be True.)\n")

# Using 'or'
print("--- OR operator ---")
is_weekend = input("Is it weekend? (yes/no): ").lower() == "yes"
is_holiday = input("Is it a holiday? (yes/no): ").lower() == "yes"

can_relax = is_weekend or is_holiday
print(f"Weekend: {is_weekend}, Holiday: {is_holiday}")
print(f"Can relax? {can_relax}")
print("(At least one True is enough for 'or' to be True.)\n")

# Using 'not'
print("--- NOT operator ---")
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
go_outside = not is_raining
print(f"Is raining: {is_raining}")
print(f"Go outside? {go_outside}")
print("('not' flips True/False.)\n")

# Combined example — age is reused from the first block
# Reusing 'age' from earlier input — same value continues here
print("=== Discount Calculator ===")
is_member = input("Are you a store member? (yes/no): ").lower() == "yes"

# Seniors (65+) OR members get discount — mentally check each side of "or"
if age >= 65 or is_member:
    print("🎉 You get a 20% discount!")
    print(
        "   (Why? Ask: is age >= 65? is member? If *either* is True, the whole 'or' is True.)"
    )
else:
    print("Regular price applies.")
    print("   (Why? Both age >= 65 and membership were False, so the 'or' is False.)")

# Bonus: AND on top of the earlier OR-style policy — combining ideas in one program
if age < 25 and is_member:
    print("🌟 BONUS: Young member extra 5% off!")
    print("   (This needs BOTH: under 25 AND member—'and', not 'or'.)")
