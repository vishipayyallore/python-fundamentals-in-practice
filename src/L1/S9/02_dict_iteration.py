"""Session 9: iterate dictionaries with keys, values, and items."""

# Filename: src/L1/S9/02_dict_iteration.py

import sys

HELP_TEXT = """02_dict_iteration.py

Purpose
    Loop over .keys(), .values(), and .items() with readable output.

Usage
    python src/L1/S9/02_dict_iteration.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 9: Dictionary iteration ===\n")

    inventory = {"notebooks": 12, "pens": 40, "markers": 8}
    print(f"inventory = {inventory}\n")

    print("Keys:")
    for key in inventory.keys():
        print(f"  {key}")

    print("\nValues:")
    for value in inventory.values():
        print(f"  {value}")

    print("\nItems (key + value pairs):")
    for key, value in inventory.items():
        print(f"  {key}: {value}")
    return 0


raise SystemExit(main(sys.argv))
