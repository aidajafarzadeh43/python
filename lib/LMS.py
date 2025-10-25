# class  Library:
#     def __init__(self,books):
#         self.books=books
#     def showbooks(self):
#      print("The available books in the library are: ")
#      for book in self.books:
#       print(" *" +book)   #This method is usually used to display lists to keep the code readable and tidy.
    
#     def trustBook(self,bookname):            
#         if bookname in self.books:
#            print(f"You have borrowed the {bookname}. Please keep it safe...")
#            self.books.remove(bookname)
#            return True
#         else:
#             print(f"Sorry! {bookname} book is either not available or already been issued to someone else...")
#             return False

#     def returnBook(self, bookname):
#         self.books.append(bookname)
#         print("Thanks for returning it. Hope you enjoy reading it")

#     def addbook(self,bookname):
#         self.books.append(bookname)
#         print("Thanks for donating the book to the library!!")

#     class student:
#      def requestbook(self):
#         self.book = input("Enter the name of the book: ")
#         return self.book
     
#      def returnbook(self):
#         self.book = input("Enter the name of the book you want to return: ")
#         return self.book

#     def addbook(self):
#         self.book = input("Enter the name of the book you want to add to the library: ")
#         return self.book

# if __name__ == "__main__":
#     centralLibrary = Library(["Algorithms", "Sherlock Holmes", "Django", "HTML Notes", "Python Notes", "C++ Notes", "Java Notes"])
#     student = Library_student()

#     msg = ''' 
# ### Welcome to the Central library of the university ###
# Please Enter the option:
# 1. List the names of all available books
# 2. Request to borrow a book
# 3. Return a book
# 4. Add a book to the library
# 5. Exit the Library
#     '''
#     print(msg)
#     while(True):
#         wlcMsg = '''
#         Please Enter the option : 
#         '''
#         print(wlcMsg)
#         a = int(input("How can I help you? : "))
#         if a == 1:
#             centralLibrary.displayBooks()
#         elif a == 2:
#             centralLibrary.borrowBooks(student.requestBook())
#         elif a == 3:
#             centralLibrary.returnBook(student.returnBook())
#         elif a == 4:
#             centralLibrary.addBook(student.addBook())
#         elif a == 5:
#             print("Thanks for using the Central Library!!")
#             exit()
#         else:
#             print("You entered an invalid choice.....")

class Library:
    def __init__(self, books):
        self.books = books

    def showbooks(self):
        print("The available books in the library are:")
        for book in self.books:
            print(" * " + book)

    def trustBook(self, bookname):
        if bookname in self.books:
            print(f"You have borrowed {bookname}. Please keep it safe...")
            self.books.remove(bookname)
            return True
        else:
            print(f"Sorry! {bookname} is not available or already borrowed.")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning it. Hope you enjoyed reading it.")

    def addbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for donating the book to the library!!")

    class student:
        def requestbook(self):
            self.book = input("Enter the name of the book: ")
            return self.book

        def returnbook(self):
            self.book = input("Enter the name of the book you want to return: ")
            return self.book

        def addbookrequest(self):
            self.book = input("Enter the name of the book you want to add to the library: ")
            return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Sherlock Holmes", "Django", "HTML Notes", "Python Notes", "C++ Notes", "Java Notes"])
    student = Library.student()

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
        a = int(input("\nHow can I help you? : "))
        if a == 1:
            centralLibrary.showbooks()
        elif a == 2:
            centralLibrary.trustBook(student.requestbook())
        elif a == 3:
            centralLibrary.returnBook(student.returnbook())
        elif a == 4:
            centralLibrary.addbook(student.addbookrequest())
        elif a == 5:
            print("Thanks for using the Central Library!!")
            break
        else:
            print("Invalid choice.")
