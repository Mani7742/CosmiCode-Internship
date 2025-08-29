# Create a program to manage a library system using
#  classes, including methods for adding, removing, and displaying
#  books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)


if __name__ == "__main__":
    library = Library()
    book1 = Book("Pakistan Studies", "Punjab Text Book Board")
    book2 = Book("Mr. Chips", "James Hilton")

    library.add_book(book1)
    library.add_book(book2)

    print("Books in the library:")
    library.display_books()

    library.remove_book(book1)
    print("\nBooks in the library after removal:")
    library.display_books()