class Book:
    total_books = 0 

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.total_books += 1

    def update_title(self, new_title):
        self.title = new_title

    def update_author(self, new_author):
        self.author = new_author

    def display_info(self, user_type="reader"):
        if user_type == "librarian":
            print(f"[Librarian View] Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
        else:
            print(f"Title: {self.title}, Author: {self.author}")

    @staticmethod
    def book_info():
        print("Books have a title, author, and ISBN to identify them in the library system.")

    @classmethod
    def get_total_books(cls):
        return cls.total_books


class Author:
    total_authors = 0

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.books = [] 
        Author.total_authors += 1

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    @staticmethod
    def author_info():
        print("Authors write books and are identified by their name and birthdate.")

    @classmethod
    def get_total_authors(cls):
        return cls.total_authors


class Library:
    library_count = 0 

    def __init__(self):
        self.books = []    
        self.authors = []  
        Library.library_count += 1

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()

    def add_author(self, author):
        if isinstance(author, Author):
            self.authors.append(author)

    @staticmethod
    def library_info():
        print("Libraries store books and manage operations related to books and authors.")

    @classmethod
    def get_library_count(cls):
        return cls.library_count

author1 = Author("R.K. Narayan", "10-Oct-1906")
author2 = Author("J.K. Rowling", "31-Jul-1965")

book1 = Book("Malgudi Days", "R.K. Narayan", "ISBN001")
book2 = Book("Harry Potter", "J.K. Rowling", "ISBN002")
book3 = Book("The Guide", "R.K. Narayan", "ISBN003")

author1.add_book(book1)
author1.add_book(book3)
author2.add_book(book2)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_author(author1)
library.add_author(author2)

print("\n Listing Books in Library ")
library.list_books()

print("\n Display Info as Librarian ")
book1.display_info("librarian")
library.remove_book("ISBN003")

print("\n Listing Books After Removal ")
library.list_books()

print("\n Static Info ")
Book.book_info()
Author.author_info()
Library.library_info()

print("\n Class Counts ")
print(f"Total Books: {Book.get_total_books()}")
print(f"Total Authors: {Author.get_total_authors()}")
print(f"Total Libraries: {Library.get_library_count()}")
