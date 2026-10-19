import json
import os
from datetime import datetime

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        print("Unable to load notes.")
        return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(notes):
    print("\n--- Create a New Note ---")

    title = input("Title: ").strip()
    content = input("Content: ").strip()
    category = input("Category: ").strip()

    if not title or not content or not category:
        print("All fields are required.")
        return

    note_id = max(
        (note["id"] for note in notes),
        default=0
    ) + 1

    note = {
        "id": note_id,
        "title": title,
        "content": content,
        "category": category,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    notes.append(note)
    save_notes(notes)

    print(f"Note saved successfully! ID: {note_id}")


def view_notes(notes):
    print("\n--- All Notes ---")

    if not notes:
        print("No notes available.")
        return

    for note in notes:
        print("-" * 40)
        print("ID:", note["id"])
        print("Title:", note["title"])
        print("Category:", note["category"])
        print("Created:", note["created_at"])
        print("Content:", note["content"])


def search_notes(notes):
    keyword = input("Enter title or keyword: ").strip().lower()

    if not keyword:
        print("Please enter a search keyword.")
        return

    results = []

    for note in notes:
        if (
            keyword in note["title"].lower()
            or keyword in note["content"].lower()
            or keyword in note["category"].lower()
        ):
            results.append(note)

    if results:
        view_notes(results)
    else:
        print("No matching notes found.")


def edit_note(notes):
    try:
        note_id = int(input("Enter note ID to edit: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for note in notes:
        if note["id"] == note_id:
            print("Leave a field empty to keep its current value.")

            title = input(f"New title [{note['title']}]: ").strip()
            content = input("New content: ").strip()
            category = input(
                f"New category [{note['category']}]: "
            ).strip()

            if title:
                note["title"] = title

            if content:
                note["content"] = content

            if category:
                note["category"] = category

            save_notes(notes)
            print("Note updated successfully!")
            return

    print("Note ID not found.")


def delete_note(notes):
    try:
        note_id = int(input("Enter note ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for note in notes:
        if note["id"] == note_id:
            confirmation = input(
                f"Delete '{note['title']}'? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                notes.remove(note)
                save_notes(notes)
                print("Note deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Note ID not found.")


def show_categories(notes):
    print("\n--- Categories ---")

    categories = sorted({
        note["category"] for note in notes
    })

    if not categories:
        print("No categories available.")
        return

    for category in categories:
        count = sum(
            1 for note in notes
            if note["category"] == category
        )

        print(f"{category}: {count} note(s)")


def main():
    notes = load_notes()

    while True:
        print("\n========== NOTENEST ==========")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. View Categories")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            edit_note(notes)
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            show_categories(notes)
        elif choice == "7":
            print("Your notes are saved. See you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
