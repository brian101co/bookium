from django.db import models
from django.conf import settings

class BookshelfManager(models.Manager):
    def total_bookshelves(self):
        return self.get_queryset().count()


class Bookshelf(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookshelves", blank=True)

    objects = BookshelfManager()

    def __str__(self):
        return self.name

    def total_books(self):
        return self.books.count()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
