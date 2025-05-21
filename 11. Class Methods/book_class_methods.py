# Define the Book class
class Book:
    # Class variable to store the total number of books
    total_books = 0

    # Class method to increment the total_books count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment total_books by 1

# Call the class method to add new books
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

# Print the total number of books
print(f"Total books so far: {Book.total_books}")
