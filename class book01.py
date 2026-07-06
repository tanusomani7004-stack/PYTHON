class book:
    def __init__(self,title,author,isbn,status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print("The Title of the book is:",self.title)
        print("The Author of the book is:",self.author)
        print("The Internatinal book number is:",self.isbn)
        print("The Status of book is:",self.status)

    def availability(self):
        if self.status=="Available":
            print(f"'{self.title}' is available for borrowing.")
        else:
            print(f"'{self.title}' is currently checked out.")

    def issue(self):
        issue=input("Do you want to issue the book or not?") 
        if issue=="yes":
            print(f"Your book {self.title} is issued")
        else:
            print("")

    def return_book(self):
        return_book=input("Do you want to return book?")
        if return_book=="yes":
            print(f"your book {self.title} is returned")
        else:
            print("Book is already available in library")

    def  save_to_file(self):
        try:
            with open("library.txt","a") as f :
                f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")
        except:
            print("Error while saving to file")

    Books=[]
    while True:
        print("\n-----LIBRARY MENU------")
    print("1. Add a Book")
    print("2. View All Books")
    print("3.Issue a Book")
    print("4. Return a Book")
    print("5. Exit")
    choice=int(input("enter your choice"))

    if choice=="1":
        title=input("Enter book title:")
        author= input("Enter author name:")
        isbn=input("Enter ISBN number:")
        book=Book(title,author,isbn)
        books.append(book)
        book.save_to_file()
        print(len(books))
    elif choice == 2:
        if not books:
            print("No books available.")
        else:
            for b in books:
                b.display_details()
    elif choice == 3:
        isbn = input("Enter ISBN to issue: ")
        for b in books:
            if b.isbn == isbn:
                b.issue_book()
            break
            else:
                print("Book not found.")

    elif choice == 4:
        isbn = input("Enter ISBN to return: ")
        for b in books:
            if b.isbn == isbn:
                b.return_book()
            break
            else:
                print("Book not found.")

    elif choice == 5:
        break

    else:
        print("Invalid choice.")

obj1=book("abc","sdf",34,"Available")
obj1.display()
obj1.availability()
obj1.issue()
obj1.return_book()
    
