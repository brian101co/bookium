from django import forms
from .models import Bookshelf, Book

class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        exclude = ('user',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('bookshelf',)