from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from apps.books.forms import BookshelfForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile
from apps.books.models import Bookshelf
from .forms import ProfileForm

@login_required
def update_user_profile(request, username):
    if request.method == "POST":
        user = get_object_or_404(User, username=username)
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = ProfileForm()
        return render(request, 'profiles/edit_profile.html', {"form":form})

@login_required
def bookium_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    form = BookshelfForm()
    following = False
    if user.profile in request.user.profile.follows.all():
        following = True
    
    if user == request.user:
        bookshelves = Bookshelf.objects.filter(user=user)
    else:
        bookshelves = Bookshelf.objects.public_shelves()

    context = {
        "user": user,
        "form": form,
        "following": following,
        "shelves": bookshelves,
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
