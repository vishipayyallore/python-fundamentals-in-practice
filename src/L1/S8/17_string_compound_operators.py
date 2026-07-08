"""String compound operators — +=, *=, and print(*text) for spaced character output."""

# Filename: src/L1/S8/17_string_compound_operators.py

import sys

HELP_TEXT = """17_string_compound_operators.py

Purpose
    Demonstrate how += and *= update string variables in place, and how
    print(*text) spreads each character into separate print arguments.

Usage
    python src/L1/S8/17_string_compound_operators.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Compound assignment with strings ===")
    teams = "Lakers"
    print(f"teams starts as {teams!r}")

    combined = teams + " Celtics"
    print(f"teams + ' Celtics'          -> {combined!r}")

    teams = combined
    teams += " Dallas"
    print(f"After += ' Dallas'          -> {teams!r}")

    repeated = teams * 3
    print(f"teams * 3                   -> {repeated!r}")

    chant = "Go! "
    chant *= 4
    print(f"\nchant after *= 4           -> {chant!r}")

    print("\n=== print(*text) spreads characters ===")
    city = "barcelona"
    print(f"city = {city!r}")
    print("print(*city) output:")
    print(*city)

    print("\nKey ideas")
    print("-" * 40)
    print("- + joins strings into one larger string.")
    print("- += updates the same variable with extra text.")
    print("- * repeats a string a chosen number of times.")
    print("- print(*text) prints each character as a separate argument.")

    print("\nMini challenge")
    print("-" * 40)
    print("Try building a banner with '=' * 20 and a team name in the middle.")

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
