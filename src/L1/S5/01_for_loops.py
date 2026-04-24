# Filename: src/L1/S5/01_for_loops.py
# Session 5: Loops & Iteration — for loops and range

print("=== Session 5: for loops ===\n")

# Why for-loop: use it when the number of repeats is known.
print("Count from 1 to 5:")
for number in range(1, 6):
    print(number)

print("\nEven numbers from 2 to 10:")
for even in range(2, 11, 2):
    print(even)

print("\nCountdown with for-loop:")
for left in range(5, 0, -1):
    print(f"T-minus {left}")
print("🚀 Lift off!")

# Nested loop: outer loop = rows, inner loop = columns.
# Why nested loops matter: they help build grid/pattern style output.
print("\nSimple pattern:")
for row in range(1, 4):
    line = ""
    for _ in range(row):
        line += "*"
    print(line)
