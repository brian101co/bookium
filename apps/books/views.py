import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView
from .models import Bookshelf
from .forms import BookshelfForm

@login_required
def create_bookshelf(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = BookshelfForm(data)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"invalid_form": form.errors})
    