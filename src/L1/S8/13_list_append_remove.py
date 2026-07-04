"""Session 8 optional: focused append() and remove() drills."""

# Filename: src/L1/S8/13_list_append_remove.py

import sys

HELP_TEXT = """13_list_append_remove.py

Purpose
    Inspect list methods, then practice append() and remove().

Usage
    python src/L1/S8/13_list_append_remove.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: append & remove ===\n")

    items = ["pen", "notebook"]
    print(f"start: {items}")
    items.append("eraser")
    print(f"after append('eraser'): {items}")
    items.remove("pen")
    print(f"after remove('pen'): {items}")
    return 0


raise SystemExit(main(sys.argv))
