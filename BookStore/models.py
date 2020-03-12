from django.db import models
from django.db.models.signals import pre_save
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from simple_history.models import HistoricalRecords

from .utils import unique_slug_generator


class Post(models.Model):
    title = models.TextField()
    img = models.ImageField()
    content = models.TextField()


# def get_absolute_url(self):
#     """Returns the URL of the book for details"""
#     return reverse('book_details', args=[str(self.id)])


CATEGORY_CHOICES = (
    ('textbook', 'Text book'),
    ('poetry', 'Poetry'),
    ('story', 'Story'),
    ('novel', 'Novel'),
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-fiction'),
    ('other', 'Other'),
)
LANGUAGE_CHOICES = (
    ('hindi', 'Hindi'),
    ('english', 'English'),
    ('other', 'Other'),
)


class Book(models.Model):
    book_title = models.TextField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    book_sub_title = models.TextField(max_length=100, blank=True, null=True)
    isbn_number = models.TextField(max_length=25, blank=True, null=True)
    book_language = models.CharField(max_length=40, default='hindi', choices=LANGUAGE_CHOICES)
    about_book = models.TextField(max_length=500, blank=True, null=True)
    book_category = models.CharField(max_length=40, default='other', choices=CATEGORY_CHOICES)
    book_cover = models.ImageField(upload_to='books_cover')
    book_content = models.FileField(upload_to='books_pdf')
    author_name = models.TextField(max_length=100)
    about_author = models.TextField(max_length=500, blank=True, null=True)
    book_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    book_cover_thumbnail = ImageSpecField(source='book_cover', processors=[ResizeToFill(500, 750)], format='JPEG',
                                          options={'quality': 60})
    history = HistoricalRecords()

    def __str__(self):
        return self.book_title

    def __unicode__(self):
        return self.book_title


def book_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(book_pre_save_receiver, sender=Book)
