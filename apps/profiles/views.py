from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from apps.books.forms import BookshelfForm

def bookium_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    form = BookshelfForm()

    context = {
        "user": user,
        "form": form,
    }

    return render(request, "profiles/bookium_profile.html", context=context)    