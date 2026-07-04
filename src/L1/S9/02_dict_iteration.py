# Filename: src/L1/S9/02_dict_iteration.py

print("=== Dictionary Iteration Demo ===\n")

grades = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}

# Iterating over keys
print("--- Iterating Over Keys ---")
for name in grades:
    print(f"Student: {name}")

# Iterating over values
print("\n--- Iterating Over Values ---")
for grade in grades.values():
    print(f"Grade: {grade}")

# Iterating over items
print("\n--- Iterating Over Items ---")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# Practical example: Statistics
print("\n--- Statistics ---")
total = sum(grades.values())
count = len(grades)
average = total / count
print(f"Total points: {total}")
print(f"Number of students: {count}")
print(f"Average grade: {average:.1f}")

# Find highest and lowest
print("\n--- Finding Extremes ---")
highest_name = max(grades, key=grades.get)
lowest_name = min(grades, key=grades.get)
print(f"Highest: {highest_name} ({grades[highest_name]})")
print(f"Lowest: {lowest_name} ({grades[lowest_name]})")

# Filter students with A grades
print("\n--- A Students (90+) ---")
a_students = []
for name, grade in grades.items():
    if grade >= 90:
        a_students.append(name)
print(f"A students: {a_students}")

# Dictionary comprehension preview
print("\n--- Dictionary Comprehension (Preview) ---")
passed = {name: grade for name, grade in grades.items() if grade >= 70}
print(f"Passed students: {passed}")
