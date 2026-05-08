"""Session 2: From raw values to variables.

Teaching arc:
  1. Raw literal values — Python evaluates them directly
  2. Arithmetic on those values — int and float behave differently
  3. type() — inspect any value or expression
  4. Why variables? — avoid rewriting the same value repeatedly
  5. Assignment, reassignment, and del

Promoted from: src/Working/Module1/02_sample.py (prior draft: sample1.py)
"""

# Filename: src/L1/S6/05_values_to_variables.py

import sys

HELP_TEXT = """05_values_to_variables.py

Purpose
    Walk through Python's four primary data types as raw values first,
    then show why variables are the natural next step.

Usage
    python src/L1/S6/05_values_to_variables.py
"""


def demo_raw_values() -> None:
    """Start with values before variables — the notebook way."""
    print("--- Integer and float literals ---")
    print(7)  # int
    print(5.9)  # float

    print("\n--- Arithmetic ---")
    print(7 * 7)  # 49   — stays int
    print(5.2 + 6.8)  # 12.0 — stays float (one float operand → float result)

    print("\n--- String literals ---")
    print("hello data science")  # double quotes
    print("hello data science")  # single quotes — same result

    print("\n--- Boolean in arithmetic ---")
    print(True * 7)  # 7  (True == 1)
    print(False * 7)  # 0  (False == 0)


def demo_type_function() -> None:
    """type() tells you the data type of any value or expression."""
    print("--- type() on values ---")
    print(type(5.9))  # <class 'float'>
    print(type(7))  # <class 'int'>
    print(type("hello data science"))  # <class 'str'>
    print(type(True))  # <class 'bool'>

    print("\n--- type() on an expression ---")
    print(type(5.2 + 6.8))  # <class 'float'>


def demo_variables() -> None:
    """Assign values to names so you don't retype them every time."""
    print("--- Assignment ---")
    a = "november"
    print(a)  # november

    b = 9
    c = 5.8
    d = True
    print(b, c, d)  # 9  5.8  True

    print("\n--- Reassignment (Python keeps the latest value) ---")
    a = "october"
    print(a)  # october — 'november' is gone

    print("\n--- del removes the variable; using it after raises NameError ---")
    a = "september"
    print(a)  # september
    del a
    # print(a)          # ← uncomment to see: NameError: name 'a' is not defined

    print("\n--- type() on variables ---")
    print(type(b))  # <class 'int'>
    print(type(c))  # <class 'float'>
    print(type(d))  # <class 'bool'>


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== 1. Raw values ===")
    demo_raw_values()
    print("\n=== 2. type() function ===")
    demo_type_function()
    print("\n=== 3. Variables ===")
    demo_variables()
    return 0


raise SystemExit(main(sys.argv))
