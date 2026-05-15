# Filename: src/L1/S6/09_non_bool_values.py
"""Non-bool values with boolean operators: truthy/falsy and short-circuit evaluation."""

import sys

HELP_TEXT = """09_non_bool_values.py

Purpose
    Show how Python handles non-bool values (int, str, list, etc.) when used
    with and, or, and not — and introduce the falsy values list.

Usage
    python src/L1/S6/09_non_bool_values.py
"""


def demo_not_returns_bool() -> None:
    print("=== 1) not always returns a Boolean result ===")
    print(f"  not 1    -> {not 1}   (1 is truthy, so not 1 is False)")
    print(f"  not 0    -> {not 0}    (0 is falsy,  so not 0 is True)")
    print(f"  not 'hi' -> {not 'hi'}   (non-empty string is truthy)")
    print(f"  not ''   -> {not ''}    (empty string is falsy)")
    print("  Unlike and/or, not always returns True or False.")


def demo_and_or_return_actual_value() -> None:
    print("\n=== 2) and / or return the actual value, not always True/False ===")
    print("  Rule: Python evaluates left-to-right and stops as soon as it")
    print("  has enough information (short-circuit).")

    print()
    print("  -- and returns the first falsy value, or the last value if all truthy --")
    print(f"  1 and 0             -> {repr(1 and 0):<10}  (0 is falsy; stops there)")
    print(f"  1 and 'loop'        -> {repr(1 and 'loop'):<10}  (all truthy; returns last)")
    print(f"  1 and 'loop' and 'list' -> {repr(1 and 'loop' and 'list'):<10}  (all truthy; returns last)")

    print()
    print("  -- or returns the first truthy value, or the last value if all falsy --")
    print(f"  0 or 'found'        -> {repr(0 or 'found'):<10}  (0 falsy; keeps looking)")
    print(f"  'yes' or 'no'       -> {repr('yes' or 'no'):<10}  ('yes' truthy; stops there)")
    print(f"  0 or '' or 'last'   -> {repr(0 or '' or 'last'):<10}  (first two falsy; returns last)")


def demo_and_first_falsy_wins() -> None:
    print("\n=== 3) and - first falsy value is returned ===")
    # All three are evaluated left-to-right; empty string '' is first falsy
    result = "" and "loop" and "list" and []
    print(f'  "" and "loop" and "list" and []')
    print(f"  -> {repr(result)}")
    print("  ('' is falsy; Python stops immediately and returns '')")
    print("  (does NOT reach 'loop', 'list', or [])")


def demo_falsy_values() -> None:
    print("\n=== 4) Falsy values in Python ===")
    print("  These are ALL the values Python treats as False in a boolean context:\n")
    falsy_candidates = [None, 0, 0.0, 0j, "", [], (), {}]
    for val in falsy_candidates:
        print(f"  bool({repr(val):<8}) -> {bool(val)}")
    print()
    print("  Everything else is truthy: non-zero numbers, non-empty strings,")
    print("  non-empty lists, non-empty dicts, most objects.")


def demo_practical_idioms() -> None:
    print("\n=== 5) Practical short-circuit idioms ===")

    # Default value pattern
    user_input = ""
    name = user_input or "Guest"
    print(f'  user_input = ""')
    print(f'  name = user_input or "Guest"  -> {repr(name)}')

    # Guard before accessing
    items = []
    first = items and items[0]
    print(f"\n  items = []")
    print(f"  first = items and items[0]    -> {repr(first)}")
    print("  (empty list is falsy; short-circuit avoids IndexError)")

    items = ["apple", "banana"]
    first = items and items[0]
    print(f"\n  items = ['apple', 'banana']")
    print(f"  first = items and items[0]    -> {repr(first)}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_not_returns_bool()
    demo_and_or_return_actual_value()
    demo_and_first_falsy_wins()
    demo_falsy_values()
    demo_practical_idioms()

    print("\n=== Done ===")
    print("Experiment: predict the output of each expression before running.")
    return 0


raise SystemExit(main(sys.argv))
