# Filename: src/L1/MP1/calculator_utils.py
# Mini Project 1: Shared helpers for calculator scripts


def is_valid_number_text(value):
    """Return True when text represents a simple signed integer or float.

    Args:
        value (str): Text entered by the learner.

    Returns:
        bool: True when the text is a valid number format; otherwise False.

    Valid examples: "10", "-3", "4.5"
    Invalid examples: "", ".", "1.2.3", "abc"
    """
    # Why: one validation rule keeps both calculator scripts consistent.
    normalized = value[1:] if value.startswith("-") else value
    return (
        normalized not in {"", "."}
        and normalized.count(".") <= 1
        and normalized.replace(".", "", 1).isdigit()
    )
