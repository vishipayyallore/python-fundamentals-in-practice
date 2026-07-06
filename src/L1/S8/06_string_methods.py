"""String methods — startswith() and endswith() with optional index bounds."""

# Filename: src/L1/S8/06_string_methods.py

import sys

HELP_TEXT = """06_string_methods.py

Purpose
    Demonstrate str.startswith() and str.endswith().  Both return a bool.
    An optional (start, end) pair narrows the search to a sub-window of the
    string.  Python indexes from 0; the end position is exclusive.

Usage
    python src/L1/S8/06_string_methods.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    url = "www.learnpython.dev"
    print(f"url = {url!r}\n")

    # Basic prefix and suffix checks
    print("startswith('www')      ->", url.startswith("www"))
    print("startswith('com')      ->", url.startswith("com"))
    print("endswith('.dev')       ->", url.endswith(".dev"))

    # Optional (start, end) bounds — indexes are 0-based, end is exclusive.
    # url[4:12] evaluates to "learnpyt"; does it start with "learn"?
    print("\n--- Optional index bounds (start inclusive, end exclusive) ---")
    print("startswith('learn', 4, 12) ->", url.startswith("learn", 4, 12))

    # url[4:15] evaluates to "learnpython"; does it end with "python"?
    print("endswith('python', 4, 15)   ->", url.endswith("python", 4, 15))

    print("\nTip: in the REPL, type  url.startswith(  then press Shift+Tab to read the docstring.")

    return 0


raise SystemExit(main(sys.argv))
