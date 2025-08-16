from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create sample books
        self.book1 = Book.objects.create(title="Django Unleashed", author="Andrew Pinkham", published_date="2016-01-01", isbn="1234567890123")
        self.book2 = Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", published_date="2018-05-15", isbn="9876543210987")

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "Test Driven Django",
            "author": "Akwasi Twum",
            "published_date": "2022-10-11",
            "isbn": "1357913579135"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            "title": "Django Unleashed - Updated",
            "author": "Andrew Pinkham",
            "published_date": "2016-01-01",
            "isbn": "1234567890123"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'])

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_filter_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Andrew Pinkham'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertEqual(book['author'], 'Andrew Pinkham')

    def test_search_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Two Scoops'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Two Scoops of Django' in book['title'] for book in response.data))

    def test_order_books_by_published_date(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'published_date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dates = [book['published_date'] for book in response.data]
        self.assertEqual(dates, sorted(dates))

    def test_permission_required(self):
        # Logout first
        self.client.logout()
        url = reverse('book-list')
        response = self.client.post(url, {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "published_date": "2023-01-01",
            "isbn": "0000000000000"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

"""
Testing Documentation:

Testing Strategy:
- These unit tests simulate API requests using Django REST Framework's APITestCase.
- CRUD operations (Create, Read/List, Update, Delete) are covered.
- Filtering, searching, and ordering functionalities are verified.
- Permission and authentication checks ensure access control works as intended.

How to Run Tests:
- From your project root, run:
    python manage.py test api

Interpreting Results:
- All tests should pass (OK) with accurate status codes.
- Failures indicate either API view logic or permissions issues.

Test Cases:
- test_create_book: Verifies book creation works and returns correct data.
- test_update_book: Checks book update is persisted.
- test_delete_book: Asserts book is removed.
- test_list_books: Ensures book list endpoint works.
- test_filter_books_by_author: Confirms filtering by author works.
- test_search_books_by_title: Confirms search endpoint is functional.
- test_order_books_by_published_date: Checks ordering by date.
- test_permission_required: Verifies that unauthenticated users cannot create books.
"""