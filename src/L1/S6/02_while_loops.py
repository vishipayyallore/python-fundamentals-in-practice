"""Session 6: while loops, countdowns, and sentinel-controlled input."""

# Filename: src/L1/S6/02_while_loops.py

import sys

HELP_TEXT = """02_while_loops.py

Purpose
    Demonstrate a countdown loop and a sentinel-controlled input loop using
    `while` conditions.

Usage
    python src/L1/S6/02_while_loops.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 6: while loops ===\n")

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
    return 0


raise SystemExit(main(sys.argv))
