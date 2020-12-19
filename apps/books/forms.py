from django import forms
from .models import Bookshelf

class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        exclude = ('user',)
