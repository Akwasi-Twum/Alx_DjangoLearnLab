from django.urls import path
from .views import BookList

["DefaultRouter()", "router.urls", "include"]
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
