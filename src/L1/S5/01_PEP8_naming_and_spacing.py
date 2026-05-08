"""PEP 8 Style Guide: Naming and Spacing Rules

This file demonstrates the five key PEP 8 naming and spacing rules
that make Python code clean, readable, and professional.
"""

# Filename: src/L1/S5/01_PEP8_naming_and_spacing.py

import sys

HELP_TEXT = """01_PEP8_naming_and_spacing.py

Purpose
    Demonstrate the five key PEP 8 style rules:
    1. Meaningful variable names (lowercase with underscores)
    2. Spaces around operators
    3. No spaces inside parentheses
    4. Space after commas
    5. Comments explain WHY, not WHAT

Usage
    python 01_PEP8_naming_and_spacing.py
"""


def demo_rule1_meaningful_names() -> None:
    """Rule 1: Use meaningful names with snake_case for multi-word names."""
    print("=== Rule 1: Meaningful Variable Names ===\n")

    # ✅ GOOD: Names describe what they hold
    operation = "+"
    first_number = 10
    second_number = 5
    result = first_number + second_number
    print(
        f"✅ Good names: operation={operation}, first_number={first_number}, second_number={second_number}"
    )
    print(f"   Result: {result}\n")

    # ❌ POOR: Single letters don't explain intent
    op = "+"
    a = 10
    b = 5
    res = a + b
    print(f"❌ Poor names: op={op}, a={a}, b={b}")
    print(f"   Result: {res}\n")


def demo_rule2_spaces_around_operators() -> None:
    """Rule 2: One space on each side of operators."""
    print("=== Rule 2: Spaces Around Operators ===\n")

    # ✅ GOOD: Spaces around =, +, -, *, /, ==, not, and, or
    x = 10
    y = 20
    is_valid = x < y and y > 0
    print(f"✅ Good spacing: x = {x}, y = {y}, is_valid = {is_valid}\n")

    # ❌ POOR: No spaces makes it hard to read
    # x=10          ← missing spaces around =
    # y=20
    # is_valid=x<y and y>0
    print("❌ Poor spacing: x=10, y=20, is_valid=x<y — hard to parse at a glance\n")


def demo_rule3_no_spaces_in_parens() -> None:
    """Rule 3: No space immediately after ( or before )."""
    print("=== Rule 3: No Spaces Inside Parentheses ===\n")

    # ✅ GOOD: No space after ( or before )
    result1 = float("123.45")
    print(f'✅ Good: float("123.45") = {result1}')
    print('✅ Good: input("Enter name: ") — no spaces inside parens\n')

    # ❌ POOR: Extra spaces inside parentheses
    # float( "123.45" )       ← awkward spaces inside parens
    # input( "Enter name: " ) ← same issue
    print('❌ Poor: float( "123.45" ) — spaces inside parentheses are incorrect\n')


def demo_rule4_space_after_commas() -> None:
    """Rule 4: One space after every comma."""
    print("=== Rule 4: Space After Commas ===\n")

    # ✅ GOOD: Space after every comma
    print("✅ Good: {'+', '-', '*', '/'} and (10, 20, 30)\n")

    # ❌ POOR: No space after commas
    # {"+","-","*","/"}   ← missing spaces after commas
    # (10,20,30)
    print("❌ Poor: {'+','-','*','/'} and (10,20,30) — hard to read\n")


def demo_rule5_comments_explain_why() -> None:
    """Rule 5: Comments explain WHY, not WHAT."""
    print("=== Rule 5: Comments Explain WHY, Not WHAT ===\n")

    # ❌ POOR: Comment describes the obvious (WHAT)
    # # check if second is zero
    # if second == 0:
    #     print("Cannot divide")
    print(
        "❌ Bad comment: '# check if second is zero' — we can see that from the code\n"
    )

    # ✅ GOOD: Comment explains the reason (WHY)
    second = 0
    # Why: division by zero is undefined in mathematics — guard before attempting operation
    if second == 0:
        print("✅ Good comment: explains WHY we check, not WHAT the code does\n")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_rule1_meaningful_names()
    demo_rule2_spaces_around_operators()
    demo_rule3_no_spaces_in_parens()
    demo_rule4_space_after_commas()
    demo_rule5_comments_explain_why()

    print("---")
    print("These 5 PEP 8 rules make your code readable and professional.")
    print("Apply them to every script you write!")
    return 0


raise SystemExit(main(sys.argv))
