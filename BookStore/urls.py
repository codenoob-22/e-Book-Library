from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views

app_name = 'BookStore'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('library/', views.library, name='library'),
    path('blog/', views.blog, name='blog'),
    path('book-reader/<slug>/', views.BookReaderSlugView.as_view(), name='BookReaderSlugView'),
    path('bookreader/book-id=<slug:book_id>/', views.bookreader, name='bookreader'),
    # path('book_details/book-id=<slug:book_id>/', views.book_details, name='book_details'),
    path('book-details/<slug>/', views.BookDetailSlugView.as_view(), name='BookDetailSlugView'),
    path('search-results/', views.search, name='search'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
