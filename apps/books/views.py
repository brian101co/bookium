import json
import requests


from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden, Http404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookshelf, Book
from .forms import BookshelfForm, BookForm

class BookshelfDetailView(LoginRequiredMixin, DetailView):
    model = Bookshelf
    template_name = "books/bookshelf_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404()
        return obj

@login_required
def create_book(request, bookshelf_id):
    if request.method == "POST":
        data = json.loads(request.body)
        form = BookForm(data)
        
        if form.is_valid():
            book = form.save(commit=False)
            book.bookshelf = get_object_or_404(Bookshelf, pk=bookshelf_id)
            book.save()
            data = {
                "success": True,
                "deleteURL": reverse("delete_book", kwargs={
                    "book_id": book.id
                }),
                "updateURL": reverse("edit_book", kwargs={
                    "book_id": book.id
                })
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"success": False, "msg": "Form Invalid"})

@login_required
def create_manual_book(request, bookshelf_id):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.bookshelf = get_object_or_404(Bookshelf, pk=bookshelf_id)
            book.save()
            data = {
                "success": True,
                "updateURL": reverse("edit_book", kwargs={
                    "book_id": book.id
                }),
                "deleteURL": reverse("delete_book", kwargs={
                    "book_id": book.id
                })
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"success":False, "msg":"form errors"})


@login_required
def create_bookshelf(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = BookshelfForm(data)
        
        if form.is_valid():
            bookshelf = form.save(commit=False)
            bookshelf.user = request.user
            bookshelf.save()
            data = {
                "success": True,
                "deleteURL": reverse("delete_bookshelf", kwargs={
                    "id": bookshelf.id,
                }),
                "detailURL": reverse("detail_bookshelf", kwargs={
                    "pk": bookshelf.id
                }),
                "id": bookshelf.id,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"invalid_form": form.errors})

@login_required
def delete_bookshelf(request, id):
    if request.method == "DELETE":
        bookshelf = get_object_or_404(Bookshelf, pk=id)
        if bookshelf.user == request.user:
            bookshelf.delete()
            return JsonResponse({"success": True})
        else:
            return HttpResponseForbidden()


@login_required
def delete_book(request, book_id):
    if request.method == "DELETE":
        book = get_object_or_404(Book, pk=book_id)
        if book.bookshelf.user == request.user:
            book.delete()
            return JsonResponse({"success": True})
        else:
            return HttpResponseForbidden()


@login_required
def edit_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=book_id)
        if book.bookshelf.user == request.user:
            fields = []
            for key in request.POST:
                fields.append(key)

            Form = modelform_factory(
                Book, form=BookForm, fields=fields
            )
            form = Form(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True, "redirect": reverse("detail_bookshelf", kwargs={
                    "pk": book.bookshelf.id,
                })})
            else:
                print(form.errors)
                return JsonResponse({"success": False})
        else:
            return HttpResponseForbidden()


def search_for_book(request):
    API_KEY = "AIzaSyDtKKU2Hr6HZJxZbzlUMjwZqtR7PT2qJ1c"
    title = request.GET.get("q").replace(" ", "+")
    res = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title}+intitle&key={API_KEY}")
    return JsonResponse(res.json(), safe=False)