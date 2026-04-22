# Filename: src/L1/S4/03_number_guessing_game.py

import random

print("=" * 40)
print("🎯 NUMBER GUESSING GAME 🎯")
print("=" * 40)
print("\nI'm thinking of a number between 1 and 10.")
print("Can you guess it?\n")

# Generate secret number
secret = random.randint(1, 10)
print(f"(For testing purposes, the secret number is: {secret})")  # Remove or comment out in real game

# Get player's guess
guess = int(input("Enter your guess (1-10): "))

# Check the guess
if guess == secret:
    print("\n🎉 CORRECT! You're a mind reader!")
elif guess < secret:
    print(f"\n📈 Too low! The number was {secret}.")
else:
    print(f"\n📉 Too high! The number was {secret}.")

# Additional feedback
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
