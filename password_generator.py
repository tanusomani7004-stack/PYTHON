import random
import string


def generate_password(length, use_numbers, use_special):

    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def main():

    print("=" * 45)
    print("       🔐 PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("❌ Password length should be at least 4.")
            return

    except ValueError:
        print("❌ Enter a valid number.")
        return

    numbers = input(
        "Include numbers? (y/n): "
    ).lower() == "y"

    special = input(
        "Include special characters? (y/n): "
    ).lower() == "y"

    password = generate_password(
        length,
        numbers,
        special
    )

    strength = check_strength(password)

    print("\n" + "=" * 45)
    print("Generated Password :", password)
    print("Password Strength  :", strength)
    print("=" * 45)


if __name__ == "__main__":
    main()
