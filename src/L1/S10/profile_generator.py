"""Mini Project 2: interactive personal profile generator."""

# Filename: src/L1/S10/profile_generator.py

import sys

HELP_TEXT = """profile_generator.py

Purpose
    Collect profile fields, store multiple profiles, display formatted output.

Usage
    python src/L1/S10/profile_generator.py
"""


def is_valid_age_text(text: str) -> bool:
    """Return True when text is a non-negative integer string."""
    return text.isdigit()


def parse_hobbies(raw: str) -> list[str]:
    """Split comma-separated hobby text into a clean list."""
    if not raw.strip():
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def format_profile(profile: dict[str, object]) -> str:
    hobbies = profile.get("hobbies", [])
    hobby_text = ", ".join(hobbies) if hobbies else "(none)"
    return (
        f"Name: {profile['name']}\n"
        f"Age: {profile['age']}\n"
        f"Hobbies: {hobby_text}\n"
        f"Goal: {profile['goal']}"
    )


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Mini Project 2: Personal Profile Generator ===")
    print("Commands: new, list, show <n>, quit\n")

    profiles: list[dict[str, object]] = []

    while True:
        command = input("profile> ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break

        if command == "list":
            if not profiles:
                print("  (no profiles yet)")
            for index, profile in enumerate(profiles, start=1):
                print(f"  {index}. {profile['name']}")
            continue

        if command == "new":
            name = input("  name: ").strip()
            if not name:
                print("  name cannot be empty")
                continue

            age_text = input("  age: ").strip()
            if not is_valid_age_text(age_text):
                print("  age must be a whole number like 25")
                continue

            hobbies_raw = input("  hobbies (comma-separated): ")
            goal = input("  goal: ").strip()
            if not goal:
                print("  goal cannot be empty")
                continue

            profile = {
                "name": name,
                "age": int(age_text),
                "hobbies": parse_hobbies(hobbies_raw),
                "goal": goal,
            }
            profiles.append(profile)
            print("  profile saved.\n")
            print(format_profile(profile))
            print()
            continue

        if command.startswith("show "):
            try:
                number = int(command.split(maxsplit=1)[1])
            except (IndexError, ValueError):
                print("  usage: show <number>")
                continue
            if 1 <= number <= len(profiles):
                print()
                print(format_profile(profiles[number - 1]))
                print()
            else:
                print("  invalid profile number")
            continue

        print("  unknown command — try new, list, show <n>, quit")
    return 0


raise SystemExit(main(sys.argv))
