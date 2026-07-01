"""Session 8 optional: insert() and pop() at specific positions."""

# Filename: src/L1/S8/14_list_insert_pop.py

import sys

HELP_TEXT = """14_list_insert_pop.py

Purpose
    Target list positions with insert() and pop().

Usage
    python src/L1/S8/14_list_insert_pop.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: insert & pop ===\n")

    queue = ["second", "third"]
    print(f"start: {queue}")
    queue.insert(0, "first")
    print(f"after insert(0, 'first'): {queue}")
    head = queue.pop(0)
    print(f"pop(0) -> {head!r}, remaining {queue}")
    return 0


raise SystemExit(main(sys.argv))
