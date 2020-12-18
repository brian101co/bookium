from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.bookium_user_profile, name="profile"),
]