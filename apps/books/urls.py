from django.urls import path
from .views import create_bookshelf

urlpatterns = [
    path("create_shelf/", create_bookshelf, name="create_bookshelf"),
]