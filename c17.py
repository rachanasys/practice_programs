#write a python program To Implement Class Methods
class Book:
    total_books = 0
    def __init__(self):
        Book.increment_count()
    @classmethod
    def increment_count(cls):
        cls.total_books += 1  # Modifying class variable
b1 = Book()
b2 = Book()
print(f"Total books created: {Book.total_books}")
