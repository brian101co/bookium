from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def feed(request):

    user_ids = [request.user.id]

    # Grab Followers
    for user_profile in request.user.profile.follows.all():
        user_ids.append(user_profile.user.id)

    posts = Post.objects.filter(created_by__id__in=user_ids)
    return render(request, 'feed/feed.html', {"posts":posts})
