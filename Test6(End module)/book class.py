"""Create user choise for
*add new book
*update book data
*Delete book
* show specific data (you have to show perticular data using regular expression like only name or author 
 or price according to user choice.)
*show whole data
(use class,constructor,use pickling to store data in file.)"""
import pickle
import re

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = input("Enter book price: ")
    b = Book(name, author, price)

    try:
        with open("books.dat", "rb") as f:
            books = pickle.load(f)
    except:
        books = []

    books.append(b)
    with open("books.dat", "wb") as f:
        pickle.dump(books, f)
    print("Book added successfully!")

def show_all():
    try:
        with open("books.dat", "rb") as f:
            books = pickle.load(f)
        for i, b in enumerate(books):
            print(f"\nBook {i+1}:")
            print(f"Name: {b.name}, Author: {b.author}, Price: {b.price}")
    except:
        print("No data found!")

def update_book():
    show_all()
    name = input("\nEnter book name to update: ")
    try:
        with open("books.dat", "rb") as f:
            books = pickle.load(f)

        found = False
        for b in books:
            if b.name.lower() == name.lower():
                b.author = input("Enter new author: ")
                b.price = input("Enter new price: ")
                found = True
                break

        if found:
            with open("books.dat", "wb") as f:
                pickle.dump(books, f)
            print("Book updated successfully!")
        else:
            print("Book not found.")
    except:
        print("No data found!")

def delete_book():
    show_all()
    name = input("\nEnter book name to delete: ")
    try:
        with open("books.dat", "rb") as f:
            books = pickle.load(f)

        new_books = [b for b in books if b.name.lower() != name.lower()]

        with open("books.dat", "wb") as f:
            pickle.dump(new_books, f)
        print("Book deleted successfully!")
    except:
        print("No data found!")

def show_specific():
    try:
        with open("books.dat", "rb") as f:
            books = pickle.load(f)

        choice = input("Show (name / author / price): ").lower()

        for b in books:
            if re.search("name", choice):
                print("Book Name:", b.name)
            elif re.search("author", choice):
                print("Author:", b.author)
            elif re.search("price", choice):
                print("Price:", b.price)
            else:
                print("Invalid choice!")
                break
    except:
        print("No data found!")

# ---------- Main Menu ----------

while True:
    print("\n----- Book Management System -----")
    print("1. Add New Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Show Specific Data")
    print("5. Show All Data")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        add_book()
    elif ch == '2':
        update_book()
    elif ch == '3':
        delete_book()
    elif ch == '4':
        show_specific()
    elif ch == '5':
        show_all()
    elif ch == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
