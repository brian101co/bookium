from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from apps.books.forms import BookshelfForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile

@login_required
def bookium_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    form = BookshelfForm()
    following = False
    if user.profile in request.user.profile.follows.all():
        following = True
   
    context = {
        "user": user,
        "form": form,
        "following": following,
    }

    return render(request, "profiles/bookium_profile.html", context=context)  

@login_required
def search_for_user(request):
    query = request.GET.get("q")
    users = User.objects.filter(username__icontains=query)
    return render(request, "profiles/search_profile.html", {"users": users})

@login_required
def follow_user(request, username):
    user = get_object_or_404(User, username=username)
    request.user.profile.follows.add(user.profile)
    return JsonResponse({"success": True})

@login_required
def unfollow_user(request, username):
    user = get_object_or_404(User, username=username)
    request.user.profile.follows.remove(user.profile)
    return JsonResponse({"success": True})
