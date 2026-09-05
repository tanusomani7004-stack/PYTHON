from datetime import datetime

# Account details
account = {
    "name": "Tannu",
    "pin": "1234",
    "balance": 10000,
    "transactions": []
}


def add_transaction(transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    account["transactions"].append(transaction)


def check_balance():
    print(f"\n💰 Current Balance: ₹{account['balance']:.2f}")


def deposit():
    try:
        amount = float(input("\nEnter amount to deposit: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        account["balance"] += amount
        add_transaction("Deposit", amount)

        print(f"✅ ₹{amount:.2f} deposited successfully.")
        check_balance()

    except ValueError:
        print("❌ Please enter a valid amount.")


def withdraw():
    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        if amount > account["balance"]:
            print("❌ Insufficient balance.")
            return

        account["balance"] -= amount
        add_transaction("Withdrawal", amount)

        print(f"✅ ₹{amount:.2f} withdrawn successfully.")
        check_balance()

    except ValueError:
        print("❌ Please enter a valid amount.")


def mini_statement():
    if not account["transactions"]:
        print("\n📭 No transactions found.")
        return

    print("\n========== MINI STATEMENT ==========")

    for transaction in account["transactions"]:
        print(
            f"{transaction['date']} | "
            f"{transaction['type']} | "
            f"₹{transaction['amount']:.2f}"
        )

    print("-------------------------------------")
    print(f"Available Balance: ₹{account['balance']:.2f}")


def login():
    attempts = 3

    while attempts > 0:
        pin = input("\nEnter your 4-digit PIN: ")

        if pin == account["pin"]:
            print(f"\n✅ Welcome, {account['name']}!")
            return True

        attempts -= 1
        print(f"❌ Incorrect PIN. Attempts left: {attempts}")

    print("\n🔒 Account locked.")
    return False


def atm_menu():
    while True:
        print("\n")
        print("================================")
        print("          🏦 ATM SYSTEM")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            mini_statement()

        elif choice == "5":
            print("\n👋 Thank you for using our ATM!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Program starts here
print("================================")
print("      🏦 WELCOME TO ATM")
print("================================")

if login():
    atm_menu()
