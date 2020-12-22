from django.urls import path
from .views import create_bookshelf, delete_bookshelf, BookshelfDetailView, search_for_book, create_book, delete_book

urlpatterns = [
    path("bookshelf/create/", create_bookshelf, name="create_bookshelf"),
    path("bookshelf/delete/<int:id>", delete_bookshelf, name="delete_bookshelf"),
    path("bookshelf/<int:pk>/", BookshelfDetailView.as_view(), name="detail_bookshelf"),
    path("books/search/", search_for_book, name="search_book"),
    path("books/create/<int:bookshelf_id>", create_book, name="create_book"),
    path("books/delete/<int:book_id>", delete_book, name="delete_book"),
]