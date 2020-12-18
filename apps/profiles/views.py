from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def bookium_user_profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        "user": user,
    }

    return render(request, "profiles/bookium_profile.html", context=context)    