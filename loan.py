from book import Book
from user import User

class Loan:
    def __init__(self):
        """
        Initialize Loan management with a dictionary.
        """
        self.loans = {}

    def borrow_book(self, user, book):
        """
        Assign a book to a user if available.
        """
        if book.available_copies > 0:
            if user.username not in self.loans:
                self.loans[user.username] = []
            self.loans[user.username].append(book)
            book.available_copies -= 1
        else:
            raise ValueError("No available copies of this book.")

    def return_book(self, user, book):
        """
        Unassign a book from a user.
        """
        if user.username in self.loans and book in self.loans[user.username]:
            self.loans[user.username].remove(book)
            book.available_copies += 1
        else:
            raise ValueError("The book is not borrowed by this user.")

    def count_user_books(self, user):
        """
        Count the number of books borrowed by a user.
        """
        return len(self.loans.get(user.username, []))

    def print_overdue_books(self):
        """
        Print overdue books (placeholder for overdue logic).
        """
        # Placeholder: Extend with due date logic if needed
        pass
