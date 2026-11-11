
import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(folder, filename):
    name, extension = os.path.splitext(filename)
    new_path = os.path.join(folder, filename)
    counter = 1

    while os.path.exists(new_path):
        new_filename = f"{name}_{counter}{extension}"
        new_path = os.path.join(folder, new_filename)
        counter += 1

    return new_path


def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return

    moved_files = 0
    skipped_files = 0

    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path, filename)

        if not os.path.isfile(source_path):
            continue

        category = get_category(filename)

        destination_folder = os.path.join(
            folder_path, category
        )

        os.makedirs(destination_folder, exist_ok=True)

        destination_path = get_unique_path(
            destination_folder, filename
        )

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {category}")
            moved_files += 1

        except OSError as error:
            print(f"Could not move {filename}: {error}")
            skipped_files += 1

    print("\n========== ORGANIZATION REPORT ==========")
    print("Files moved:", moved_files)
    print("Files skipped:", skipped_files)
    print("Organization completed!")


def show_categories():
    print("\nAvailable Categories:")

    for category, extensions in FILE_CATEGORIES.items():
        if extensions:
            print(category, ":", ", ".join(extensions))
        else:
            print(category, ": All other file types")


def main():
    while True:
        print("\n======= SMART DOWNLOADS MANAGER =======")
        print("1. Organize Downloads Folder")
        print("2. Show File Categories")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            folder_path = input(
                "Enter folder path: "
            ).strip().strip('"')

            organize_files(folder_path)

        elif choice == "2":
            show_categories()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
