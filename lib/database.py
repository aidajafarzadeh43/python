
# import sqlite3

# def create_database():
#     conn = sqlite3.connect('info.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         status TEXT NOT NULL CHECK(status IN ('available', 'borrowed'))
#     )
#     ''')

#     conn.commit()
#     conn.close()

# def add_book_to_db(title):
#     conn = sqlite3.connect('info.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     INSERT INTO books (title, status) VALUES (?, ?)
#     ''', (title, 'available'))

#     conn.commit()
#     conn.close()

# def show_books_from_db():
#     conn = sqlite3.connect('info.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT title, status FROM books')
#     books = cursor.fetchall()

#     for book in books:
#         print(f" * {book[0]} ({book[1]})")

#     conn.close()

# def borrow_book_from_db(bookname):
#     conn = sqlite3.connect('info.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     UPDATE books SET status = ? WHERE title = ? AND status = ?
#     ''', ('borrowed', bookname, 'available'))

#     if cursor.rowcount > 0:
#         print(f"You have borrowed '{bookname}'. Please keep it safe...")
#     else:
#         print(f"Sorry! '{bookname}' is not available or already borrowed.")

#     conn.commit()
#     conn.close()

# def return_book_to_db(bookname):
#     conn = sqlite3.connect('info.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     UPDATE books SET status = ? WHERE title = ? AND status = ?
#     ''', ('available', bookname, 'borrowed'))

#     if cursor.rowcount > 0:
#         print(f"Thanks for returning '{bookname}'. Hope you enjoyed reading it.")
#     else:
#         print(f"Sorry! '{bookname}' was not borrowed or does not exist.")

#     conn.commit()
#     conn.close()

import sqlite3

def create_database():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    # جدول کاربران
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin','user'))
    )
    ''')

    # جدول کتاب‌ها
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('available', 'borrowed'))
    )
    ''')

    conn.commit()
    conn.close()

def add_user_to_db(username, password, role='user'):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('''
      INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)
    ''', (username, password, role))

    conn.commit()
    conn.close()


# افزودن کاربر ادمین
add_user_to_db('admin1', '11', 'admin')

# افزودن کاربر عادی
add_user_to_db('22', '22', 'user')

def login_user_from_db(username, password):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('''
      SELECT role FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
       return None

def add_book_to_db(title):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO books (title, status) VALUES (?, ?)
    ''', (title, 'available'))

    conn.commit()
    conn.close()

def show_books_from_db():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, status FROM books')
    books = cursor.fetchall()

    for book in books:
        print(f" * {book[0]} ({book[1]})")

    conn.close()

def borrow_book_from_db(bookname):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE books SET status = ? WHERE title = ? AND status = ?
    ''', ('borrowed', bookname, 'available'))

    if cursor.rowcount > 0:
        print(f"You have borrowed '{bookname}'. Please keep it safe...")
    else:
        print(f"Sorry! '{bookname}' is not available or already borrowed.")

    conn.commit()
    conn.close()

def return_book_to_db(bookname):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE books SET status = ? WHERE title = ? AND status = ?
    ''', ('available', bookname, 'borrowed'))

    if cursor.rowcount > 0:
        print(f"Thanks for returning '{bookname}'. Hope you enjoyed reading it.")
    else:
        print(f"Sorry! '{bookname}' was not borrowed or does not exist.")

    conn.commit()
    conn.close()



