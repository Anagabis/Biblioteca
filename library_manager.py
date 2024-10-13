class LibraryManager:
    def __init__(self):

        pass

class CLI:
    def __init__(self, library_manager):
        self.library_manager = library_manager

library_manager = LibraryManager()

cli = library_manager

from persistence.book_repository import BookRepository

class LibraryManager:
    def __init__(self):
        self.repository = BookRepository()

    def add_book(self, title, author):
        self.repository.add_book(title, author)

    def list_books(self):
        return self.repository.get_books()

    def delete_book(self, title):
        self.repository.delete_book(title)
