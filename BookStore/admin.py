from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Post, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Book


admin.site.register(Post)
admin.site.register(Book, BookAdmin)
