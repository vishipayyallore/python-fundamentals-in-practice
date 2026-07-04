"""String basics — quoting, type(), concatenation (+), repetition (*), TypeError."""

# Filename: src/L1/S8/04_string_basics.py

import sys

HELP_TEXT = """04_string_basics.py

Purpose
    Explore how Python stores and operates on string values: quoting rules,
    what type() reports, how + joins strings, how * repeats them, and which
    operations raise TypeError.

Usage
    python src/L1/S8/04_string_basics.py
"""


def _show_type_error(label: str, fn) -> None:
    print(f"\n--- {label} ---")
    try:
        fn()
    except TypeError as exc:
        print(f"TypeError (expected): {exc}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Quoting rules ===")
    # A bare word without quotes is a SyntaxError in code.
    # Prefixing a line with # turns it into a comment — Python skips it.
    # hello world  ← this comment is ignored at runtime

    print("\n=== type() on a number vs a quoted number ===")
    print("type(42)         ->", type(42))
    print('type("42")       ->', type("42"))

    print("\n=== Concatenation: + joins strings side by side ===")
    print('"hello" + "world"           ->', repr("hello" + "world"))
    print('"hello" + " " + "world"     ->', repr("hello" + " " + "world"))

    _show_type_error("Subtraction is not defined for strings", lambda: "hello" - "world")

    print("\n=== Repetition: * produces n copies side by side ===")
    print('"ha" * 3         ->', repr("ha" * 3))

    _show_type_error("str * str is not defined", lambda: "ha" * "ha")
    _show_type_error("str / int is not defined", lambda: "ha" / 3)

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
