from django.urls import path
from .views import create_bookshelf, delete_bookshelf, BookshelfDetailView, search_for_book, create_book

urlpatterns = [
    path("create_shelf/", create_bookshelf, name="create_bookshelf"),
    path("search/", search_for_book, name="search_book"),
    path("create_book/<int:bookshelf_id>", create_book, name="create_book"),
    path("delete_shelf/<int:id>", delete_bookshelf, name="delete_bookshelf"),
    path("<int:pk>/", BookshelfDetailView.as_view(), name="detail_bookshelf"),
]