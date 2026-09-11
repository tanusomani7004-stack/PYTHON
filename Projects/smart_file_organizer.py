import os
import shutil


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".xls", ".xlsx", ".ppt", ".pptx"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".flv", ".wmv"
    ],

    "Music": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz"
    ],

    "Code": [
        ".py", ".js", ".html", ".css",
        ".java", ".cpp", ".c", ".sql",
        ".json"
    ]
}


def get_category(extension):
    """Find category according to file extension."""

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_folder(folder_path):

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("❌ The given path is not a folder.")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):

        source_path = os.path.join(folder_path, filename)

        # Ignore folders
        if os.path.isdir(source_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        category = get_category(extension)

        # Create category folder
        category_folder = os.path.join(
            folder_path,
            category
        )

        os.makedirs(
            category_folder,
            exist_ok=True
        )

        destination_path = os.path.join(
            category_folder,
            filename
        )

        # Handle duplicate filenames
        if os.path.exists(destination_path):

            name, ext = os.path.splitext(filename)

            counter = 1

            while os.path.exists(destination_path):

                new_name = f"{name}_{counter}{ext}"

                destination_path = os.path.join(
                    category_folder,
                    new_name
                )

                counter += 1

        shutil.move(
            source_path,
            destination_path
        )

        print(
            f"📁 {filename}  →  {category}/"
        )

        files_moved += 1

    print("\n" + "=" * 45)
    print("        ORGANIZATION COMPLETE")
    print("=" * 45)
    print(f"Files organized: {files_moved}")


def show_categories():

    print("\n========== FILE CATEGORIES ==========")

    for category, extensions in FILE_CATEGORIES.items():

        print(
            f"{category:12} : "
            f"{', '.join(extensions)}"
        )

    print("Others       : Unknown extensions")


def main():

    print("\n======================================")
    print("       🗂️ SMART FILE ORGANIZER")
    print("======================================")

    while True:

        print("\n1. Organize Folder")
        print("2. Show Supported Categories")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            folder = input(
                "\nEnter folder path: "
            ).strip()

            organize_folder(folder)

        elif choice == "2":
            show_categories()

        elif choice == "3":
            print("\n👋 Program closed.")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
