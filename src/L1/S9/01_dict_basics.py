"""Session 9: dictionary creation, access, update, and deletion."""

# Filename: src/L1/S9/01_dict_basics.py

import sys

HELP_TEXT = """01_dict_basics.py

Purpose
    Create dicts, read/update values, and remove keys safely.

Usage
    python src/L1/S9/01_dict_basics.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 9: Dictionary basics ===\n")

    student = {"name": "Riya", "grade": "B", "score": 86}
    print(f"student = {student}")
    print(f"student['name'] -> {student['name']}")

    student["score"] = 91
    student["grade"] = "A"
    print(f"after updates: {student}")

    removed = student.pop("grade")
    print(f"pop('grade') removed {removed!r} -> {student}")

    # Why: .get() avoids KeyError when a key might be missing.
    city = student.get("city", "unknown")
    print(f"student.get('city', 'unknown') -> {city!r}")
    return 0


raise SystemExit(main(sys.argv))
