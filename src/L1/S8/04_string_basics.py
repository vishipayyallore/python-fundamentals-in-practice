"""Session 8 optional: string + and * operators (sequences)."""

# Filename: src/L1/S8/04_string_basics.py

import sys

HELP_TEXT = """04_string_basics.py

Purpose
    Show string concatenation (+) and repetition (*) — contrast with int + int.

Usage
    python src/L1/S8/04_string_basics.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: String operators ===\n")

    greeting = "Hello" + ", " + "Python"
    print(f"'Hello' + ', ' + 'Python' -> {greeting}")

    line = "-" * 20
    print(f"'-' * 20 -> {line}")

    print("\nMixing str + int raises TypeError:")
    try:
        broken = "age: " + 25
        print(broken)
    except TypeError as err:
        print(f"  {err}")
    print('Fix: "age: " + str(25)')
    return 0


raise SystemExit(main(sys.argv))
