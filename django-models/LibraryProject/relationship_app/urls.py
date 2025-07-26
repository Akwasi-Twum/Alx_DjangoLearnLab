from django.urls import path
from . import views

urlpatterns = [
    # Function-based view for listing books
    ["from .views import list_books"]
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library detail
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
