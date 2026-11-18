
import csv
import os
from collections import Counter


def load_csv(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            if not reader.fieldnames:
                print("CSV file is empty or has no headers!")
                return None, None

            return reader.fieldnames, rows

    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except UnicodeDecodeError:
        print("Unable to read file encoding!")

    return None, None


def show_basic_info(headers, rows):
    print("\n========== DATASET INFORMATION ==========")
    print("Total Rows:", len(rows))
    print("Total Columns:", len(headers))

    print("\nColumn Names:")
    for column in headers:
        print("-", column)


def analyze_missing_values(headers, rows):
    print("\n========== MISSING VALUES ==========")

    for column in headers:
        missing = 0

        for row in rows:
            if not row.get(column, "").strip():
                missing += 1

        print(column, ":", missing)


def analyze_numeric_columns(headers, rows):
    print("\n========== NUMERIC ANALYSIS ==========")

    for column in headers:
        values = []

        for row in rows:
            try:
                value = float(row[column])
                values.append(value)
            except (ValueError, TypeError, KeyError):
                continue

        if values:
            average = sum(values) / len(values)

            print("\nColumn:", column)
            print("Valid Numbers:", len(values))
            print("Average:", round(average, 2))
            print("Minimum:", min(values))
            print("Maximum:", max(values))


def analyze_unique_values(headers, rows):
    print("\n========== UNIQUE VALUES ==========")

    for column in headers:
        values = []

        for row in rows:
            value = row.get(column, "").strip()

            if value:
                values.append(value)

        print(column, ":", len(set(values)), "unique values")


def show_most_common(headers, rows):
    print("\n========== MOST COMMON VALUES ==========")

    for column in headers:
        values = [
            row.get(column, "").strip()
            for row in rows
            if row.get(column, "").strip()
        ]

        if values:
            common = Counter(values).most_common(3)

            print("\nColumn:", column)

            for value, count in common:
                print(value, "->", count, "times")


def generate_report(headers, rows):
    report_file = "analysis_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("CSV DATA ANALYSIS REPORT\n")
        file.write("========================\n\n")

        file.write("Total Rows: " + str(len(rows)) + "\n")
        file.write("Total Columns: " + str(len(headers)) + "\n\n")

        for column in headers:
            missing = sum(
                1 for row in rows
                if not row.get(column, "").strip()
            )

            file.write(f"\nColumn: {column}\n")
            file.write(f"Missing Values: {missing}\n")

            values = []

            for row in rows:
                try:
                    values.append(float(row[column]))
                except (ValueError, TypeError, KeyError):
                    continue

            if values:
                file.write(f"Average: {sum(values) / len(values):.2f}\n")
                file.write(f"Minimum: {min(values)}\n")
                file.write(f"Maximum: {max(values)}\n")

    print("\nReport generated:", report_file)


def main():
    print("======= CSV DATA ANALYZER =======")

    file_path = input("Enter CSV file path: ").strip().strip('"')

    headers, rows = load_csv(file_path)

    if headers is None:
        return

    while True:
        print("\n1. Dataset Information")
        print("2. Missing Values Analysis")
        print("3. Numeric Data Analysis")
        print("4. Unique Values Analysis")
        print("5. Most Common Values")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            show_basic_info(headers, rows)

        elif choice == "2":
            analyze_missing_values(headers, rows)

        elif choice == "3":
            analyze_numeric_columns(headers, rows)

        elif choice == "4":
            analyze_unique_values(headers, rows)

        elif choice == "5":
            show_most_common(headers, rows)

        elif choice == "6":
            generate_report(headers, rows)

        elif choice == "7":
            print("Thank you for using CSV Analyzer!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
