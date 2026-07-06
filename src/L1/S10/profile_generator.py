# Filename: src/L1/S10/profile_generator.py

"""
👤 Personal Profile Generator
Level 1 Capstone Project - Phase B

A complete application demonstrating:
- Dictionaries for structured data
- Lists for collections
- Input validation
- Menu-driven interface
"""

# Store all profiles in a list
profiles = []


def collect_list_items(prompt, item_name):
    """Collect multiple items from user until they type 'done'."""
    print(f"\n{prompt} (type 'done' when finished):")
    items = []
    while True:
        item = input(f"  {item_name}: ").strip()
        if item.lower() == "done":
            break
        if item:
            items.append(item)

    if not items:
        items = ["Not specified"]
    return items


def create_profile():
    """Collect user information and create a new profile."""
    print("\n" + "=" * 50)
    print("📝 CREATE NEW PROFILE")
    print("=" * 50)

    # Collect name
    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return None

    # Check if name already exists
    for p in profiles:
        if p["name"].lower() == name.lower():
            print(f"⚠️ Profile for '{name}' already exists!")
            return None

    # Collect age with validation
    while True:
        try:
            age = int(input("Enter age (1-150): "))
            if 1 <= age <= 150:
                break
            else:
                print("❌ Age must be between 1 and 150!")
        except ValueError:
            print("❌ Please enter a valid number!")

    # Collect city
    city = input("Enter city: ").strip()
    if not city:
        city = "Not specified"

    # Collect hobbies
    hobbies = collect_list_items("Enter hobbies", "Hobby")

    # Collect goals
    goals = collect_list_items("Enter goals", "Goal")

    # Create profile dictionary
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "hobbies": hobbies,
        "goals": goals,
    }

    return profile


def display_profile(profile):
    """Display a single profile as a formatted card."""
    print("\n" + "╔" + "═" * 48 + "╗")
    print(f"║{'👤 PROFILE CARD':^48}║")
    print("╠" + "═" * 48 + "╣")
    print(f"║ Name:    {profile['name']:<38}║")
    print(f"║ Age:     {profile['age']:<38}║")
    print(f"║ City:    {profile['city']:<38}║")
    print("╠" + "═" * 48 + "╣")
    print(f"║{'🎨 Hobbies':^48}║")
    if profile["hobbies"] and profile["hobbies"] != ["Not specified"]:
        for hobby in profile["hobbies"]:
            # Truncate long hobbies
            display_hobby = hobby[:40] if len(hobby) > 40 else hobby
            print(f"║   • {display_hobby:<42}║")
    else:
        print(f"║   {'(No hobbies listed)':<43}║")
    print("╠" + "═" * 48 + "╣")
    print(f"║{'🎯 Goals':^48}║")
    if profile["goals"] and profile["goals"] != ["Not specified"]:
        for goal in profile["goals"]:
            # Truncate long goals
            display_goal = goal[:40] if len(goal) > 40 else goal
            print(f"║   • {display_goal:<42}║")
    else:
        print(f"║   {'(No goals listed)':<43}║")
    print("╚" + "═" * 48 + "╝")


def view_all_profiles():
    """Display summary of all profiles."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    print(f"\n📋 All Profiles ({len(profiles)} total):")
    print("-" * 50)
    print(f"{'#':<4} {'Name':<20} {'Age':>5}  {'City':<18}")
    print("-" * 50)
    for i, p in enumerate(profiles, 1):
        print(f"{i:<4} {p['name']:<20} {p['age']:>5}  {p['city']:<18}")
    print("-" * 50)


def view_single_profile():
    """View a single profile in detail."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    print("\n📋 Available Profiles:")
    for i, p in enumerate(profiles, 1):
        print(f"  {i}. {p['name']}")

    try:
        num = int(input("\nEnter profile number: "))
        if 1 <= num <= len(profiles):
            display_profile(profiles[num - 1])
        else:
            print("❌ Invalid profile number!")
    except ValueError:
        print("❌ Please enter a number!")


def search_profiles():
    """Search profiles by name."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    search = input("Enter name to search: ").strip().lower()
    if not search:
        print("❌ Please enter a search term!")
        return

    found = []
    for p in profiles:
        if search in p["name"].lower():
            found.append(p)

    if found:
        print(f"\n🔍 Found {len(found)} profile(s):")
        for p in found:
            display_profile(p)
    else:
        print(f"❌ No profiles found matching '{search}'")


def edit_profile():
    """Edit an existing profile."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    print("\n📋 Available Profiles:")
    for i, p in enumerate(profiles, 1):
        print(f"  {i}. {p['name']}")

    try:
        num = int(input("\nEnter profile number to edit: "))
        if 1 <= num <= len(profiles):
            profile = profiles[num - 1]
            print(f"\n✏️ Editing: {profile['name']}")
            print("(Press Enter to keep current value)\n")

            # Edit name
            new_name = input(f"Name [{profile['name']}]: ").strip()
            if new_name:
                profile["name"] = new_name

            # Edit age
            new_age = input(f"Age [{profile['age']}]: ").strip()
            if new_age:
                try:
                    age = int(new_age)
                    if 1 <= age <= 150:
                        profile["age"] = age
                    else:
                        print("Invalid age range, keeping current value")
                except ValueError:
                    print("Invalid age, keeping current value")

            # Edit city
            new_city = input(f"City [{profile['city']}]: ").strip()
            if new_city:
                profile["city"] = new_city

            # Option to edit hobbies
            edit_hobbies = input("Edit hobbies? (y/n): ").strip().lower()
            if edit_hobbies == "y":
                profile["hobbies"] = collect_list_items("Enter new hobbies", "Hobby")

            # Option to edit goals
            edit_goals = input("Edit goals? (y/n): ").strip().lower()
            if edit_goals == "y":
                profile["goals"] = collect_list_items("Enter new goals", "Goal")

            print("✅ Profile updated!")
            display_profile(profile)
        else:
            print("❌ Invalid profile number!")
    except ValueError:
        print("❌ Please enter a number!")


