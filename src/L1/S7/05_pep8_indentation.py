"""Session 7: PEP 8 indentation and simple multi-line wrapping."""

# Filename: src/L1/S7/05_pep8_indentation.py

import sys

HELP_TEXT = """05_pep8_indentation.py

Purpose
    Show consistent 4-space indentation and a readable multi-line condition.

Usage
    python src/L1/S7/05_pep8_indentation.py
"""


def classify_score(score: int) -> str:
    """Return a short label for a numeric score."""
    # Why break across lines: long conditions are easier to read when split.
    if (
        score >= 90
        and score <= 100
    ):
        return "excellent"
    if score >= 75:
        return "pass"
    return "review"


def nested_block_demo(count: int) -> None:
    """Indentation shows which lines belong to which block."""
    print(f"count starts at {count}")
    if count > 0:
        print("  inside if: count is positive")
        while count > 0:
            print(f"    inside while: {count}")
            count -= 1
    print(f"count ends at {count}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: PEP 8 indentation ===\n")

    for sample in (95, 80, 55):
        label = classify_score(sample)
        print(f"score {sample} -> {label}")

    print()
    nested_block_demo(3)
    print("\nRule of thumb: every new block indents 4 more spaces.")
    return 0


raise SystemExit(main(sys.argv))
