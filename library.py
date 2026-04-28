class library:
    
    def __init__(self):
        self.books = ["python", "java", "c++", "Data science"]

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("Available books:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")


lib = library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        book = input("Enter your book's name: ")
        lib.add_book(book)

    elif choice == 2:
        lib.show_books()

    elif choice == 3:
        book = input("Enter book to issue: ")
        lib.issue_book(book)

    elif choice == 4:
        book = input("Enter book to return: ")
        lib.return_book(book)

    elif choice == 5:
        print("thank you")
        break

    else:
        print("invalid choice")