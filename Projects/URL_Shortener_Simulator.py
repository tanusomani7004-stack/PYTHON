import random
import string


url_database = {}


def generate_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choices(characters, k=length))

        if code not in url_database:
            return code


def shorten_url():
    long_url = input("\nEnter long URL: ").strip()

    if not long_url:
        print("❌ URL cannot be empty.")
        return

    if not (
        long_url.startswith("http://")
        or long_url.startswith("https://")
    ):
        print("❌ Please enter a valid URL.")
        return

    code = generate_code()

    url_database[code] = {
        "url": long_url,
        "clicks": 0
    }

    print("\n✅ URL shortened successfully!")
    print(f"Short URL: https://short.ly/{code}")


def open_url():
    code = input("\nEnter short URL/code: ").strip()

    # Allow complete short URL too
    if "/" in code:
        code = code.rstrip("/").split("/")[-1]

    if code not in url_database:
        print("❌ Short URL not found.")
        return

    url_database[code]["clicks"] += 1

    print("\n🌐 Redirecting...")
    print("Original URL:", url_database[code]["url"])


def show_statistics():
    if not url_database:
        print("\n📭 No URLs created yet.")
        return

    print("\n========== URL STATISTICS ==========")

    total_clicks = 0

    for code, data in url_database.items():

        total_clicks += data["clicks"]

        print(f"""
Short Code : {code}
URL        : {data['url']}
Clicks     : {data['clicks']}
-------------------------------------
""")

    print(f"Total URLs    : {len(url_database)}")
    print(f"Total Clicks  : {total_clicks}")


def search_url():
    keyword = input("\nEnter keyword to search URL: ").lower()

    found = False

    for code, data in url_database.items():

        if keyword in data["url"].lower():

            print(f"\nCode   : {code}")
            print(f"URL    : {data['url']}")
            print(f"Clicks : {data['clicks']}")

            found = True

    if not found:
        print("❌ No matching URL found.")


def main():

    print("=" * 45)
    print("          🔗 PYTHON URL SHORTENER")
    print("=" * 45)

    while True:

        print("\n1. Shorten URL")
        print("2. Open Short URL")
        print("3. URL Statistics")
        print("4. Search URL")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            shorten_url()

        elif choice == "2":
            open_url()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            search_url()

        elif choice == "5":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
