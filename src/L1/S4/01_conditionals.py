# Filename: src/L1/S4/01_conditionals.py

print("=== Conditional Statements Demo ===\n")

# Simple if-else
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult! 🧑")
else:
    print("You are a minor! 👶")
print("I belong to main block")

# if-elif-else chain
print("\n=== Grade Calculator ===")
score = int(input("Enter your score (0-100): "))

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

print(f"\nYour grade: {grade}")
print(f"Message: {message}")

# Nested conditionals
print("\n=== Movie Theater ===")
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"

if has_ticket:
    age = int(input("What's your age? "))
    if age >= 18:
        print("Enjoy the R-rated movie! 🎬")
    else:
        print("Here's your PG movie ticket! 🎥")
else:
    print("Please buy a ticket at the counter. 🎫")
