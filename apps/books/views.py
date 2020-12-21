import json
import requests

from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden, Http404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookshelf
from .forms import BookshelfForm

class BookshelfDetailView(LoginRequiredMixin, DetailView):
    model = Bookshelf
    template_name = "books/bookshelf_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404()
        return obj

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


def search_for_book(request):
    API_KEY = "AIzaSyDtKKU2Hr6HZJxZbzlUMjwZqtR7PT2qJ1c"
    title = request.GET.get("q").replace(" ", "+")
    res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title}+intitle&key={API_KEY}")
    return JsonResponse(res.json(), safe=False)