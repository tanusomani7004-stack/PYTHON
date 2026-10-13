import json
import os
from datetime import datetime

FILE_NAME = "lost_found.json"


def load_items():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not load saved data.")
        return []


def save_items(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def report_item(items):
    print("\n--- Report an Item ---")

    name = input("Item name: ").strip()
    category = input("Category: ").strip()
    location = input("Last seen / found location: ").strip()
    status = input("Type (lost/found): ").strip().lower()

    if not name or not category or not location:
        print("All fields are required.")
        return

    if status not in ["lost", "found"]:
        print("Please enter either 'lost' or 'found'.")
        return

    item_id = max((item["id"] for item in items), default=0) + 1

    item = {
        "id": item_id,
        "name": name,
        "category": category,
        "location": location,
        "status": status,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "claimed": False
    }

    items.append(item)
    save_items(items)

    print(f"Item reported successfully! Item ID: {item_id}")


def view_items(items):
    print("\n--- All Reports ---")

    if not items:
        print("No items reported yet.")
        return

    for item in items:
        print("-" * 35)
        print("ID:", item["id"])
        print("Item:", item["name"])
        print("Category:", item["category"])
        print("Location:", item["location"])
        print("Status:", item["status"].upper())
        print("Date:", item["date"])
        print("Claimed:", "Yes" if item["claimed"] else "No")


def search_items(items):
    keyword = input("Search by item name or category: ").strip().lower()

    matches = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["category"].lower()
    ]

    if not matches:
