"""Session 7: print() sep and end for clearer debug output."""

# Filename: src/L1/S7/06_print_sep_end.py

import sys

HELP_TEXT = """06_print_sep_end.py

Purpose
    Use print(sep=...) and print(end=...) to format debug lines without extra noise.

Usage
    python src/L1/S7/06_print_sep_end.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 7: print sep and end ===\n")

    print("Default print adds a newline after each call:")
    print("alpha")
    print("beta")
    print()

    print("sep changes the separator between values on one line:")
    print("step", 1, "done", sep=" | ")
    print()

    print("end keeps the cursor on the same line:")
    print("loading", end=" ")
    print("still loading", end=" ")
    print("finished")
    print()

    tags = ["debug", "session7", "print"]
    print("Join debug tags on one line:")
    print(*tags, sep=", ")
    return 0


raise SystemExit(main(sys.argv))
