"""Session 8: common list methods — append, remove, insert, pop, sort."""

# Filename: src/L1/S8/02_list_methods.py

import sys

HELP_TEXT = """02_list_methods.py

Purpose
    Practice append(), remove(), insert(), pop(), sort(), and reverse().

Usage
    python src/L1/S8/02_list_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8: List methods ===\n")

    tasks = ["read notes", "run examples"]
    print(f"start: {tasks}")

    tasks.append("write summary")
    print(f"after append: {tasks}")

    tasks.insert(1, "watch replay")
    print(f"after insert at 1: {tasks}")

    removed = tasks.pop()
    print(f"pop() removed {removed!r} -> {tasks}")

    tasks.remove("read notes")
    print(f"after remove('read notes'): {tasks}\n")

    scores = [88, 92, 75, 91]
    print(f"unsorted scores: {scores}")
    scores.sort()
    print(f"after sort(): {scores}")
    scores.reverse()
    print(f"after reverse(): {scores}")
    return 0


raise SystemExit(main(sys.argv))
