class Library:
    def __init__(self):
        self.books = ["Maths", "Science", "English", "Computer Science"]
        self.books.sort()
    def display_book(self):
        print("Books in library: ")
        for book in self.books:
            print(book)
    def add_book(self,book):
        self.books.append(book)
        self.books.sort()
        print(book, "added successfully")
    def lend_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print("Book has been lended")
        else:
            print("Book not available")
    def return_book(self,book):
        self.books.append(book)
        self.books.sort()
        print("Book returned successfully")
s1 = Library()
while True:
    print("1. Display Book")
    print("2. Add Book")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")
    choice = int(input("What would you like to do: "))
    if choice == 1:
        s1.display_book()
    elif choice == 2:
        book = input("Enter book you would like to add: ")
        s1.add_book(book)
    elif choice == 3:
        book = input("Enter book you would like to lend: ")
        s1.lend_book(book)
    elif choice == 4:
        book = input("Enter book you would like to return: ")
        s1.return_book(book)
    elif choice == 5:
        print("Thank you for visiting the library")
        break
    else:
        print("Invalid choice")