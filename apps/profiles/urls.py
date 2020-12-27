from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_for_user, name="search"),
    path('<str:username>/', views.bookium_user_profile, name="profile"),
    path('<str:username>/follow/', views.follow_user, name="follow"),
    path('<str:username>/unfollow/', views.unfollow_user, name="unfollow"),
    path('<str:username>/edit/', views.update_user_profile, name="edit_profile"),
]