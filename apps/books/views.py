import json

from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
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
            print(obj.id)
            data = {
                "success": True,
                "deleteURL": reverse("delete_bookshelf", kwargs={
                    "id": obj.id,
                }),
                "id": obj.id,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"invalid_form": form.errors})

@login_required
def delete_bookshelf(request, id):
    if request.method == "DELETE":
        print(id)
        bookshelf = get_object_or_404(Bookshelf, pk=id)
        if bookshelf.user == request.user:
            bookshelf.delete()
            return JsonResponse({"success": True})
        else:
            return HttpResponseForbidden()
       