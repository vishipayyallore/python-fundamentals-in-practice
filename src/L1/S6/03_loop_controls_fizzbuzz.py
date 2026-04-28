# Filename: src/L1/S6/03_loop_controls_fizzbuzz.py
# Session 5: Loops & Iteration — break, continue, pass, and FizzBuzz

print("=== Loop controls demo ===\n")

print("continue demo (skip 3):")
for value in range(1, 6):
    if value == 3:
        # Why continue: skip this one case, keep loop alive for others.
        continue
    print(value)

print("\nbreak demo (stop at 4):")
for value in range(1, 8):
    if value == 4:
        # Why break: we are done with the loop entirely.
        break
    print(value)

print("\npass demo (placeholder branch):")
for value in range(1, 4):
    if value == 2:
        # pass keeps syntax valid when you intentionally do nothing.
        pass
    print(f"Value: {value}")

print("\nFizzBuzz 1..20:")
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
