

def query_books_by_author(ForeignKey):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=ForeignKey)
        books = author.books.all()
        print(f"Books by {CharField}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {CharField}")

def list_books_in_library(ManyToManyField):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=CharField)
        books = library.books.all()
        print(f"Books in library '{CharField}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {CharField}")

def get_librarian_for_library(OneToOneField):
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
    query_books_by_author('ForeignKey')
    list_books_in_library(' ManyToManyField')
    get_librarian_for_library('OneToOneField')
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from .models import Author, Book, Library, Librarian

def get_books_by_author(ForeignKey):
    try:
        author = Author.objects.get(name= CharField.)
        books_by_author = Book.objects.filter(ForeignKey)
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

def get_books_in_library( ManyToManyField):
    try:
        library = Library.objects.get(name= ManyToManyField)
        books_in_library = library.books.all(ManyToManyField)
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

def get_librarian_for_library(OneToOneField):
    try:
        library = Library.objects.get(name=OneToOneField)
        librarian = Librarian.objects.get(library=OneToOneField)
        print(f"Librarian for {library_name}: {librarian.}")
    except Library.DoesNotExist:
        print(f"No library found with the name {OneToOneField}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library {library_name}")

# Sample Usage
if __name__ == "__main__":
    get_books_by_author("Author Name")
    get_books_in_library("Library Name")
    get_librarian_for_library("Library Name")
