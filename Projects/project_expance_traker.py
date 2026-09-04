import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# ---------------- LOAD DATA ----------------
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


# ---------------- SAVE DATA ----------------
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# ---------------- ADD EXPENSE ----------------
def add_expense(expenses):
    title = input("Enter expense title: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\n✅ Expense added successfully!")


# ---------------- SHOW EXPENSES ----------------
def show_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['date']}"
        )


# ---------------- DELETE EXPENSE ----------------
def delete_expense(expenses):
    show_expenses(expenses)

    if not expenses:
        return

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)

            # Reassign IDs
            for index, item in enumerate(expenses, start=1):
                item["id"] = index

            save_expenses(expenses)

            print("✅ Expense deleted.")
            return

    print("❌ Expense not found.")


# ---------------- SEARCH ----------------
def search_expense(expenses):
    keyword = input("Search expense: ").lower()

    results = [
        expense for expense in expenses
        if keyword in expense["title"].lower()
        or keyword in expense["category"].lower()
    ]

    if not results:
        print("\n❌ No matching expenses found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for expense in results:
        print(
            f"{expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['date']}"
        )


# ---------------- CATEGORY SUMMARY ----------------
def category_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


# ---------------- MONTHLY TOTAL ----------------
def monthly_total(expenses):
    month = input("Enter month (YYYY-MM): ")

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["date"].startswith(month)
    )

    print(f"\n💰 Total expenses for {month}: ₹{total:.2f}")


# ---------------- HIGHEST EXPENSE ----------------
def highest_expense(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\n========== HIGHEST EXPENSE ==========")
    print(f"Title    : {highest['title']}")
    print(f"Category : {highest['category']}")
    print(f"Amount   : ₹{highest['amount']}")
    print(f"Date     : {highest['date']}")


# ---------------- MAIN MENU ----------------
def main():
    expenses = load_expenses()

    while True:
        print("\n")
        print("================================")
        print("       💰 EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Category Summary")
        print("6. Monthly Total")
        print("7. Highest Expense")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            search_expense(expenses)

        elif choice == "5":
            category_summary(expenses)

        elif choice == "6":
            monthly_total(expenses)

        elif choice == "7":
            highest_expense(expenses)

        elif choice == "8":
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()
