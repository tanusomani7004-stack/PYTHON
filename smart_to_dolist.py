import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task name: ").strip()

    if not task_name:
        print("Task name cannot be empty!")
        return

    task = {
        "id": len(tasks) + 1,
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(
            f'{task["id"]}. {task["name"]} - {status}'
        )


def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print("Task completed successfully!")
                return

        print("Task not found!")

    except ValueError:
        print("Please enter a valid ID!")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully!")
                return

        print("Task not found!")

    except ValueError:
        print("Please enter a valid ID!")


def show_pending(tasks):
    pending = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending:
        print("No pending tasks!")
        return

    print("\n========== PENDING TASKS ==========")

    for task in pending:
        print(f'{task["id"]}. {task["name"]}')


def main():
    tasks = load_tasks()

    while True:
        print("\n========== SMART TODO MANAGER ==========")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. View Pending Tasks")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            show_pending(tasks)

        elif choice == "6":
            print("Thank you for using Smart Todo Manager!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
