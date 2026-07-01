"""Session 8: list creation, indexing, slicing, and modification."""

# Filename: src/L1/S8/01_list_basics.py

import sys

HELP_TEXT = """01_list_basics.py

Purpose
    Create lists, access items by index, slice sub-ranges, and update elements.

Usage
    python src/L1/S8/01_list_basics.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8: List basics ===\n")

    cities = ["Hyderabad", "Pune", "Chennai"]
    print(f"cities = {cities}")
    print(f"first city (index 0): {cities[0]}")
    print(f"last city (index -1): {cities[-1]}\n")

    print(f"slice cities[1:3] -> {cities[1:3]}")
    cities[1] = "Bengaluru"
    print(f"after cities[1] = 'Bengaluru': {cities}\n")

    numbers = list(range(1, 6))
    print(f"numbers from range: {numbers}")
    print(f"length via len(): {len(numbers)}")
    return 0


raise SystemExit(main(sys.argv))
