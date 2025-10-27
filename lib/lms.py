# from database import create_database, add_book_to_db, show_books_from_db, borrow_book_from_db, return_book_to_db

# class Library:
#     def __init__(self):
#         create_database()

#     def add_book(self, title):
#         add_book_to_db(title)

#     def show_books(self):
#         show_books_from_db()

#     def borrow_book(self, bookname):
#         borrow_book_from_db(bookname)

#     def return_book(self, bookname):
#         return_book_to_db(bookname)

# class Student:
#     def request_book(self):
#         return input("Enter the name of the book: ")

# if __name__ == "__main__":
#     central_library = Library()
#     student = Student()

#     msg = ''' 
#     ### Welcome to the Central Library ###
#     1. List all available books
#     2. Request to borrow a book
#     3. Return a book
#     4. Add a book to the library
#     5. Exit
#     '''
#     print(msg)

#     while True:
#         choice = int(input("\nHow can I help you? : "))
#         if choice == 1:
#             central_library.show_books()
#         elif choice == 2:
#             book = student.request_book()
#             central_library.borrow_book(book)
#         elif choice == 3:
#             book = student.request_book()
#             central_library.return_book(book)
#         elif choice == 4:
#             book = student.request_book()
#             central_library.add_book(book)
#         elif choice == 5:
#             print("Thanks for using the Central Library!!")
#             break
#         else:
#             print("Invalid choice.")


from database import (
    create_database, add_user_to_db, login_user_from_db,
    add_book_to_db, show_books_from_db, borrow_book_from_db, return_book_to_db
)

class Library:
    def __init__(self, role):
        create_database()
        self.role = role

    def add_book(self, title):
        if self.role != 'admin':
            print("Only admin can add new books.")
            return
        add_book_to_db(title)
        print(f"Book '{title}' added.")

    def show_books(self):
        show_books_from_db()

    def borrow_book(self, bookname):
        if self.role not in ('admin', 'user'):
            print("Invalid role.")
            return
        borrow_book_from_db(bookname)

    def return_book(self, bookname):
        if self.role not in ('admin', 'user'):
            print("Invalid role.")
            return
        return_book_to_db(bookname)

class Student:
    def request_book(self):
        return input("Enter the name of the book: ")

if __name__ == "__main__":
    create_database()

    # اگر اولین اجرای برنامه است، یک ادمین اضافه کنید:
    # (در واقع برای راحتی، می‌تونید ادمین را از قبل اضافه کنید.)
    try:
        add_user_to_db('admin', 'adminpass', role='admin')
        print("Default admin created: username='admin', password='adminpass'")
    except Exception as e:
        # اگر یوزرنیم تکراری بود، بی‌توجه باش
        pass

    print("=== Welcome to the Central Library ===")
    username = input("Username: ")
    password = input("Password: ")
    role = login_user_from_db(username, password)

    if role is None:
        print(f"The username or password is incorrect.")
        exit()

    print(f"Welcome, you have entered with the role of{role}")

    central_library = Library(role)
    student = Student()

    while True:
        if role == 'admin':
            msg = '''
            1. List all books
            2. Borrow a book
            3. Return a book
            4. Add a book
            5. Exit
            '''
        else:  # کاربر عادی
            msg = '''
            1. List all books
            2. Borrow a book
            3. Return a book
            4. Exit
            '''

        print(msg)
        try:
            choice = int(input("How can I help you? : "))
        except ValueError:
            print("Please enter a number:")
            continue

        if choice == 1:
            central_library.show_books()
        elif choice == 2:
            book = student.request_book()
            central_library.borrow_book(book)
        elif choice == 3:
            book = student.request_book()
            central_library.return_book(book)
        elif role == 'admin' and choice == 4:
            book = student.request_book()
            central_library.add_book(book)
        elif (role == 'admin' and choice == 5) or (role != 'admin' and choice == 4):
            print("Thanks for using the Central Library!!")
          
            break
        else:
            print("Invalid choice.")