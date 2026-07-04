"""Legacy percent-style string formatting for strings, integers, and floats."""

# Filename: src/L1/S8/16_percent_formatting.py

import sys

HELP_TEXT = """16_percent_formatting.py

Purpose
    Demonstrate percent-style string formatting for strings, integers, and
    floating-point values.

Usage
    python src/L1/S8/16_percent_formatting.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    school_template = "There are %s in the library."
    print(f"school_template = {school_template!r}\n")
    print(school_template % "students")
    print(school_template % "teachers")

    profile_template = "I am %d years old and my height is %.2f cm."
    print(f"\nprofile_template = {profile_template!r}\n")

    age = 29
    height = 172.4
    print(profile_template % (age, height))

    age = 35
    height = 168.95
    print(profile_template % (age, height))

    report_template = "%s scored %d marks and averaged %.1f per test."
    name = "Asha"
    total_marks = 438
    average = 87.6

    print("\nMixed placeholders")
    print("-" * 40)
    print(report_template % (name, total_marks, average))

    print("\nKey ideas")
    print("-" * 40)
    print("- %s inserts string data.")
    print("- %d inserts whole-number data.")
    print("- %.2f inserts a float rounded to 2 decimal places.")
    print("- Values must be passed in the same order as the placeholders.")

    print("\nReminder")
    print("-" * 40)
    print(
        "Modern Python often prefers f-strings, but percent formatting "
        "still appears in older code."
    )

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
