from person import Person

class Member(Person):
    """
    Member class inherits from Person.
    Adds membership_id and methods to borrow/return books.
    """
    def __init__(self, name, age, person_id, membership_id):
        # Person class ka constructor call karo
        super().__init__(name, age, person_id)
        self.membership_id = membership_id
        self.borrowed_books = []  # Empty list shuru me

    def display_info(self):
        """Override Person's method to add membership info"""
        super().display_info()  # Person wala info print karo
        print(f"Membership ID: {self.membership_id}")
        print(f"Books Borrowed: {len(self.borrowed_books)}")

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f"Member {self.name} borrowed book: {book_title}")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"Member {self.name} returned book: {book_title}")
        else:
            print(f"{book_title} not found in borrowed books")

    def __str__(self):
        return f"Member(Name: {self.name}, Membership ID: {self.membership_id})"