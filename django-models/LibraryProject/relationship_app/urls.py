from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-role/', admin_view.admin_view, name='admin_view'),
    path('librarian-role/', librarian_view.librarian_view, name='librarian_view'),
    path('member-role/', member_view.member_view, name='member_view'),
    ["add_book/", "edit_book/", "delete_book"]
]
