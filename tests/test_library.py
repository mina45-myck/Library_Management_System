import pytest
from src.book import Book
from src.member import Member
from src.librarian import Librarian

def test_book_creation():
    book = Book('Python Basics', 'John Doe', '12345', 5)
    assert book.title == 'Python Basics'

def test_member_creation():
    member = Member('Minal', 20, 'P001', 'M001')
    assert member.name == 'Minal'
    assert member.membership_id == 'M001'

def test_librarian_creation():
    librarian = Librarian('Mr. Ali', 35, 'P002', 'L001')
    assert librarian.name == 'Mr. Ali'
    assert librarian.employee_id == 'L001'

def test_book_issue_status():
    book = Book('Python Basics', 'John Doe', '12345', 5)
    book.is_issued = True
    assert book.is_issued == True
