import json
import os
from datetime import date, timedelta

FILE_NAME = "habits.json"


def load_habits():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not load saved habits.")
        return []


def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)


def add_habit(habits):
    name = input("Enter habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    for habit in habits:
        if habit["name"].lower() == name.lower():
            print("This habit already exists.")
            return

    habit = {
        "id": max((h["id"] for h in habits), default=0) + 1,
        "name": name,
        "completed_dates": []
    }

    habits.append(habit)
    save_habits(habits)
    print("Habit added successfully!")


def view_habits(habits):
    print("\n========== YOUR HABITS ==========")

    if not habits:
        print("No habits added yet.")
        return

    today = date.today().isoformat()

    for habit in habits:
        status = (
            "Completed today"
            if today in habit["completed_dates"]
            else "Pending today"
        )

        print(
            f"ID: {habit['id']} | "
            f"{habit['name']} | {status}"
        )


def complete_habit(habits):
    view_habits(habits)

    try:
        habit_id = int(input("\nEnter habit ID: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for habit in habits:
        if habit["id"] == habit_id:
            today = date.today().isoformat()

            if today in habit["completed_dates"]:
                print("Already completed today!")
                return

            habit["completed_dates"].append(today)
            save_habits(habits)
            print("Great! Habit completed for today.")
            return

    print("Habit not found.")


def calculate_streak(habit):
    completed = set(habit["completed_dates"])
    current_day = date.today()

    # If today's habit is still pending, check from yesterday.
    if current_day.isoformat() not in completed:
        current_day -= timedelta(days=1)

    streak = 0

    while current_day.isoformat() in completed:
        streak += 1
        current_day -= timedelta(days=1)

    return streak


def show_progress(habits):
    if not habits:
        print("Add a habit to see your progress.")
        return

    today = date.today()
    start_day = today - timedelta(days=6)

    print("\n========== WEEKLY PROGRESS ==========")

    for habit in habits:
        completed_dates = set(habit["completed_dates"])
        completed_count = 0

        for day_offset in range(7):
            current_day = start_day + timedelta(days=day_offset)

            if current_day.isoformat() in completed_dates:
                completed_count += 1

        percentage = completed_count / 7 * 100

        print(f"\nHabit: {habit['name']}")
        print(f"Completed days: {completed_count}/7")
        print(f"Weekly completion: {percentage:.1f}%")
        print(f"Current streak: {calculate_streak(habit)} day(s)")


def delete_habit(habits):
    view_habits(habits)

    try:
        habit_id = int(input("\nEnter habit ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for habit in habits:
        if habit["id"] == habit_id:
            habits.remove(habit)
            save_habits(habits)
            print("Habit deleted successfully.")
            return

    print("Habit not found.")


def main():
    habits = load_habits()

    while True:
        print("\n====== SMART HABIT TRACKER ======")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Habit Complete")
        print("4. Weekly Progress")
        print("5. Delete Habit")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            complete_habit(habits)
        elif choice == "4":
            show_progress(habits)
        elif choice == "5":
            delete_habit(habits)
        elif choice == "6":
            print("Keep building good habits!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
