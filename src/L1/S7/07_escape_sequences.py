"""Session 7: escape sequences for structured debug and report output."""

# Filename: src/L1/S7/07_escape_sequences.py

import sys

HELP_TEXT = """07_escape_sequences.py

Purpose
    Practice \\n, \\t, and quote escaping when formatting multi-line debug text.

Usage
    python src/L1/S7/07_escape_sequences.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: Escape sequences ===\n")

    print("Newline \\n starts the next line:")
    print("line one\nline two\n")

    print("Tab \\t aligns columns in a simple report:")
    print("name\tscore")
    print("Ada\t92")
    print("Lin\t88")
    print()

    print("Quote inside a string:")
    print("She said, \"Read the traceback carefully.\"")
    print()

    print("Multi-line f-string for a debug snapshot:")
    name = "practice_run"
    status = "ok"
    detail = (
        f"--- debug ---\n"
        f"name: {name}\n"
        f"status: {status}\n"
        f"-------------"
    )
    print(detail)
    return 0


raise SystemExit(main(sys.argv))
