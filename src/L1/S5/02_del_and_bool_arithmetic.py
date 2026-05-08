"""Session 2 Appendix — del, NameError, and bool in arithmetic.

What you practice here:
- Removing a variable with `del`
- Observing a NameError when accessing a deleted (or undefined) name
- Seeing how True and False behave as 1 and 0 in numeric expressions
"""

# Filename: src/L1/S5/02_del_and_bool_arithmetic.py

import sys

HELP_TEXT = """02_del_and_bool_arithmetic.py

Purpose
    Explore two extra concepts from Session 2:
    1. del removes a variable; any later access raises NameError.
    2. bool values (True / False) act as 1 / 0 in arithmetic.

Usage
    python src/L1/S5/02_del_and_bool_arithmetic.py
"""


def demo_del_and_name_error() -> None:
    """Show what happens when you delete a variable and then reference it."""
    season = "October"
    print("Before del:", season)  # → October

    del season
    # Uncommenting the next line causes NameError: name 'season' is not defined
    # print(season)
    print("'season' has been deleted — referencing it now would raise NameError.")


def demo_bool_arithmetic() -> None:
    """Show that True == 1 and False == 0 in numeric operations."""
    print("True * 7  =", True * 7)  # → 7
    print("False * 7 =", False * 7)  # → 0
    print("True + True =", True + True)  # → 2  (1 + 1)
    print("type(True) =", type(True))  # → <class 'bool'>

    # Practical note: bool is a subtype of int in Python
    print("isinstance(True, int):", isinstance(True, int))  # → True


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== del and NameError ===")
    demo_del_and_name_error()

    print()
    print("=== bool in arithmetic ===")
    demo_bool_arithmetic()

    return 0


raise SystemExit(main(sys.argv))
