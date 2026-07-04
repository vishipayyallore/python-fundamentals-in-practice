# Filename: src/L1/S9/01_dict_basics.py

print("=== Dictionary Basics Demo ===\n")

# Creating dictionaries
print("--- Creating Dictionaries ---")
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Bob", grade=95, subject="Math")
print(f"Student: {student}")

# Empty dictionary
empty = {}
print(f"Empty dict: {empty}")

# Accessing values
print("\n--- Accessing Values ---")
print(f"person['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('country') = {person.get('country')}")
print(f"person.get('country', 'USA') = {person.get('country', 'USA')}")

# Modifying values
print("\n--- Modifying Values ---")
person["age"] = 26
print(f"After person['age'] = 26: {person}")

person["country"] = "USA"
print(f"After adding 'country': {person}")

# Removing values
print("\n--- Removing Values ---")
removed = person.pop("city")
print(f"Removed 'city': {removed}")
print(f"After pop: {person}")

# Checking keys
print("\n--- Checking Keys ---")
print(f"'name' in person: {'name' in person}")
print(f"'city' in person: {'city' in person}")

# Dictionary with different value types
print("\n--- Mixed Value Types ---")
profile = {
    "name": "Charlie",
    "age": 30,
    "scores": [95, 87, 92],
    "active": True,
    "address": {"city": "Boston", "zip": "02101"},
}
print(f"Profile: {profile}")
print(f"First score: {profile['scores'][0]}")
print(f"City: {profile['address']['city']}")
