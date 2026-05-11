# Filename: src/L1/S1/02_interactive_hello.py
# Session 1: Python Introduction & Environment Setup

# Interactive greeting script
print("=== Python Interactive Greeting ===")

# Get user input
name = input("What's your name? ")
age = input("How old are you? ")

# Display personalized message
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print("Nice to meet you!")

# Demonstrate built-in functions type() and help()
print("\n🔍 Let's explore Python's built-in functions:")
print(f"The name '{name}' is of type: {type(name)}")
print(f"The age '{age}' is of type: {type(age)}")

print(
    "\n⚠️ Important: Even when you type digits for age, input() still gives you a string (str)."
)
print("Next session: variables, types, and int(age) when you need a real number.")
print(
    "\nCuriosity: in the REPL, try  int('25')  — that turns digit text into a real integer."
)

print("\n💡 Want to learn more about a function? Try help()!")
print("For example: help(print) shows documentation for print function")
print("(You can try this in the Python shell later!)")
