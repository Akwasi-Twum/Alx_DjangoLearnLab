from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer: Serializes all fields of the Book model.
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer: Serializes the author's name and their books.
# Uses a nested BookSerializer for the books relationship.
# This demonstrates how to serialize nested relationships in DRF.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    # The relationship between Author and Book is handled via the 'books' related_name in the Book model.
    # This serializer will include a list of serialized Book objects for each author.