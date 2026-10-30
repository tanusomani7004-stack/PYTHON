import os
import json
import base64
import hashlib
import getpass
from cryptography.fernet import Fernet, InvalidToken

VAULT_FILE = "password_vault.json"


def derive_key(master_password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode(),
        salt,
        600000,
        dklen=32
    )

    return base64.urlsafe_b64encode(key)


def create_vault():
    print("\n--- Create Password Vault ---")

    master_password = getpass.getpass("Create master password: ")

    if len(master_password) < 8:
        print("Master password must be at least 8 characters.")
        return

    confirm = getpass.getpass("Confirm master password: ")

    if master_password != confirm:
        print("Passwords do not match.")
        return

    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(b"[]")

    vault = {
        "salt": base64.b64encode(salt).decode(),
        "data": encrypted_data.decode()
    }

    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)

    print("Vault created successfully!")


def unlock_vault():
    if not os.path.exists(VAULT_FILE):
        print("No vault found. Create one first.")
        return None, None

    try:
        with open(VAULT_FILE, "r") as file:
            vault = json.load(file)

        salt = base64.b64decode(vault["salt"])
        master_password = getpass.getpass("Enter master password: ")

        key = derive_key(master_password, salt)
        cipher = Fernet(key)

        decrypted_data = cipher.decrypt(
            vault["data"].encode()
        )

        passwords = json.loads(decrypted_data.decode())

        print("Vault unlocked successfully!")
        return vault, passwords

    except (InvalidToken, ValueError, KeyError, json.JSONDecodeError):
        print("Incorrect password or invalid vault.")
        return None, None


def save_vault(vault, passwords, cipher):
    encrypted_data = cipher.encrypt(
        json.dumps(passwords).encode()
    )

    vault["data"] = encrypted_data.decode()

    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)


def add_password(vault, passwords, cipher):
    website = input("Website or app: ").strip()
    username = input("Username or email: ").strip()
    password = getpass.getpass("Account password: ")

    if not website or not username or not password:
        print("All fields are required.")
        return

    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_vault(vault, passwords, cipher)
    print("Password saved securely!")


def view_passwords(passwords):
    print("\n--- Saved Accounts ---")

    if not passwords:
        print("No passwords saved.")
        return

    for index, item in enumerate(passwords, start=1):
        print(f"{index}. {item['website']} — {item['username']}")


def search_password(passwords):
    query = input("Search website or username: ").strip().lower()

    results = [
        item for item in passwords
        if query in item["website"].lower()
        or query in item["username"].lower()
    ]

    if not results:
        print("No matching accounts found.")
        return

    for item in results:
        print("\nWebsite:", item["website"])
        print("Username:", item["username"])
        print("Password:", item["password"])


def delete_password(vault, passwords, cipher):
    view_passwords(passwords)

    try:
        index = int(input("Enter account number to delete: ")) - 1
    except ValueError:
        print("Enter a valid number.")
        return

    if 0 <= index < len(passwords):
        removed = passwords.pop(index)
        save_vault(vault, passwords, cipher)
        print(f"Deleted account for {removed['website']}.")
    else:
        print("Invalid account number.")


def main():
    while True:
        print("\n===== SECURE PASSWORD VAULT =====")
        print("1. Create Vault")
        print("2. Unlock Vault")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if os.path.exists(VAULT_FILE):
                print("A vault already exists.")
            else:
                create_vault()

        elif choice == "2":
            vault, passwords = unlock_vault()

            if vault is None:
                continue

            salt = base64.b64decode(vault["salt"])
            master_password = getpass.getpass(
                "Enter master password again to initialize session: "
            )
            cipher = Fernet(derive_key(master_password, salt))

            while True:
                print("\n--- Vault Menu ---")
                print("1. Add Password")
                print("2. View Accounts")
                print("3. Search Password")
                print("4. Delete Account")
                print("5. Lock Vault")

                action = input("Choose an option: ").strip()

                if action == "1":
                    add_password(vault, passwords, cipher)
                elif action == "2":
                    view_passwords(passwords)
                elif action == "3":
                    search_password(passwords)
                elif action == "4":
                    delete_password(vault, passwords, cipher)
                elif action == "5":
                    print("Vault locked.")
                    break
                else:
                    print("Invalid choice.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
