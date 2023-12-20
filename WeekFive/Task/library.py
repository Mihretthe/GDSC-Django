from books import Book
from user import User
from transaction import Transaction



class Library:
    def __init__(self):
        self.libraryBooks = {}
        self.users = {}
        self.transaction = Transaction()
        

    def addBook(self, title, author, ISBN, availability):
        book = Book(title, author, ISBN, availability)
        self.libraryBooks[title] = book

    def registerUser(self, user_id, name, books_borrowed):
        user = User(user_id, name, books_borrowed)
        self.users[user_id] = user

    
    def handleTransactionBorrow(self, user_id, book_title):
        # book = self.libraryBooks[book_title]
        # user = self.users[user_id]
        if self.libraryBooks[book_title].getAvail():
            self.users[user_id].borrowBooks(self.libraryBooks[book_title])
            self.libraryBooks[book_title].setAvail(False)
            self.transaction.recordTransactionBorrowed(user_id, book_title)

        else:
            print("Borrowed")

        # user.displayBooks()
        # book.display()

    def handleTransactionReturn(self, user_id, book_title):
        # book = self.libraryBooks[book_title]
        # user = self.users[user_id]
        if not self.libraryBooks[book_title].getAvail():
            self.transaction.recordTransactionReturned(user_id, book_title)
        self.users[user_id].returnBook(self.libraryBooks[book_title])
        self.libraryBooks[book_title].setAvail(True)
        

        

    def getLibraryInformation(self):
        print("Library Books")
        for key, value in self.libraryBooks.items():
            print(key , "Information")
            value.display()
            print()
        
    def getUserInformation(self):
        print("Users Information")        
        for key, value in self.users.items():
            print(f"{key} : {value.getName()}")
            value.displayBooks()

    def displayTransactionDetail(self):
        self.transaction.report()










    





