"""Session 7: PEP 8 naming, spacing, and comment quality (before vs after)."""

# Filename: src/L1/S7/04_pep8_style_refactor.py

import sys

HELP_TEXT = """04_pep8_style_refactor.py

Purpose
    Compare cramped style with PEP 8-friendly names, spacing, and # Why: comments.

Usage
    python src/L1/S7/04_pep8_style_refactor.py
"""


def cramped_style_demo() -> None:
    """Shows patterns beginners often write — hard to read in teams."""
    print("--- Before: cramped style (avoid in real projects) ---")
    print("Example of what NOT to write: x=10; y=20; z=x+y  (no spaces, one-letter names)")
    x = 10
    y = 20
    z = x + y
    print(f"Same math with bad names: z={z}\n")


def pep8_style_demo() -> None:
    """Same idea with readable names and spacing."""
    print("--- After: PEP 8 friendly ---")
    first_value = 10
    second_value = 20
    total = first_value + second_value
    # Why: names describe intent; spaces around = and + improve scanability.
    print(f"first_value={first_value}, second_value={second_value}, total={total}\n")


def comment_quality_demo() -> None:
    """Good comments explain decisions, not obvious actions."""
    print("--- Comment quality ---")
    user_text = "42"
    # Why: input() always returns str; validate before int() to avoid ValueError.
    if user_text.isdigit():
        answer = int(user_text)
        print(f"Converted safely: {answer}")
    else:
        print("Skipped conversion — not all digits.")
    print()


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: PEP 8 style refactor ===\n")
    cramped_style_demo()
    pep8_style_demo()
    comment_quality_demo()
    print("Revisit src/L1/S5/01_PEP8_naming_and_spacing.py for the full five-rule tour.")
    return 0


raise SystemExit(main(sys.argv))
