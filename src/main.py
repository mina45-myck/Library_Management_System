from book import Book
from librarian import Librarian
from member import Member

def main():
    print("=== LIBRARY MANAGEMENT SYSTEM ===\n")
    
    # 1. Librarian banao
    lib1 = Librarian("Minal", 20, "P001", "EMP101")
    print("Librarian Info:")
    lib1.display_info()
    print()
    
    # 2. Books banao
    book1 = Book("Python Basics", "John Doe", "ISBN123", 3)
    book2 = Book("OOP in Python", "Jane Smith", "ISBN456", 2)
    print("Books Added to Library:")
    book1.display_info()
    print()
    book2.display_info()
    print()
    
    # 3. Librarian books add kare
    lib1.add_book(book1.title)
    lib1.add_book(book2.title)
    print()
    
    # 4. Member banao
    member1 = Member("Ali", 22, "P002", "MEM101")
    print("Member Info:")
    member1.display_info()
    print()
    
    # 5. Member book borrow kare
    print("=== BORROWING PROCESS ===")
    member1.borrow_book(book1.title)
    book1.borrow_book()  # Copies kam karo
    print()
    
    # 6. Member book return kare
    print("=== RETURNING PROCESS ===")
    member1.return_book(book1.title)
    book1.return_book()  # Copies wapas badhao
    print()
    
    # 7. Final status
    print("=== FINAL STATUS ===")
    print(member1)
    print(book1)
    print("\n=== SYSTEM COMPLETE ===")

if __name__ == "__main__":
    main()