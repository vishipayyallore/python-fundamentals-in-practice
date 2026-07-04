"""PEP 8 warm-up demo for Session 7."""

# Filename: src/L1/S7/04_pep8_style_refactor.py

import sys

HELP_TEXT = """04_pep8_style_refactor.py

Purpose
    Demonstrate readable naming, spacing, and comments through a short PEP 8
    refactor warm-up.

Usage
    python src/L1/S7/04_pep8_style_refactor.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=" * 60)
    print("PEP 8 WARM-UP: Readability Before Debugging")
    print("=" * 60)

    # 1) Naming: vague names vs clear names
    print("\n--- 1) Naming ---")
    raw_a = 22.4
    raw_b = 14.0
    raw_c = True

    station_temperature_c = 22.4
    station_wind_speed_kmh = 14.0
    station_is_online = True

    print(f"Vague set      : {raw_a}, {raw_b}, {raw_c}")
    print("Clear set      : " f"{station_temperature_c} C, " f"{station_wind_speed_kmh} km/h, " f"{station_is_online}")

    # 2) Spacing: operators, commas, brackets
    print("\n--- 2) Spacing ---")
    hourly_readings = [18.0, 20.5, 22.4, 21.1, 19.8]
    reading_total = sum(hourly_readings)
    reading_count = len(hourly_readings)
    reading_average = reading_total / reading_count

    print(f"Readings       : {hourly_readings}")
    print(f"Total          : {reading_total}")
    print(f"Average        : {reading_average:.2f}")

    # 3) Comments: explain why, not what
    print("\n--- 3) Comments ---")
    # We flag values that drift too far from average to mimic a simple QA check.
    allowed_drift = 1.0
    drift_outliers = [value for value in hourly_readings if abs(value - reading_average) > allowed_drift]

    if drift_outliers:
        print(f"Outliers       : {drift_outliers}")
    else:
        print("Outliers       : none")

    print("\n" + "=" * 60)
    print("Try this next: rename one variable and re-run.")
    print("Then break spacing intentionally and clean it again.")
    print("=" * 60)
    return 0


raise SystemExit(main(sys.argv))
