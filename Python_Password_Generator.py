import secrets
import string


def generate_password(length=16, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+"

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]

    if use_symbols:
        password.append(secrets.choice("!@#$%^&*()-_=+"))

    password.extend(
        secrets.choice(characters)
        for _ in range(length - len(password))
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print("=== Secure Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))
        symbols = input("Include symbols? (y/n): ").strip().lower()

        if symbols not in ("y", "n"):
            print("Please enter y or n.")
            return

        password = generate_password(length, symbols == "y")

        print("\nGenerated Password:", password)
        print("Password Length:", len(password))

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