def delete_profile():
    """Delete a profile."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    print("\n📋 Available Profiles:")
    for i, p in enumerate(profiles, 1):
        print(f"  {i}. {p['name']}")

    try:
        num = int(input("\nEnter profile number to delete: "))
        if 1 <= num <= len(profiles):
            profile = profiles[num - 1]
            confirm = input(f"Delete '{profile['name']}'? (y/n): ").strip().lower()
            if confirm == "y":
                removed = profiles.pop(num - 1)
                print(f"🗑️ Deleted profile: {removed['name']}")
            else:
                print("Deletion cancelled.")
        else:
            print("❌ Invalid profile number!")
    except ValueError:
        print("❌ Please enter a number!")


def show_statistics():
    """Display statistics about all profiles."""
    if not profiles:
        print("📭 No profiles yet!")
        return

    print("\n" + "=" * 50)
    print("📊 PROFILE STATISTICS")
    print("=" * 50)

    # Count
    print(f"\n👥 Total profiles: {len(profiles)}")

    # Average age
    total_age = sum(p["age"] for p in profiles)
    avg_age = total_age / len(profiles)
    print(f"📅 Average age: {avg_age:.1f}")

    # Youngest and oldest
    youngest = min(profiles, key=lambda p: p["age"])
    oldest = max(profiles, key=lambda p: p["age"])
    print(f"👶 Youngest: {youngest['name']} ({youngest['age']})")
    print(f"👴 Oldest: {oldest['name']} ({oldest['age']})")

    # Cities
    cities = {}
    for p in profiles:
        city = p["city"]
        cities[city] = cities.get(city, 0) + 1

    print("\n🏙️ Profiles by city:")
    for city, count in sorted(cities.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * count
        print(f"  {city:<20} {bar} ({count})")

    # Most common hobbies
    all_hobbies = {}
    for p in profiles:
        for hobby in p["hobbies"]:
            if hobby != "Not specified":
                all_hobbies[hobby] = all_hobbies.get(hobby, 0) + 1

    if all_hobbies:
        print("\n🎨 Top 5 hobbies:")
        sorted_hobbies = sorted(all_hobbies.items(), key=lambda x: x[1], reverse=True)[:5]
        for hobby, count in sorted_hobbies:
            print(f"  • {hobby}: {count}")

    # Most common goals
    all_goals = {}
    for p in profiles:
        for goal in p["goals"]:
            if goal != "Not specified":
                all_goals[goal] = all_goals.get(goal, 0) + 1

    if all_goals:
        print("\n🎯 Top 5 goals:")
        sorted_goals = sorted(all_goals.items(), key=lambda x: x[1], reverse=True)[:5]
        for goal, count in sorted_goals:
            print(f"  • {goal}: {count}")

    print("\n" + "=" * 50)


def add_sample_profiles():
    """Add sample profiles for testing."""
    sample_profiles = [
        {
            "name": "Alice Johnson",
            "age": 28,
            "city": "New York",
            "hobbies": ["Reading", "Hiking", "Photography"],
            "goals": ["Learn Python", "Travel to Japan"],
        },
        {
            "name": "Bob Smith",
            "age": 35,
            "city": "San Francisco",
            "hobbies": ["Gaming", "Cooking", "Music"],
            "goals": ["Start a business", "Run a marathon"],
        },
        {
            "name": "Carol Davis",
            "age": 24,
            "city": "Boston",
            "hobbies": ["Painting", "Yoga", "Reading"],
            "goals": ["Get a promotion", "Learn Spanish"],
        },
        {
            "name": "David Lee",
            "age": 42,
            "city": "New York",
            "hobbies": ["Golf", "Photography", "Cooking"],
            "goals": ["Retire early", "Write a book"],
        },
    ]

    profiles.extend(sample_profiles)
    print(f"✅ Added {len(sample_profiles)} sample profiles!")


def main():
    """Main application loop."""
    print("\n" + "=" * 60)
    print("👤 PERSONAL PROFILE GENERATOR")
    print("    Level 1 Capstone Project - Phase B")
    print("=" * 60)

    while True:
        print("\n" + "-" * 40)
        print("           📋 MAIN MENU")
        print("-" * 40)
        print("  1. Create new profile")
        print("  2. View all profiles")
        print("  3. View single profile")
        print("  4. Search profiles")
        print("  5. Edit profile")
        print("  6. Delete profile")
        print("  7. Profile statistics")
        print("  8. Add sample profiles")
        print("  9. Quit")
        print("-" * 40)

        choice = input("\nEnter choice (1-9): ").strip()

        if choice == "1":
            profile = create_profile()
            if profile:
                profiles.append(profile)
                print(f"\n✅ Profile created for {profile['name']}!")
                display_profile(profile)

        elif choice == "2":
            view_all_profiles()

        elif choice == "3":
            view_single_profile()

        elif choice == "4":
            search_profiles()

        elif choice == "5":
            edit_profile()

        elif choice == "6":
            delete_profile()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            add_sample_profiles()

        elif choice == "9":
            print("\n" + "=" * 60)
            print("👋 Thanks for using Profile Generator!")
            print("   Keep building amazing Python projects!")
            print("=" * 60)
            break

        else:
            print("❌ Invalid choice! Please enter 1-9.")


# Run the application
if __name__ == "__main__":
    main()
