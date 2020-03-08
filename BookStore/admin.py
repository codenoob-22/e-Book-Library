from django.contrib import admin
from .models import Post, Book


# class BookStoreAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'slug']
#
#     class Meta:
#         model = Book

admin.site.register(Post)
admin.site.register(Book)

