"""Session 7: PEP 8 — Indentation and multi-line argument wrapping.

Teaching arc:
  1. The 4-space rule — every nested block indents by exactly 4 spaces
  2. Long function calls — wrap arguments starting on the line BELOW
     the opening bracket, not on the same line as it
  3. Long expressions — use implicit line continuation inside brackets
     instead of the backslash continuation style

"""

# Filename: src/L1/S7/05_pep8_indentation.py
# Session 7: Debugging & Built-ins

import sys

HELP_TEXT = """05_pep8_indentation.py

Purpose
    Demonstrate PEP 8 indentation rules: 4-space nested blocks and
    correct multi-line wrapping of function calls and expressions.

Usage
    python src/L1/S7/05_pep8_indentation.py
"""


# ---------------------------------------------------------------------------
# Helper — used to demonstrate multi-line call wrapping
# ---------------------------------------------------------------------------


def format_reading(station_id, temperature_celsius, humidity_percent, wind_speed_kmh):
    """Return a one-line summary of a weather-station reading."""
    return f"[{station_id}]  " f"{temperature_celsius} C  |  " f"{humidity_percent}% RH  |  " f"{wind_speed_kmh} km/h"


# ---------------------------------------------------------------------------
# Section 1 — The 4-space indent rule
# ---------------------------------------------------------------------------


def demo_four_space_indent() -> None:
    """Show how each nested block indents by exactly 4 spaces."""

    print("=== 1. Four-Space Indentation ===\n")

    readings = [17.2, 18.0, 22.4, 21.1, 19.8]
    threshold = 21.0

    # Each if/for body is one indent level (4 spaces) deeper than its header.
    for reading in readings:
        if reading > threshold:
            # Two levels deep: 8 spaces from the left edge of the function body.
            print(f"  Above threshold: {reading} C")

    print()
    print("👉 Use exactly 4 spaces — never 2, never 8, never a mix of tabs.")
    print("   Most editors insert 4 spaces automatically when you press Tab.")


# ---------------------------------------------------------------------------
# Section 2 — Multi-line argument wrapping
# ---------------------------------------------------------------------------


def demo_multiline_call() -> None:
    """Show the correct way to wrap a long function call across lines."""

    print("\n=== 2. Multi-Line Argument Wrapping ===\n")

    # ✅ GOOD: opening bracket at end of the call line; each argument on its
    #          own line with one extra indent level; closing bracket on a new line.
    summary = format_reading(
        station_id="WS-07",
        temperature_celsius=22.4,
        humidity_percent=61,
        wind_speed_kmh=14.0,
    )
    print(summary)

    print()
    print("👉 Start arguments on the NEXT line after the opening bracket.")
    print("   Indent them one level (4 spaces) further than the call itself.")
    print("   A trailing comma after the last argument makes future edits easier.")


# ---------------------------------------------------------------------------
# Section 3 — Long expressions inside brackets
# ---------------------------------------------------------------------------


def demo_long_expressions() -> None:
    """Show how to split a long expression using implicit continuation."""

    print("\n=== 3. Long Expressions — Implicit Continuation ===\n")

    hourly_temps = [17.2, 18.0, 19.5, 21.3, 22.4, 21.8, 20.1, 18.6]

    # ✅ GOOD: wrap inside parentheses — Python joins lines automatically.
    mean_temp = sum(hourly_temps) / len(hourly_temps)

    # ✅ GOOD: long condition split across lines for readability.
    high_alert = mean_temp > 20.0 and max(hourly_temps) > 22.0

    print(f"Mean temperature : {mean_temp:.2f} C")
    print(f"High-alert flag  : {high_alert}")

    print()
    print("👉 Prefer implicit continuation (wrapping inside brackets) over")
    print("   the backslash style — brackets are cleaner and more reliable.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_four_space_indent()
    demo_multiline_call()
    demo_long_expressions()
    return 0


raise SystemExit(main(sys.argv))
