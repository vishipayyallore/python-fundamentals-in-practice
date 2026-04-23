# Filename: src/L1/S4/01_conditionals.py
# Session 4: Conditionals — practice script

print("=== Conditional Statements Demo ===\n")

# For now, type whole numbers only for age (we handle bad input in a later session).
print("(Tip: use digits only for age—e.g. 16, not sixteen.)\n")

age = int(input("Enter your age: "))

# Simple if-else
if age >= 18:
    print("You are an adult! 🧑")
else:
    print("You are a minor! 👶")

# This line is NOT inside the if/else—it always runs after that block finishes.
print("This line runs no matter which branch ran above.")

# if-elif-else chain
print("\n=== Grade Calculator ===")
print("(Tip: enter an integer score 0–100.)\n")
print("Think about: What band is 89? 100? 101? (Code uses >=, so boundaries matter.)\n")

score = int(input("Enter your score (0-100): "))

# Grades are integer bands; 89.9 would need floats—try that in the REPL later.
if score >= 90:
    grade = "A"
    message = "Excellent! 🌟"
elif score >= 80:
    grade = "B"
    message = "Great job! 👍"
elif score >= 70:
    grade = "C"
    message = "Good work! 😊"
elif score >= 60:
    grade = "D"
    message = "You passed! 📝"
else:
    grade = "F"
    message = "Keep trying! 💪"

# Only ONE of the above branches runs (first True condition)
print(f"\nYour grade: {grade}")
print(f"Message: {message}")

# Nested conditionals — inner if/else only runs when the outer if is True.
print("\n=== Movie Theater ===")
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"

if has_ticket:
    # Second question only matters if the first condition (has ticket) is True.
    # Reusing the name `age` overwrites the earlier value—only one `age` exists at a time.
    age = int(input("What's your age? "))
    if age >= 18:
        print("Enjoy the R-rated movie! 🎬")
    else:
        print("Here's your PG movie ticket! 🎥")
else:
    print("Please buy a ticket at the counter. 🎫")
