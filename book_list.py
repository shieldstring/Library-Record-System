from book import Book

class BookList:
    def __init__(self):
        """
        Initialize the BookList with an empty dictionary.
        """
        self.books = {}

    def add_book(self, book):
        """
        Add a book object to the collection using its title as the key.
        """
        if book.title in self.books:
            raise ValueError("A book with this title already exists.")
        self.books[book.title] = book

    def search_book(self, key, value):
        """
        Search for a book by title, author, publisher, or publication date.
        """
        for book in self.books.values():
            if getattr(book, key, None) == value:
                return book
        return None

    def remove_book(self, title):
        """
        Remove a book by title.
        """
        if title in self.books:
            del self.books[title]
        else:
            raise ValueError("Book not found.")

    def total_books(self):
        """
        Return the total number of books in the collection.
        """
        return len(self.books)
