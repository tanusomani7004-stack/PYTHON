import json
import os
import hashlib
import secrets
from datetime import datetime

USER_FILE = "users.json"
LOG_FILE = "security_logs.json"
MAX_ATTEMPTS = 3


def load_data(filename):
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        200000
    ).hex()


def log_event(username, event):
    logs = load_data(LOG_FILE)

    if not isinstance(logs, list):
        logs = []

    logs.append({
        "username": username,
        "event": event,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_data(LOG_FILE, logs)


def register():
    users = load_data(USER_FILE)

    username = input("Create username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists.")
        return

    password = input("Create password (minimum 8 characters): ")

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    salt = secrets.token_hex(16)

    users[username] = {
        "salt": salt,
        "password_hash": hash_password(password, salt),
        "failed_attempts": 0,
        "locked": False
    }

    save_data(USER_FILE, users)
    log_event(username, "Account registered")

    print("Account created successfully!")


def login():
    users = load_data(USER_FILE)

    username = input("Username: ").strip()

    if username not in users:
        log_event(username, "Login failed: unknown username")
        print("Invalid username or password.")
        return

    user = users[username]

    if user["locked"]:
        log_event(username, "Login blocked: account locked")
        print("Account locked due to repeated failed attempts.")
        return

    password = input("Password: ")
    password_hash = hash_password(password, user["salt"])

    if secrets.compare_digest(
        password_hash,
        user["password_hash"]
    ):
        user["failed_attempts"] = 0
        save_data(USER_FILE, users)

        log_event(username, "Successful login")
        print("Login successful! Welcome,", username)

    else:
        user["failed_attempts"] += 1

        log_event(username, "Failed login attempt")

        if user["failed_attempts"] >= MAX_ATTEMPTS:
            user["locked"] = True
            print("ALERT: Account locked after repeated failures!")
            log_event(username, "Security alert: account locked")
        else:
            remaining = MAX_ATTEMPTS - user["failed_attempts"]
            print("Incorrect password.")
            print("Attempts remaining:", remaining)

        save_data(USER_FILE, users)


def view_logs():
    logs = load_data(LOG_FILE)

    print("\n========== SECURITY LOGS ==========")

    if not isinstance(logs, list) or not logs:
        print("No activity recorded.")
        return

    for entry in logs:
        print(
            f"{entry['time']} | "
            f"User: {entry['username']} | "
            f"Event: {entry['event']}"
        )


def main():
    while True:
        print("\n===== LOGIN SECURITY MONITOR =====")
        print("1. Register")
        print("2. Login")
        print("3. View Security Logs")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            print("Exiting security monitor.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
