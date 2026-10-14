import json
import os
from datetime import datetime

FILE_NAME = "applications.json"

STATUSES = [
    "Applied",
    "Assessment",
    "Interview",
    "Selected",
    "Rejected"
]


def load_applications():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        print("Could not read saved applications.")
        return []


def save_applications(applications):
    with open(FILE_NAME, "w") as file:
        json.dump(applications, file, indent=4)


def add_application(applications):
    print("\n--- Add Application ---")

    company = input("Company name: ").strip()
    role = input("Job/Internship role: ").strip()
    link = input("Application link (optional): ").strip()

    if not company or not role:
        print("Company and role are required.")
        return

    application_id = max(
        (app["id"] for app in applications),
        default=0
    ) + 1

    application = {
        "id": application_id,
        "company": company,
        "role": role,
        "link": link,
        "status": "Applied",
        "applied_on": datetime.now().strftime("%Y-%m-%d"),
        "interview_date": ""
    }

    applications.append(application)
    save_applications(applications)

    print(f"Application added! ID: {application_id}")


def view_applications(applications):
    print("\n--- Your Applications ---")

    if not applications:
        print("No applications recorded.")
        return

    for app in applications:
        print("-" * 40)
        print("ID:", app["id"])
        print("Company:", app["company"])
        print("Role:", app["role"])
        print("Status:", app["status"])
        print("Applied on:", app["applied_on"])
        print("Interview date:", app["interview_date"] or "Not scheduled")
        print("Link:", app["link"] or "Not provided")


def search_applications(applications):
    keyword = input("Search company or role: ").strip().lower()

    if not keyword:
        print("Enter a search term.")
        return

    matches = [
        app for app in applications
        if keyword in app["company"].lower()
        or keyword in app["role"].lower()
    ]

    if matches:
        view_applications(matches)
    else:
        print("No matching applications found.")


def update_application(applications):
    try:
        application_id = int(input("Enter application ID: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for app in applications:
        if app["id"] == application_id:
            print("\nAvailable statuses:")

            for index, status in enumerate(STATUSES, start=1):
                print(f"{index}. {status}")

            try:
                choice = int(input("Choose status number: "))
                if choice < 1 or choice > len(STATUSES):
                    print("Invalid status choice.")
                    return
            except ValueError:
                print("Enter a valid number.")
                return

            app["status"] = STATUSES[choice - 1]

            if app["status"] == "Interview":
                interview_date = input(
                    "Interview date (YYYY-MM-DD, optional): "
                ).strip()

                if interview_date:
                    try:
                        datetime.strptime(interview_date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format.")
                        return

                app["interview_date"] = interview_date

            save_applications(applications)
            print("Application updated successfully!")
            return

    print("Application ID not found.")


def delete_application(applications):
    try:
        application_id = int(input("Enter application ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for app in applications:
        if app["id"] == application_id:
            applications.remove(app)
            save_applications(applications)
            print("Application deleted.")
            return

    print("Application ID not found.")


def show_statistics(applications):
    print("\n--- Application Statistics ---")
    print("Total applications:", len(applications))

    for status in STATUSES:
        count = sum(
            1 for app in applications
            if app["status"] == status
        )
        print(f"{status}: {count}")

    total = len(applications)

    if total:
        selected = sum(
            1 for app in applications
            if app["status"] == "Selected"
        )

        print(f"Selection rate: {selected / total * 100:.1f}%")


def main():
    applications = load_applications()

    while True:
        print("\n===== JOB APPLICATION TRACKER =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Applications")
        print("4. Update Status")
        print("5. Delete Application")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            search_applications(applications)
        elif choice == "4":
            update_application(applications)
        elif choice == "5":
            delete_application(applications)
        elif choice == "6":
            show_statistics(applications)
        elif choice == "7":
            print("Good luck with your applications!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
