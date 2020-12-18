import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..feed.models import Post

@login_required
def api_add_post(request):
    data = json.loads(request.body)
    body = data["body"]

    post = Post.objects.create(body=body, created_by=request.user)
    return JsonResponse({"success": True})

