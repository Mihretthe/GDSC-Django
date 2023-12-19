from books import Book

class User:
    def __init__(self, user_id, name, books_borrowed):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = books_borrowed
        self.returned = []

    def getID(self):
        return self.user_id
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def displayUserDetails(self):
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
    
    def borrowBooks(self, book):
        self.books_borrowed.append(book)

    def displayBooks(self):
        print(f"Borrowed Books by {self.name}")
        for book in self.books_borrowed:
            print(book.getTitle(), end = " ")
        print()

    def returnBook(self, book):     
        if book in self.books_borrowed:            
            self.returned.append(book)
            self.books_borrowed.remove(book)
            print(f"Book {book.getTitle()} is returned")
        else:
            print(f"{self.user_id} doesn't borrow such a book.")

    

