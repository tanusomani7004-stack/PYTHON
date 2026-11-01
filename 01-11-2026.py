
import hashlib
import json
import os

DATABASE_FILE = "file_hashes.json"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: File not found!")
        return None

    except PermissionError:
        print("Error: Permission denied!")
        return None


def load_database():
    if not os.path.exists(DATABASE_FILE):
        return {}

    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the saved database.")
        return {}


def save_database(database):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)


def register_file():
    file_path = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("Invalid file path!")
        return

    file_hash = calculate_hash(file_path)

    if file_hash is None:
        return

    database = load_database()
    database[os.path.abspath(file_path)] = file_hash
    save_database(database)

    print("\nFile registered successfully!")
    print("SHA-256:", file_hash)


def verify_file():
    file_path = input("Enter file path to verify: ").strip().strip('"')
    absolute_path = os.path.abspath(file_path)

    database = load_database()

    if absolute_path not in database:
        print("File is not registered yet!")
        return

    if not os.path.isfile(absolute_path):
        print("WARNING: Registered file is missing!")
        return

    current_hash = calculate_hash(absolute_path)

    if current_hash is None:
        return

    saved_hash = database[absolute_path]

    if current_hash == saved_hash:
        print("STATUS: File is unchanged.")
    else:
        print("WARNING: File has been modified!")

        choice = input("Update saved fingerprint? (yes/no): ").lower()

        if choice == "yes":
            database[absolute_path] = current_hash
            save_database(database)
            print("Fingerprint updated successfully.")


def show_registered_files():
    database = load_database()

    if not database:
        print("No files registered yet.")
        return

    print("\n--- Registered Files ---")

    for file_path, file_hash in database.items():
        print("\nFile:", file_path)
        print("Hash:", file_hash)


def main():
    while True:
        print("\n===== FILE INTEGRITY CHECKER =====")
        print("1. Register a file")
        print("2. Verify a file")
        print("3. Show registered files")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_file()

        elif choice == "2":
            verify_file()

        elif choice == "3":
            show_registered_files()

        elif choice == "4":
            print("Thank you for using File Integrity Checker!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()
