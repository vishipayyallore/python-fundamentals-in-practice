"""Session 8 optional: startswith() and endswith() with optional bounds."""

# Filename: src/L1/S8/06_string_methods.py

import sys

HELP_TEXT = """06_string_methods.py

Purpose
    Practice startswith() and endswith() for simple text checks.

Usage
    python src/L1/S8/06_string_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8 optional: String methods ===\n")

    filename = "report_2026.txt"
    print(f"filename = {filename!r}")
    print(f"startswith('report') -> {filename.startswith('report')}")
    print(f"endswith('.txt') -> {filename.endswith('.txt')}")
    print(f"startswith('repo', 0, 4) -> {filename.startswith('repo', 0, 4)}")
    return 0


raise SystemExit(main(sys.argv))
