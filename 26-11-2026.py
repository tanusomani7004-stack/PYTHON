
import urllib.request
import urllib.error
import time
import csv
from datetime import datetime


WEBSITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]

REPORT_FILE = "website_report.csv"


def check_website(url):
    start_time = time.time()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "PythonHealthMonitor/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            status_code = response.status

        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)

        return {
            "url": url,
            "status": "ONLINE",
            "code": status_code,
            "response_time": response_time
        }

    except urllib.error.HTTPError as error:
        end_time = time.time()

        return {
            "url": url,
            "status": "HTTP ERROR",
            "code": error.code,
            "response_time": round((end_time - start_time) * 1000, 2)
        }

    except (urllib.error.URLError, TimeoutError, OSError):
        return {
            "url": url,
            "status": "OFFLINE",
            "code": "N/A",
            "response_time": "N/A"
        }


def monitor_websites():
    results = []

    print("\n========== WEBSITE MONITOR ==========")

    for website in WEBSITES:
        print("\nChecking:", website)

        result = check_website(website)
        results.append(result)

        print("Status:", result["status"])
        print("Status Code:", result["code"])
        print("Response Time:", result["response_time"], "ms")

    return results


def save_report(results):
    file_exists = False

    try:
        with open(REPORT_FILE, "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(REPORT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Website",
                "Status",
                "Status Code",
                "Response Time (ms)"
            ])

        for result in results:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                result["url"],
                result["status"],
                result["code"],
                result["response_time"]
            ])

    print("\nReport saved successfully:", REPORT_FILE)


def show_summary(results):
    online = sum(
        1 for result in results
        if result["status"] == "ONLINE"
    )

    offline = sum(
        1 for result in results
        if result["status"] != "ONLINE"
    )

    print("\n========== SUMMARY ==========")
    print("Total Websites:", len(results))
    print("Online Websites:", online)
    print("Offline / Error Websites:", offline)


def main():
    while True:
        print("\n======= SMART WEBSITE HEALTH MONITOR =======")
        print("1. Check All Websites")
        print("2. View Last Check Summary")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            results = monitor_websites()
            show_summary(results)
            save_report(results)

        elif choice == "2":
            print("\nOpen website_report.csv to view saved reports.")

        elif choice == "3":
            print("Monitor closed successfully!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
