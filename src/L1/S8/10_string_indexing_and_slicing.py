"""String indexing and slicing — positive, negative, and stepped access."""

# Filename: src/L1/S8/10_string_indexing_and_slicing.py

import sys

HELP_TEXT = """10_string_indexing_and_slicing.py

Purpose
    Demonstrate how strings behave like sequences: index access, negative
    indexes, basic slices, and step slices.

Usage
    python src/L1/S8/10_string_indexing_and_slicing.py
"""


def show_slice(label: str, text: str, start: int | None, stop: int | None, step: int | None = None) -> None:
    print(f"{label:<28} -> {text[start:stop:step]!r}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    topic = "sequence"
    print(f"topic = {topic!r}\n")

    print("=== Indexing ===")
    print(f"topic[0]    -> {topic[0]!r}")
    print(f"topic[3]    -> {topic[3]!r}")
    print(f"topic[-1]   -> {topic[-1]!r}")
    print(f"topic[-2]   -> {topic[-2]!r}")

    print("\n=== Basic slicing ===")
    show_slice("topic[1:5]", topic, 1, 5)
    show_slice("topic[:4]", topic, None, 4)
    show_slice("topic[4:]", topic, 4, None)
    show_slice("topic[-4:]", topic, -4, None)

    print("\n=== Step slicing ===")
    show_slice("topic[::2]", topic, None, None, 2)
    show_slice("topic[1::2]", topic, 1, None, 2)
    show_slice("topic[::-1]", topic, None, None, -1)

    print("\nRemember:")
    print("- Strings are immutable, so slicing creates a new string.")
    print("- The stop index is exclusive.")
    print("- Negative step values move from right to left.")

    return 0


raise SystemExit(main(sys.argv))
