# Filename: src/L1/S9/03_gradebook.py

"""
📚 Simple Gradebook Application
Demonstrates dictionaries, loops, and basic testing!
"""


def get_letter_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(grades_dict):
    """Calculate average of all grades in dictionary."""
    if len(grades_dict) == 0:
        return 0
    return sum(grades_dict.values()) / len(grades_dict)


def display_gradebook(grades_dict):
    """Display all students and their grades."""
    if len(grades_dict) == 0:
        print("📭 No students in gradebook!")
        return

    print("\n" + "=" * 40)
    print("📚 GRADEBOOK")
    print("=" * 40)
    print(f"{'Name':<15} {'Score':>8} {'Grade':>8}")
    print("-" * 40)

    for name, score in grades_dict.items():
        letter = get_letter_grade(score)
        print(f"{name:<15} {score:>8} {letter:>8}")

    print("-" * 40)
    avg = calculate_average(grades_dict)
    print(f"{'Average:':<15} {avg:>8.1f} {get_letter_grade(avg):>8}")
    print("=" * 40)


# Run tests first
print("🧪 Running tests...")

# Test get_letter_grade
assert get_letter_grade(95) == "A", "95 should be A"
assert get_letter_grade(85) == "B", "85 should be B"
assert get_letter_grade(75) == "C", "75 should be C"
assert get_letter_grade(65) == "D", "65 should be D"
assert get_letter_grade(55) == "F", "55 should be F"
assert get_letter_grade(90) == "A", "90 should be A (boundary)"

# Test calculate_average
test_grades = {"A": 100, "B": 80}
assert calculate_average(test_grades) == 90, "Average of 100 and 80 should be 90"
assert calculate_average({}) == 0, "Empty dict average should be 0"

print("✅ All tests passed!\n")

# Main application
print("=" * 50)
print("📚 GRADEBOOK APPLICATION")
print("=" * 50)

gradebook = {}

while True:
    print("\n--- Menu ---")
    print("1. Add student grade")
    print("2. View gradebook")
    print("3. Update grade")
    print("4. Remove student")
    print("5. Get student info")
    print("6. Quit")

    choice = input("\nEnter choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in gradebook:
            print(f"⚠️ {name} already exists! Use option 3 to update.")
        else:
            try:
                score = int(input("Enter score (0-100): "))
                if 0 <= score <= 100:
                    gradebook[name] = score
                    letter = get_letter_grade(score)
                    print(f"✅ Added: {name} - {score} ({letter})")
                else:
                    print("❌ Score must be between 0 and 100!")
            except ValueError:
                print("❌ Please enter a valid number!")

    elif choice == "2":
        display_gradebook(gradebook)

    elif choice == "3":
        if len(gradebook) == 0:
            print("📭 No students in gradebook!")
        else:
            name = input("Enter student name to update: ")
            if name in gradebook:
                try:
                    score = int(input("Enter new score (0-100): "))
                    if 0 <= score <= 100:
                        old_score = gradebook[name]
                        gradebook[name] = score
                        print(f"✅ Updated: {name} - {old_score} → {score}")
                    else:
                        print("❌ Score must be between 0 and 100!")
                except ValueError:
                    print("❌ Please enter a valid number!")
            else:
                print(f"❌ Student '{name}' not found!")

    elif choice == "4":
        if len(gradebook) == 0:
            print("📭 No students in gradebook!")
        else:
            name = input("Enter student name to remove: ")
            if name in gradebook:
                removed_score = gradebook.pop(name)
                print(f"🗑️ Removed: {name} (score: {removed_score})")
            else:
                print(f"❌ Student '{name}' not found!")

    elif choice == "5":
        if len(gradebook) == 0:
            print("📭 No students in gradebook!")
        else:
            name = input("Enter student name: ")
            if name in gradebook:
                score = gradebook[name]
                letter = get_letter_grade(score)
                print("\n📋 Student Info:")
                print(f"   Name: {name}")
                print(f"   Score: {score}")
                print(f"   Grade: {letter}")
            else:
                print(f"❌ Student '{name}' not found!")

    elif choice == "6":
        print("\n" + "=" * 50)
        print("👋 Goodbye! Keep learning!")
        print("=" * 50)
        break

    else:
        print("❌ Invalid choice! Please enter 1-6.")
