# Filename: src/L1/S6/08_boolean_logic_precedence.py
"""Compound conditions for loops: and, or, not, and evaluation order.

Pairs with Session 6 while-loops: messy headers are a common source of
"why does my loop never run?" bugs. Use parentheses when in doubt.
"""

import sys

HELP_TEXT = """08_boolean_logic_precedence.py

Purpose
    Demonstrate how Python evaluates compound boolean conditions:
    operator precedence (not -> and -> or), parentheses override,
    and compound while-loop conditions.

Usage
    python src/L1/S6/08_boolean_logic_precedence.py
"""


def demo_truth_tables() -> None:
    print("=== 1) Truth tables (quick reminders) ===")
    print(f"  True  and True   -> {True and True}")
    print(f"  True  and False  -> {True and False}")
    print(f"  False and True   -> {False and True}")
    print(f"  False and False  -> {False and False}")
    print()
    print(f"  True  or True    -> {True or True}")
    print(f"  True  or False   -> {True or False}")
    print(f"  False or True    -> {False or True}")
    print(f"  False or False   -> {False or False}")
    print()
    print(f"  not True   -> {not True}")
    print(f"  not False  -> {not False}")


def demo_precedence_simple() -> None:
    print("\n=== 2) Order without parentheses: not -> and -> or ===")
    # Same rule as arithmetic: use explicit () when readers might pause.
    expr = True and not False or False
    print("  True and not False or False")
    print("    parsed as: (True and (not False)) or False")
    print(f"    result: {expr}")

    explicit = (True and (not False)) or False
    print(f"  explicit form: {explicit}")


def demo_precedence_step_by_step() -> None:
    print("\n=== 3) Step-by-step: True and False or not False or False ===")
    # Step 1: resolve all 'not' first
    # not False -> True
    # expression becomes: True and False or True or False
    print("  Start:    True and False or not False or False")
    print("  Step 1 (not):  not False -> True")
    print("  After:    True and False or True or False")
    # Step 2: resolve all 'and'
    # True and False -> False
    # expression becomes: False or True or False
    print("  Step 2 (and):  True and False -> False")
    print("  After:    False or True or False")
    # Step 3: resolve 'or' left-to-right
    # False or True -> True
    # True or False -> True
    print("  Step 3 (or):   False or True -> True, then True or False -> True")
    result = True and False or not False or False
    print(f"  Final result: {result}")


def demo_parentheses_override() -> None:
    print("\n=== 4) Parentheses win - always ===")
    without = True or False and False  # and binds tighter -> True or False -> True
    with_parens = (True or False) and False  # parens first -> True and False -> False
    print(f"  True or False and False       -> {without}  (and binds first)")
    print(f"  (True or False) and False     -> {with_parens}  (parens override)")


def demo_compound_while() -> None:
    print("\n=== 5) Compound while condition ===")
    count = 0
    evens_printed = 0
    # Run while count is small AND we have not hit the cap on evens printed.
    while count < 8 and evens_printed < 3:
        if count % 2 == 0:
            print(f"  even: {count}")
            evens_printed += 1
        count += 1
    print("  Loop exited because one side of 'and' became false.")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_truth_tables()
    demo_precedence_simple()
    demo_precedence_step_by_step()
    demo_parentheses_override()
    demo_compound_while()
    print("\n=== Done ===")
    print("Experiment: wrap parts of a condition in () and predict the result before running.")
    return 0


raise SystemExit(main(sys.argv))
