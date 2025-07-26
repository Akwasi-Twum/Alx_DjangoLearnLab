from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    # Add filters for publication year and author
    list_filter = ('publication_year', 'author')
    # Enable searching by title and author
    search_fields = ('title', 'author')
["admin.site.register(CustomUser, CustomUserAdmin)"]
admin.site.register(Book, BookAdmin)
