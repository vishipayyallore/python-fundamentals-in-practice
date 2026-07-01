"""Session 9 capstone: gradebook with dictionaries and assert checks."""

# Filename: src/L1/S9/03_gradebook.py

import sys

HELP_TEXT = """03_gradebook.py

Purpose
    Store student scores in a dict and verify behavior with assert.

Usage
    python src/L1/S9/03_gradebook.py
"""


def average_score(scores: dict[str, int]) -> float:
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 9: Gradebook ===\n")

    gradebook = {"Ada": 92, "Lin": 88, "Sam": 95}
    print(f"gradebook = {gradebook}")

    mean = average_score(gradebook)
    print(f"class average: {mean:.1f}")

    # Why assert: quick self-check while learning — not a full test framework.
    assert average_score({"only": 100}) == 100.0
    assert average_score({}) == 0.0
    assert len(gradebook) == 3

    print("\nAll assert checks passed.")
    return 0


raise SystemExit(main(sys.argv))
