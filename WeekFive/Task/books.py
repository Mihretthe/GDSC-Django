class Book:
    def __init__(self, title, author, ISBN, availability_status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = availability_status

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title
    
    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author
    
    def setISBN(self, ISBN):
        self.ISBN = ISBN

    def getISBN(self):
        return self.ISBN
    
    def setAvail(self, availability_status = True):
        self.availability_status = availability_status

    def getAvail(self):
        return self.availability_status
    

    def display(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book ISBN: {self.ISBN}")
        print(f"Book Availability: {self.availability_status}")

    def updateStatus(self, availability_status):
        self.availability_status = availability_status
