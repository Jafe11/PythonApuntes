class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.avalliable = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def borrow(self):
        if self.avalliable:
            self.avalliable = False
            print(f"You have borrowed '{self.title}'.")
        else: 
            print(f"'{self.title}' is not available for borrowing.")

    def returnBook(self):
        if not self.avalliable:
            self.avalliable = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
    

class user:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def __str__(self):
            return f"User {self.user_id}: {self.name}"
        
    def borrowBook(self, book):
        if book.avalliable:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"'{book.title}' is not available for borrowing.")
    
    def returnBook(self, book):
        if book in self.borrowed_books:
            book.returnBook()
            self.borrowed_books.remove(book)
        else:
            print(f"You have not borrowed '{book.title}'.")
        
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def addBook(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")
    
    def adduser(self, user):
        self.users.append(user)
        print(f"Added user {user.name} to the library.")

    def listBooks(self):
        print("Books in the library:")
        for book in self.books:
            if book.avalliable:
                print(f"- {book}")


libro1 = Book("1984", "George Orwell", 1949)
libro2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)  
libro3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

user1 = user("Alice", 1)
user2 = user("Bob", 2)

library = Library()
library.addBook(libro1)
library.addBook(libro2)
library.addBook(libro3)

library.adduser(user1)
library.adduser(user2)

library.listBooks()

user1.borrowBook(libro1)
user1.borrowBook(libro2)
user2.borrowBook(libro3)

library.listBooks()
    
for book in user1.borrowed_books:
    print(f"{user1.name} has borrowed: {book}")

user1.returnBook(libro1)
library.listBooks()
