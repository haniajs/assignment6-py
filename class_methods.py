class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

book1 = Book("Jannat kay pattay", "Nimra Ahamed")
book2 = Book("Rooh-e-yaram", "Areej Shah")
book3 = Book("Namal", "Nimra Ahmed")

print("Total number of books:", Book.get_total_books())
