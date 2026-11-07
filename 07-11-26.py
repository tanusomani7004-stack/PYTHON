
import os
from collections import Counter

LOG_FILE = "application.log"
REPORT_FILE = "error_report.txt"


def create_sample_log():
    if os.path.exists(LOG_FILE):
        return

    sample_logs = [
        "INFO: Application started",
        "INFO: User logged in",
        "WARNING: High memory usage",
        "ERROR: Database connection failed",
        "INFO: User logged out",
        "ERROR: Database connection failed",
        "CRITICAL: Server unavailable",
        "WARNING: Low disk space",
        "INFO: Application restarted",
        "ERROR: Invalid user request",
        "INFO: Backup completed",
        "CRITICAL: Server unavailable"
    ]

    with open(LOG_FILE, "w") as file:
        for log in sample_logs:
            file.write(log + "\n")


def read_logs():
    try:
        with open(LOG_FILE, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Log file not found!")
        return []


def analyze_logs():
    logs = read_logs()

    if not logs:
        return

    levels = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    error_messages = []

    for log in logs:
        for level in levels:
            if log.startswith(level + ":"):
                levels[level] += 1

                if level in ["ERROR", "CRITICAL"]:
                    message = log.split(":", 1)[1].strip()
                    error_messages.append(message)

                break

    print("\n========== LOG ANALYSIS ==========")
    print("Total Logs:", len(logs))

    for level, count in levels.items():
        print(level, ":", count)

    print("\nMost Common Errors:")

    if error_messages:
        error_count = Counter(error_messages)

        for message, count in error_count.most_common():
            print(message, "->", count, "times")
    else:
        print("No errors found.")


def search_logs():
    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Please enter a keyword!")
        return

    logs = read_logs()
    results = []

    for log in logs:
        if keyword in log.lower():
            results.append(log)

    print("\nSearch Results:")

    if results:
        for result in results:
            print(result)
        print("Total matches:", len(results))
    else:
        print("No matching logs found.")


def generate_report():
    logs = read_logs()

    if not logs:
        return

    error_logs = []

    for log in logs:
        if log.startswith("ERROR:") or log.startswith("CRITICAL:"):
            error_logs.append(log)

    with open(REPORT_FILE, "w") as file:
        file.write("SMART LOG ANALYZER REPORT\n")
        file.write("=========================\n\n")
        file.write("Total log entries: " + str(len(logs)) + "\n")
        file.write("Total errors: " + str(len(error_logs)) + "\n\n")
        file.write("ERROR DETAILS:\n")

        for log in error_logs:
            file.write(log + "\n")

    print("Report generated:", REPORT_FILE)


def main():
    create_sample_log()

    while True:
        print("\n========== SMART LOG ANALYZER ==========")
        print("1. Analyze Logs")
        print("2. Search Logs")
        print("3. Generate Error Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyze_logs()

        elif choice == "2":
            search_logs()

        elif choice == "3":
            generate_report()

        elif choice == "4":
            print("Program closed successfully!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
