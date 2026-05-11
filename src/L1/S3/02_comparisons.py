# Filename: src/L1/S3/02_comparisons.py
# Session 3: Comparisons — True/False is the on-ramp to decisions (Session 4)

print("=== Comparison operators ===\n")
print("👉 Guess the output before we print (True or False?)\n")

# Basic comparisons
x, y = 10, 5
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y:  {x > y}")
print(f"x < y:  {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# = vs == (biggest beginner mix-up)
print("\n=== Common mistake: = (store) vs == (compare) ===")
x = 5
print("x = 5  →  stores 5 in x (assignment)")
print("x == 5 ?", x == 5, "  →  compares, safe inside print()")
# You cannot write: print(x = 5)  # assignment in expression position — invalid / wrong tool

print("\n=== Chained comparisons ===\n")
age = 25
print(f"age = {age}")
print(f"Is age between 18 and 65? {18 <= age <= 65}")

score = 75
print(f"score = {score}")
print(f"Is score between 70 and 80? {70 <= score <= 80}")

# Session 4 preview: comparison → future "if"
print("\n=== From compare to 'decision' (Session 4 next) ===\n")
age = int(input("Enter your age: "))
print("Can vote (age >= 18)?", age >= 18)
print(
    "👉 This expression is True or False — if/else will *act* on that next session.\n"
)

# Grade check (reuses "thinking" with another input)
print("--- Test score check ---")
test_score = int(input("Enter your test score (0-100): "))

print(f"\nYour score: {test_score}")
print(f"Is passing (>= 60)? {test_score >= 60}")
print(f"Is excellent (>= 90)? {test_score >= 90}")
print(f"Is in B range (80-89)? {80 <= test_score <= 89}")
