contacts = {}


def add_contact():
    name = input("Enter name: ").strip()

    if name in contacts:
        print("❌ Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("✅ Contact added successfully!")


def show_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return

    print("\n========== CONTACTS ==========")

    for name, details in contacts.items():
        print(f"""
Name  : {name}
Phone : {details['phone']}
Email : {details['email']}
-------------------------------""")


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        contact = contacts[name]

        print("\n✅ Contact Found")
        print("Name :", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("❌ Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    print("\n1. Update Phone")
    print("2. Update Email")

    choice = input("Enter choice: ")

    if choice == "1":
        contacts[name]["phone"] = input("Enter new phone: ")
        print("✅ Phone updated.")

    elif choice == "2":
        contacts[name]["email"] = input("Enter new email: ")
        print("✅ Email updated.")

    else:
        print("❌ Invalid choice.")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("✅ Contact deleted.")
    else:
        print("❌ Contact not found.")


def main():

    while True:

        print("\n" + "=" * 35)
        print("       📱 CONTACT BOOK")
        print("=" * 35)
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=" * 35)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\n👋 Contact Book closed.")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
