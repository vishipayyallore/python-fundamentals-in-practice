# Filename: src/L1/S7/07_escape_sequences.py
"""Session 1 revisited — escape sequences in strings.

A backslash inside a string changes how the next character prints.
\\n and \\t help space out multi-line debug output; escaping quotes
prevents Python from ending a string early.
"""

import sys

HELP_TEXT = """07_escape_sequences.py

Purpose
    Practice escape sequences for formatting and special characters.
    \\n and \\t are especially useful for structuring multi-line debug output.

Usage
    python src/L1/S7/07_escape_sequences.py

Topics Covered
    - New line: \\n
    - Tab space: \\t
    - Backspace effect: \\b
    - Escaping quotes inside strings
"""


def demo_newline() -> None:
    print("=== New line (\\n) ===")
    print("Course: Python Fundamentals\nTrack: Beginner Practice")


def demo_tab() -> None:
    print("\n=== Tab (\\t) ===")
    print("Name:\tPython Fundamentals")
    print("Level:\t\tBeginner")


def demo_backspace() -> None:
    print("\n=== Backspace (\\b) ===")
    print("Plan A\bB")


def demo_escaping_quotes() -> None:
    print("\n=== Escaping apostrophe ===")
    print("Using double quotes:", "I'm building Python skills")
    print('Using escape in single quotes:', 'I\'m building Python skills')


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_newline()
    demo_tab()
    demo_backspace()
    demo_escaping_quotes()
    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
