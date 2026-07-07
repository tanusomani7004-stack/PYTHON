import csv
from pathlib import Path
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if self.is_available():
            self.status = "issued"
            logging.info(f"Book issued: {self.title}")
        else:
            logging.error(f"Attempt to issue already issued book: {self.title}")
            raise Exception("Book is already issued!")

    def return_book(self):
        if not self.is_available():
            self.status = "available"
            logging.info(f"Book returned: {self.title}")
        else:
            logging.error(f"Attempt to return already available book: {self.title}")
            raise Exception("Book is not issued!")

class LibraryInventory:
    def __init__(self, file_path="books.csv"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if not self.file_path.exists():
                logging.warning("CSV file not found. Creating a new one.")
                return

            with self.file_path.open("r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        title=row["title"],
                        author=row["author"],
                        isbn=row["isbn"],
                        status=row["status"]
                    )
                    self.books.append(book)
        except Exception as e:
            logging.error(f"Error loading CSV: {e}")
            print("CSV corrupted or unreadable!")

    def save_books(self):
        try:
            with self.file_path.open("w", newline="", encoding="utf-8") as file:
                fieldnames = ["title", "author", "isbn", "status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.books:
                    writer.writerow(book.to_dict())
        except Exception as e:
            logging.error(f"Error saving CSV: {e}")
            print("Error saving file!")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        logging.info(f"Book added: {book.title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
            return
        for book in self.books:
            print(book)

def main_menu():
    inventory = LibraryInventory()

    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        print("=======================================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")

            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book Added Successfully!")

        elif choice == 2:
            isbn = input("Enter ISBN to Issue: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                try:
                    book.issue()
                    inventory.save_books()
                    print("Book Issued Successfully!")
                except Exception as e:
                    print(e)
            else:
                print("Book not found!")

        elif choice == 3:
            isbn = input("Enter ISBN to Return: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                try:
                    book.return_book()
                    inventory.save_books()
                    print("Book Returned Successfully!")
                except Exception as e:
                    print(e)
            else:
                print("Book not found!")

        elif choice == 4:
            inventory.display_all()

      
        elif choice == 5:
            term = input("Search by Title: ")
            results = inventory.search_by_title(term)

            if results:
                print("\nSearch Results:")
                for b in results:
                    print(b)
            else:
                print("No book found!")

        elif choice == 6:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
