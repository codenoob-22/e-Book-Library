from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.TextField()
    img = models.ImageField()
    content = models.TextField()


def get_absolute_url(self):
    """Returns the URL of the book for details"""
    return reverse('book_details', args=[str(self.id)])


class Book(models.Model):
    book_title = models.TextField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    author_name = models.TextField(max_length=100)
    book_cover = models.ImageField(upload_to='books_cover')
    book_content = models.FileField(upload_to='books_pdf')
    book_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)




