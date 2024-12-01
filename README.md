##Library Record System

A Python-based library management system designed to track books, users, and loans using Object-Oriented Programming principles. The system supports adding, managing, and interacting with books and users, and handles book borrowing and returning.

Features

- Book Management: Add, remove, and search for books in the library collection.
- User Management: Register users, manage their information, and track their borrowing history.
- Loan Management: Handle book borrowing and returning processes, including tracking overdue books.
- Error Handling: Comprehensive validation ensures data integrity.
- Interactive CLI (Optional): Modify user and book details through a simple command-line interface.

Project Structure

library-record-system/

│

├── main.py # Entry point for the application

├── book.py # Book class with methods to manage book details

├── book_list.py # BookList class to handle collections of books

├── user.py # User class for managing user data

├── user_list.py # UserList class to handle user collections

└── loan.py # Loan class to manage book loans

Dependencies

    Python 3.8+
    No external libraries required.

Installation

    Clone the Repository:

git clone https://github.com/your-username/library-record-system.git
cd library-record-system

Run the Application:

    python main.py

    Ensure you have the necessary Python version installed.

Usage Guide

1. Managing Books:

   Add a Book:

book_list.add_book(Book(title="1984", author="George Orwell", year=1949, publisher="Secker & Warburg", num_copies=5))

Search for a Book:

    book = book_list.search_book("1984")

2. Managing Users:

   Add a User:

user_list.add_user(User(username="jdoe", firstname="John", surname="Doe", email="johndoe@example.com"))

Get User Details:

    user = user_list.get_user_details("jdoe")

3. Managing Loans:

   Borrow a Book:

loan.borrow_book(username="jdoe", book_title="1984")

Return a Book:

    loan.return_book(username="jdoe", book_title="1984")

Testing

    Manual Testing:
        Run main.py and interact with the system via the terminal.
        Verify outputs for each functionality (adding/removing books, loan management).

    Automated Testing:
        Create unit tests using Python’s unittest module.
        Example:

        import unittest
        from book import Book

        class TestBookMethods(unittest.TestCase):
            def test_book_creation(self):
                book = Book("Test Title", "Test Author", 2020, "Test Publisher", 3)
                self.assertEqual(book.get_title(), "Test Title")

        if __name__ == "__main__":
            unittest.main()
