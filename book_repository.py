import json

class BookRepository:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file)

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        self.save_books()

    def get_books(self):
        return self.books

    def delete_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]
        self.save_books()
