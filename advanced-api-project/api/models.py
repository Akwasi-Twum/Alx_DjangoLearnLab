from django.db import models

# Author model: Represents a book author.
# Fields:
#   - name: Stores the author's name as a string.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model: Represents a book written by an author.
# Fields:
#   - title: The title of the book.
#   - publication_year: The year the book was published.
#   - author: ForeignKey linking to Author, establishing a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"