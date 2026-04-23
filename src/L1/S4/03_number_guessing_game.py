# Filename: src/L1/S4/03_number_guessing_game.py
# Session 4: Hero demo — one guess only; loops for multiple tries come in Session 5.

import random

print("=" * 40)
print("🎯 NUMBER GUESSING GAME 🎯")
print("=" * 40)
print("\nI'm thinking of a number between 1 and 10.")
print("Can you guess it?\n")
print("One attempt in this script—next session we add loops for many tries.\n")
print("Use a whole number for your guess (letters will error until we learn handling).\n")

# Generate secret number
secret = random.randint(1, 10)

# Instructor demo only: set True to show the secret while teaching branches—then False for learners.
REVEAL_SECRET_FOR_DEMO = False
if REVEAL_SECRET_FOR_DEMO:
    print(f"(Demo only — turn REVEAL_SECRET_FOR_DEMO off for a real game: secret is {secret})\n")

# Get player's guess (reminder in the moment for live sessions)
print("(Enter a number like 5, not the word five — same rule as other int inputs in this level.)")
guess = int(input("Enter your guess (1-10): "))

# Boundary check — reinforces comparisons and 'or'
if guess < 1 or guess > 10:
    print("\nPlease enter a number between 1 and 10 (inclusive). Run again to play.")
else:
    # Check the guess
    if guess == secret:
        print("\n🎉 CORRECT! You're a mind reader!")
    elif guess < secret:
        print(f"\n📈 Too low! The number was {secret}.")
    else:
        print(f"\n📉 Too high! The number was {secret}.")

    # How far off? (only when guess was in 1..10)
    # abs() gives positive difference (distance between numbers)
    difference = abs(guess - secret)
    if difference == 0:
        print("Perfect guess!")
    elif difference == 1:
        print("So close! Just off by 1!")
    elif difference <= 3:
        print("Not bad, you were in the ballpark!")
    else:
        print("Way off! Better luck next time!")

print("\n" + "=" * 40)
print("Thanks for playing! 🎮")
print("=" * 40)
