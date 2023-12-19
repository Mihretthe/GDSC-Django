from collections import defaultdict

# from library import Library


class Transaction:
    def __init__(self):
        self.transaction = defaultdict(list)
    
    def recordTransactionBorrowed(self, user_id, book_title):
        self.transaction[user_id].append(f"User {user_id} borrows {book_title}")

    def recordTransactionReturned(self, user_id, book_title):
        self.transaction[user_id].append(f"User {user_id} returns {book_title}")


    def report(self):
        print("Transaction Report")
        for key, value in self.transaction.items():
            for val in value:
                print(val)






