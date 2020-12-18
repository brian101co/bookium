from django.urls import path
from .views import feed
from .api import api_add_post

urlpatterns = [
    path('', feed, name='feed'),
    path('api/add_post/', api_add_post, name="add_post"),
]