from .person import Person
class Librarian(Person):
    """
    Librarian class inherits from Person.
    Adds employee_id and methods to manage books.
    """
    def __init__(self, name, age, person_id, employee_id):
        # Person class ka constructor call karo
        super().__init__(name, age, person_id)
        self.employee_id = employee_id

    def display_info(self):
        """Override Person's method to add employee info"""
        super().display_info()  # Person wala info print karo
        print(f"Employee ID: {self.employee_id}")
        print(f"Role: Librarian")

    def add_book(self, book_title):
        print(f"Librarian {self.name} added book: {book_title}")

    def __str__(self):
        return f"Librarian(Name: {self.name}, Employee ID: {self.employee_id})"