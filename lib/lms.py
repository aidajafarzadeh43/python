from database import create_database, add_book_to_db, show_books_from_db, borrow_book_from_db, return_book_to_db

class Library:
    def __init__(self):
        create_database()

    def add_book(self, title):
        add_book_to_db(title)

    def show_books(self):
        show_books_from_db()

    def borrow_book(self, bookname):
        borrow_book_from_db(bookname)

    def return_book(self, bookname):
        return_book_to_db(bookname)

class Student:
    def request_book(self):
        return input("Enter the name of the book: ")

if __name__ == "__main__":
    central_library = Library()
    student = Student()

    msg = ''' 
    ### Welcome to the Central Library ###
    1. List all available books
    2. Request to borrow a book
    3. Return a book
    4. Add a book to the library
    5. Exit
    '''
    print(msg)

    while True:
        choice = int(input("\nHow can I help you? : "))
        if choice == 1:
            central_library.show_books()
        elif choice == 2:
            book = student.request_book()
            central_library.borrow_book(book)
        elif choice == 3:
            book = student.request_book()
            central_library.return_book(book)
        elif choice == 4:
            book = student.request_book()
            central_library.add_book(book)
        elif choice == 5:
            print("Thanks for using the Central Library!!")
            break
        else:
            print("Invalid choice.")