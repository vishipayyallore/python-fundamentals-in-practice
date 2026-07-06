"""Session 8 reinforcement: inspect list methods, then append and remove items."""

# Filename: src/L1/S8/13_list_append_remove.py

import sys

HELP_TEXT = """13_list_append_remove.py

Purpose
    Reinforce how to inspect list capabilities with dir(), then use
    append() and remove() to change a list in place.

Usage
    python src/L1/S8/13_list_append_remove.py
"""


def show_public_list_methods() -> None:
    public_methods = []

    for method_name in dir(list):
        if not method_name.startswith("_"):
            public_methods.append(method_name)

    print("Public list methods learners should recognize:")
    print(public_methods)


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 Reinforcement: append() and remove() ===\n")
    show_public_list_methods()

    topic_scores = [10, 20, 30, 40, 50, 60]
    print(f"\nStart: {topic_scores}")

    topic_scores.append(70)
    print(f"After append(70): {topic_scores}")

    topic_scores.remove(70)
    print(f"After remove(70): {topic_scores}")
    return 0


raise SystemExit(main(sys.argv))
