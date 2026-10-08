import os
import shutil
import hashlib


def calculate_hash(file_path):
    hash_object = hashlib.md5()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                hash_object.update(data)

        return hash_object.hexdigest()

    except Exception:
        return None


def find_duplicates(folder):
    file_hashes = {}
    duplicates = []

    for root, folders, files in os.walk(folder):

        for file_name in files:

            file_path = os.path.join(root, file_name)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in file_hashes:
                duplicates.append(
                    (file_path, file_hashes[file_hash])
                )
            else:
                file_hashes[file_hash] = file_path

    return duplicates


def backup_files(source, destination):

    if not os.path.exists(source):
        print("❌ Source folder does not exist.")
        return

    os.makedirs(destination, exist_ok=True)

    count = 0

    for root, folders, files in os.walk(source):

        relative_path = os.path.relpath(root, source)

        backup_folder = os.path.join(
            destination,
            relative_path
        )

        os.makedirs(backup_folder, exist_ok=True)

        for file_name in files:

            source_file = os.path.join(
                root,
                file_name
            )

            destination_file = os.path.join(
                backup_folder,
                file_name
            )

            shutil.copy2(
                source_file,
                destination_file
            )

            count += 1

    print(f"✅ {count} files backed up successfully!")


def show_folder_info(folder):

    if not os.path.exists(folder):
        print("❌ Folder does not exist.")
        return

    total_files = 0
    total_size = 0

    for root, folders, files in os.walk(folder):

        for file_name in files:

            file_path = os.path.join(
                root,
                file_name
            )

            try:
                total_size += os.path.getsize(file_path)
                total_files += 1
            except:
                pass

    size_mb = total_size / (1024 * 1024)

    print("\n========== FOLDER INFO ==========")
    print("Total Files :", total_files)
    print(f"Total Size  : {size_mb:.2f} MB")


def main():

    while True:

        print("\n======================================")
        print("       📁 SMART FILE MANAGER")
        print("======================================")
        print("1. Backup Folder")
        print("2. Find Duplicate Files")
        print("3. Folder Information")
        print("4. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            source = input(
                "Enter source folder path: "
            ).strip()

            destination = input(
                "Enter backup folder path: "
            ).strip()

            backup_files(
                source,
                destination
            )

        elif choice == "2":

            folder = input(
                "Enter folder path: "
            ).strip()

            print("\n🔍 Searching for duplicates...")

            duplicates = find_duplicates(folder)

            if not duplicates:
                print("✅ No duplicate files found.")

            else:

                print("\n========== DUPLICATE FILES ==========")

                for duplicate, original in duplicates:

                    print("\nDuplicate:")
                    print(duplicate)

                    print("Original:")
                    print(original)

                    print("--------------------------------")

                print(
                    f"\nFound {len(duplicates)} duplicate files."
                )

        elif choice == "3":

            folder = input(
                "Enter folder path: "
            ).strip()

            show_folder_info(folder)

        elif choice == "4":

            print("👋 Exiting Smart File Manager...")
            break

        else:

            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
