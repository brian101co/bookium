from django.urls import path
from .views import create_bookshelf, delete_bookshelf

urlpatterns = [
    path("create_shelf/", create_bookshelf, name="create_bookshelf"),
    path("delete_shelf/<int:id>", delete_bookshelf, name="delete_bookshelf"),
]