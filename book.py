import uuid

class Book:
    def __init__(self, title, author, year, publisher, num_copies, publication_date):
        """
        Initialize a Book instance with attributes.
        """
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.num_copies = num_copies
        self.available_copies = num_copies
        self.publication_date = publication_date

    # Setters
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_num_copies(self, num_copies):
        if num_copies >= 0:
            self.num_copies = num_copies
            self.available_copies = num_copies
        else:
            raise ValueError("Number of copies cannot be negative.")

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    # Getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_num_copies(self):
        return self.num_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date
