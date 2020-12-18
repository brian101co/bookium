from django.shortcuts import render, get_object_or_404
from django.conf import settings

def bookium_user_profile(request, username):
    user = get_object_or_404(settings.AUTH_USER_MODEL, username=username)

    context = {
        "user": user,
    }

    return render(request, "profiles/bookium_profile.html", context=context)    