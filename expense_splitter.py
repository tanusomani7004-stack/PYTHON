from collections import defaultdict


def get_expenses():
    expenses = {}

    print("\nEnter participant names.")
    print("Type 'done' when finished.\n")

    while True:
        name = input("Name: ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Name cannot be empty.")
            continue

        if name in expenses:
            print(" Person already added.")
            continue

        try:
            amount = float(input(f"Amount paid by {name}: ₹"))

            if amount < 0:
                print(" Amount cannot be negative.")
                continue

            expenses[name] = amount

        except ValueError:
            print(" Enter a valid amount.")

    return expenses


def calculate_settlements(expenses):
    total = sum(expenses.values())
    people = len(expenses)

    if people == 0:
        return total, 0, []

    share = total / people

    balances = {}

    for person, paid in expenses.items():
        balances[person] = round(paid - share, 2)

    creditors = []
    debtors = []

    for person, balance in balances.items():

        if balance > 0:
            creditors.append([person, balance])

        elif balance < 0:
            debtors.append([person, -balance])

    settlements = []

    i = 0
    j = 0

    while i < len(debtors) and j < len(creditors):

        debtor = debtors[i]
        creditor = creditors[j]

        amount = min(debtor[1], creditor[1])

        settlements.append(
            f"{debtor[0]} pays {creditor[0]} ₹{amount:.2f}"
        )

        debtor[1] -= amount
        creditor[1] -= amount

        if debtor[1] < 0.01:
            i += 1

        if creditor[1] < 0.01:
            j += 1

    return total, share, settlements


def show_summary(expenses, total, share):

    print("\n" + "=" * 45)
    print("             EXPENSE SUMMARY")
    print("=" * 45)

    for person, amount in expenses.items():
        print(f"{person:<15} ₹{amount:.2f}")

    print("-" * 45)
    print(f"Total Expense   : ₹{total:.2f}")
    print(f"Each Person Pays: ₹{share:.2f}")


def main():

    print("=" * 45)
    print("           EXPENSE SPLITTER")
    print("=" * 45)

    expenses = get_expenses()

    if not expenses:
        print("\n No expenses entered.")
        return

    total, share, settlements = calculate_settlements(expenses)

    show_summary(expenses, total, share)

    print("\n========== SETTLEMENT ==========")

    if settlements:
        for settlement in settlements:
            print("", settlement)
    else:
        print(" Everyone has paid equally!")

    print("\n Done!")


if __name__ == "__main__":
    main()
