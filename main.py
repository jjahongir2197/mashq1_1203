# 1) Library Management System

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def info(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} | {self.author} | {self.year} | {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def show_books(self):
        for i, b in enumerate(self.books):
            print(i+1, b.info())

    def borrow_book(self, index):
        if self.books[index].borrow():
            print("Book borrowed")
        else:
            print("Book not available")

    def return_book(self, index):
        self.books[index].return_book()
        print("Book returned")


def run():
    lib = Library()

    lib.add_book("Python Basics", "Guido", 1991)
    lib.add_book("Data Structures", "Mark", 2005)
    lib.add_book("Algorithms", "CLRS", 2000)

    while True:
        print("\n1 Show Books")
        print("2 Borrow Book")
        print("3 Return Book")
        print("4 Exit")

        c = input()

        if c == "1":
            lib.show_books()

        elif c == "2":
            lib.show_books()
            i = int(input("Book: ")) - 1
            lib.borrow_book(i)

        elif c == "3":
            lib.show_books()
            i = int(input("Book: ")) - 1
            lib.return_book(i)

        else:
            break


run()
