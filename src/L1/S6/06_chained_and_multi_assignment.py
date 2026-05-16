"""Session 2: Chained and multiple-target assignment.

Teaching arc:
  1. Chained assignment — give the same value to several names at once
  2. Multiple-target assignment (tuple unpacking) — give different values
     to different names in a single statement
  3. Variable swap — swap two values without a temporary variable

"""

# Filename: src/L1/S6/06_chained_and_multi_assignment.py

import sys

HELP_TEXT = """06_chained_and_multi_assignment.py

Purpose
    Demonstrate two compact assignment forms: chained assignment for
    a shared value and tuple unpacking for paired or swapped values.

Usage
    python src/L1/S6/06_chained_and_multi_assignment.py
"""


# ---------------------------------------------------------------------------
# Section 1 — Chained Assignment
# ---------------------------------------------------------------------------


def demo_chained_assignment() -> None:
    """Assign the same value to multiple names in one statement."""

    print("=== 1. Chained Assignment ===\n")

    # Standard delivery zones all share a 2-business-day lead time.
    # Reading right-to-left: 2 is stored in east, then central, south, north.
    north = south = central = east = 2
    print("Standard zones (days) - " f"North: {north}, South: {south}, Central: {central}, East: {east}")

    # Remote delivery zones share a 5-business-day lead time.
    highland = island = offshore = border = 5
    print(
        "Remote zones   (days) - " f"Highland: {highland}, Island: {island}, " f"Offshore: {offshore}, Border: {border}"
    )

    print()
    print("Note: Use chained assignment when several names share one starting value.")
    print("      Changing any name later does NOT change the others -- they just")
    print("      started equal; they are independent variables after assignment.")


# ---------------------------------------------------------------------------
# Section 2 — Multiple-Target Assignment (Tuple Unpacking)
# ---------------------------------------------------------------------------


def demo_multi_target_assignment() -> None:
    """Assign different values to different names in one statement."""

    print("\n=== 2. Multiple-Target Assignment (Tuple Unpacking) ===\n")

    # Pair a city with its nearest fulfilment hub in a single statement.
    city, hub = "Hyderabad", "Pune"
    print(f"City: {city!r},  Nearest hub: {hub!r}")

    # Unpack three related values at once — avoids three separate lines.
    product, category, price = "Laptop", "Electronics", 54999
    print(f"Product: {product!r},  Category: {category!r},  Price: Rs.{price}")

    print()
    print("Note: The number of names on the left must match the number of values")
    print("   on the right, or Python raises a ValueError.")


# ---------------------------------------------------------------------------
# Section 3 — Variable Swap (classic tuple-unpacking trick)
# ---------------------------------------------------------------------------


def demo_swap() -> None:
    """Swap two variables without a temporary holder."""

    print("\n=== 3. Variable Swap ===\n")

    warehouse_a = 120  # units in stock at warehouse A
    warehouse_b = 45  # units in stock at warehouse B

    print(f"Before swap: warehouse_a={warehouse_a}, warehouse_b={warehouse_b}")

    # Python evaluates the right side completely before assigning — no temp needed.
    warehouse_a, warehouse_b = warehouse_b, warehouse_a

    print(f"After swap : warehouse_a={warehouse_a}, warehouse_b={warehouse_b}")

    print()
    print("Note: This works because Python packs the right side into a tuple first,")
    print("   then unpacks it into the names on the left.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_chained_assignment()
    demo_multi_target_assignment()
    demo_swap()
    return 0


raise SystemExit(main(sys.argv))
