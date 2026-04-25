# Filename: src/L1/S5/02_while_loops.py
# Session 5: Loops & Iteration — while loops and conditions

print("=== Session 5: while loops ===\n")

# Why while-loop: repeat until a condition becomes False.
# The update step is critical; without it, loops may never end.
print("Countdown with while-loop:")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("Done!\n")

print("Type short notes (type 'quit' to stop):")
note = input("Note: ").strip().lower()
while note != "quit":
    print(f"Saved note: {note}")
    note = input("Next note (or 'quit'): ").strip().lower()

print("Loop ended because you entered 'quit'.")
