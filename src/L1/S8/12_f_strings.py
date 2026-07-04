"""Modern string formatting with f-strings."""

# Filename: src/L1/S8/12_f_strings.py

import sys

HELP_TEXT = """12_f_strings.py

Purpose
    Demonstrate how f-strings insert variables, expressions, and method
    results directly inside a string.

Usage
    python src/L1/S8/12_f_strings.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    kilos = 2
    vegetable = "tomatoes"
    market_message = f"I bought {kilos} kilos of {vegetable} from the market."

    print(f"kilos = {kilos}")
    print(f"vegetable = {vegetable!r}\n")
    print(market_message)

    age_message = f"I am {2 ** 5} years old in this pretend example."
    print("\n=== Expression inside braces ===")
    print(age_message)

    name = "joseph"
    shout_name = f"My name is {name.upper()}."
    print("\n=== Method call inside braces ===")
    print(shout_name)

    print("\nRemember:")
    print("- Add f before the opening quote to create an f-string.")
    print("- Put variables inside braces to insert their values.")
    print("- Expressions such as 2 ** 5 are evaluated before printing.")
    print("- Method calls such as name.upper() can be used inside braces.")

    return 0


raise SystemExit(main(sys.argv))
