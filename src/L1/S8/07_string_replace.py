"""String replacement with str.replace(old, new, count)."""

# Filename: src/L1/S8/07_string_replace.py

import sys

HELP_TEXT = """07_string_replace.py

Purpose
    Demonstrate how str.replace() swaps one piece of text for another.
    The optional count argument limits how many replacements happen.

Usage
    python src/L1/S8/07_string_replace.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    coded_name = "j-o-s-e-p-h"
    print(f"coded_name = {coded_name!r}")
    print("replace('-', '') preview ->", repr(coded_name.replace("-", "")))

    cleaned_name = coded_name.replace("-", "")
    print("cleaned_name             ->", repr(cleaned_name))

    school_code = "h-ar-v-a-r-d"
    print(f"\nschool_code = {school_code!r}")
    print("replace('-', '', 2)      ->", repr(school_code.replace("-", "", 2)))
    print("replace('-', '')         ->", repr(school_code.replace("-", "")))

    sentence = "Lists are useful. Lists are flexible."
    print(f"\nsentence = {sentence!r}")
    print(
        "replace('Lists', 'Strings', 1) ->",
        repr(sentence.replace("Lists", "Strings", 1)),
    )

    return 0


raise SystemExit(main(sys.argv))
