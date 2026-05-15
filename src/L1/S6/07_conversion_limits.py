"""Session 2: Conversion limits — what you lose, and what fails.

Teaching arc:
  1. int(float) truncates — the decimal part is dropped, NOT rounded
  2. float(bool) — True becomes 1.0, False becomes 0.0
     (connects the bool-as-1/0 idea from 04_ to type conversion)
  3. try/except ValueError — catch a conversion that cannot succeed
     and explain why (preview of formal error-handling in S7)

"""

# Filename: src/L1/S6/07_conversion_limits.py

import sys

HELP_TEXT = """07_conversion_limits.py

Purpose
    Explore three conversion edge-cases that trip up beginners:
    int(float) truncates, float(bool) follows the bool-as-int rule,
    and int() on a word string raises ValueError.

Usage
    python src/L1/S6/07_conversion_limits.py
"""


# ---------------------------------------------------------------------------
# Section 1 — int(float) truncates; it does NOT round
# ---------------------------------------------------------------------------


def demo_truncation() -> None:
    """Show that int() drops the decimal part rather than rounding."""

    print("=== 1. int(float) - truncation, not rounding ===\n")

    readings = [5.2, 5.8, 5.5, -3.9]

    for r in readings:
        print(f"  int({r}) = {int(r)}")

    print()
    print("Note: int() always moves toward zero, regardless of the decimal.")
    print("      int(5.8) is 5, not 6.  int(-3.9) is -3, not -4.")
    print("      Use round() when you need conventional rounding.")


# ---------------------------------------------------------------------------
# Section 2 — float(bool) follows the bool-as-int rule
# ---------------------------------------------------------------------------


def demo_bool_to_float() -> None:
    """Show that True and False carry their integer value into float()."""

    print("\n=== 2. float(bool) - True is 1.0, False is 0.0 ===\n")

    print(f"  float(True)  = {float(True)}")
    print(f"  float(False) = {float(False)}")

    # Practical: a sensor flag used in a float calculation
    sensor_active = True
    weight_kg = 72.4
    effective_weight = float(sensor_active) * weight_kg
    print(f"\n  sensor_active={sensor_active!r}, weight={weight_kg}")
    print(f"  float(sensor_active) * weight = {effective_weight}")

    print()
    print("Note: bool is a subtype of int in Python (True==1, False==0).")
    print("      float() simply promotes that integer value to a float.")


# ---------------------------------------------------------------------------
# Section 3 — ValueError: int() on a non-numeric string
# ---------------------------------------------------------------------------


def demo_value_error() -> None:
    """Show what happens when int() cannot parse the string it receives."""

    print("\n=== 3. ValueError - when conversion is impossible ===\n")

    # A word string has no numeric meaning → int() raises ValueError.
    label = "september"
    print(f"  Attempting int({label!r}) ...")
    try:
        result = int(label)
        print(f"  Result: {result}")  # never reached
    except ValueError as err:
        print(f"  ValueError caught: {err}")

    print()

    # A numeric string works fine.
    score = "87"
    print(f"  Attempting int({score!r}) ...")
    converted = int(score)
    print(f"  Result: {converted}  type={type(converted).__name__}")

    print()
    print("Note: int() succeeds only when the string contains digits")
    print("      (optionally preceded by + or -).")
    print("      This is the same error you get from bad input() data --")
    print("      int(input('Enter a number: ')) crashes if the user types words.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_truncation()
    demo_bool_to_float()
    demo_value_error()
    return 0


raise SystemExit(main(sys.argv))
