class Person:
    """
    Base class for all people in the Library Management System.
    This will be inherited by Librarian and Member classes.
    """
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id

    def display_info(self):
        """Display basic info of the person"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")

    def __str__(self):
        return f"Person(Name: {self.name}, ID: {self.person_id})"
    