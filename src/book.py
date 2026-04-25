class Book:
    """
    Book class to store book information.
    Tracks availability status for borrowing/returning.
    """
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies  # Shuru me sab available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available: {self.available_copies}/{self.total_copies}")

    def borrow_book(self):
        """Decrease available copies if book is available"""
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book borrowed: {self.title}")
            return True
        else:
            print(f"Sorry, {self.title} is not available")
            return False

    def return_book(self):
        """Increase available copies"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"Book returned: {self.title}")
        else:
            print("All copies already in library")

    def __str__(self):
        return f"Book(Title: {self.title}, Available: {self.available_copies})"