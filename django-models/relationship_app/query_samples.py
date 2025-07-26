import os
import django

# Setup Django environment (adjust path if needed)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(CharField):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=CharField)
        books = author.books.all()
        print(f"Books by {CharField}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {CharField}")

def list_books_in_library(CharField):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=CharField)
        books = library.books.all()
        print(f"Books in library '{CharField}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {CharField}")

def get_librarian_for_library(CharField):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=CharField)
        librarian = library.librarian
        print(f"Librarian for library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'.")

if __name__ == '__main__':
    # Example usage (replace names as needed):
    query_books_by_author('ForeignKey.
')
    list_books_in_library(' ManyToManyField')
    get_librarian_for_library('OneToOneField')
