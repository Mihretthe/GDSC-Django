from library import Library

library = Library()

library.addBook("Book1", "Abebe", "12312", True)
library.addBook("Book2", "Abebe", "12312", True)
library.addBook("Book3", "Abebe", "12312", True)
library.addBook("Book4", "Abebe", "12312", True)

library.registerUser(12, "Mihret", [])
library.registerUser(13, "Tekalgn", [])
library.registerUser(14, "Adanech", [])
library.registerUser(11, "Betemariam", [])

library.handleTransactionBorrow(11, "Book1")
library.handleTransactionBorrow(12, "Book2")
library.handleTransactionBorrow(13, "Book1")
library.handleTransactionBorrow(11, "Book3")

library.getLibraryInformation()
library.getUserInformation()

library.handleTransactionReturn(11, "Book1")
library.handleTransactionReturn(12, "Book2")
library.handleTransactionReturn(13, "Book1")
library.handleTransactionReturn(11, "Book3")

library.getLibraryInformation()
library.getUserInformation()
library.displayTransactionDetail()