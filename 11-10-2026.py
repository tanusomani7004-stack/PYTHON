import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved expenses.")

    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Expense name: ").strip()
    category = input("Category (Food/Travel/Shopping/Other): ").strip()

    try:
        amount = float(input("Amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "id": max((e["id"] for e in expenses), default=0) + 1,
        "title": title,
        "category": category.title(),
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    if not title or not category:
        print("Name and category cannot be empty.")
        return

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- Expense History ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['date']} | "
            f"{expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def set_budget():
    try:
        budget = float(input("Enter your monthly budget (₹): "))

        if budget <= 0:
            print("Budget must be greater than zero.")
            return None

        with open("budget.json", "w") as file:
            json.dump({"monthly_budget": budget}, file)

        print("Monthly budget saved!")
        return budget

    except ValueError:
        print("Please enter a valid budget.")
        return None


def load_budget():
    if os.path.exists("budget.json"):
        try:
            with open("budget.json", "r") as file:
                return json.load(file).get("monthly_budget", 0)
        except (json.JSONDecodeError, OSError):
            pass

    return 0


def show_summary(expenses):
    current_month = datetime.now().strftime("%Y-%m")

    monthly_expenses = [
        e for e in expenses
        if e["date"].startswith(current_month)
    ]

    total = sum(e["amount"] for e in monthly_expenses)
    categories = {}

    for expense in monthly_expenses:
        category = expense["category"]
        categories[category] = (
            categories.get(category, 0) + expense["amount"]
        )

    budget = load_budget()

    print("\n--- Monthly Summary ---")
    print(f"Month: {current_month}")
    print(f"Total spent: ₹{total:.2f}")

    if categories:
        print("\nCategory-wise spending:")
        for category, amount in categories.items():
            print(f"{category}: ₹{amount:.2f}")

    if budget > 0:
        remaining = budget - total
        print(f"\nBudget: ₹{budget:.2f}")
        print(f"Remaining: ₹{remaining:.2f}")

        if total > budget:
            print("ALERT: Monthly budget exceeded!")
        elif total >= budget * 0.8:
            print("WARNING: You have used at least 80% of your budget.")
        else:
            print("You are within your budget.")


def delete_expense(expenses):
    view_expenses(expenses)

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully!")
            return

    print("Expense ID not found.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL BUDGET TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Monthly Summary & Alerts")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            set_budget()
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Happy budgeting!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
