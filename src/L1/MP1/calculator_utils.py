# Filename: src/L1/MP1/calculator_utils.py
# Mini Project 1: Shared helpers for calculator scripts


def is_valid_number_text(value):
    # Why: one validation rule keeps both calculator scripts consistent.
    normalized = value[1:] if value.startswith("-") else value
    return (
        normalized not in {"", "."}
        and normalized.count(".") <= 1
        and normalized.replace(".", "", 1).isdigit()
    )
