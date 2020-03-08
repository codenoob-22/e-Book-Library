from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView

from carts.models import Cart
from .models import Post, Book


def index(request):
    books = Book.objects.all()
    latest_books = Book.objects.filter().order_by('-author_name')
    return render(request, 'BookStore/storepage.html', {'latest_books': latest_books, 'books': books})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def add(request):
    n1 = request.POST['n1']
    n2 = request.POST['n2']
    res = int(n1) + int(n2)
    return render(request, 'base.html', {'result': res})


def library(request):
    books = Book.objects.all()
    latest_books = Book.objects.filter().order_by('-book_title')
    return render(request, 'BookStore/storepage.html', {'latest_books': latest_books, 'books': books})


@login_required()
def bookreader(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'BookStore/bookreader.html', {'book': book})


# class BookDetailSlugView(DetailView):
#     queryset = Book.objects.all()
#     template_name = 'BookStore/book_details.html'
#
#     def get_object(self, *args, **kwargs):
#         request= self.request
#         slug= self.kwargs.get('slug')
#         #instance = Book.objects.get_by_id(pk)
#         try:
#             instance = Book.objects.get(slug=slug, active=True)
#         except Book.DoesNotExist:
#             raise Http404(" Not Found")
#         except Book.MultipleObjectsReturned:
#             qs=Book.objects.get(slug=slug, active=True)
#             instance = qs.first()
#         except:
#             raise Http404("Book doesn't exist")
#         return instance
#


def book_details(request, book_id):
    book_detail = Book.objects.get(id=book_id)
    return render(request, 'BookStore/book_details.html', {'book': book_detail})


def search(request):
    search_value = request.GET.get('search_value')
    results = Book.objects.filter(Q(book_title__icontains=search_value) | Q(author_name__icontains=search_value))
    context = {'results': results}
    return render(request, 'BookStore/search_results.html', context)

# class BookDetailSlugView(DetailView):
#     queryset = Book.objects.all()
#     template_name = 'BookStore/book_details.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(BookDetailSlugView,self.get_context_data(*args,**kwargs)
#
#     def get_object(self,  *args, **kwargs):
#         request =self.request
#         slug = self.kwargs.get('slug')
#         try:
#             instance = Book.objects.get(slug=slug, active =True)
#         except Book.DoesNotExist:
#             raise Http404("Book not found")
#         except Book.MultipleObjectReturnd:
#             qs =Book.objects.filter(slug=slug, active =True)
#             instance = qs.first()
#         except
#             raise Http404("Ohhhh")
#         return instance
