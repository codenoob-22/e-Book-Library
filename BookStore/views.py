from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post, Book


def index(request):
    books = Book.objects.all()[:6]
    latest_books = Book.objects.filter().order_by('-author_name')[:6]

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
    books=books[1:6]
    latest_books = Book.objects.filter().order_by('-book_title')
    return render(request, 'BookStore/storepage.html', {'latest_books': latest_books, 'books': books})


class BookReaderSlugView(DetailView):
    model = Book
    template_name = "BookStore/bookreader.html"


@login_required()
def bookreader(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'BookStore/bookreader.html', {'book': book})


class BookDetailSlugView(DetailView):
    model = Book
    template_name = "BookStore/book_details.html"


# def book_details(request, book_id):
#     book_detail = Book.objects.get(id=book_id)
#     return render(request, 'BookStore/book_details.html', {'book': book_detail})


def search(request):
    search_value = request.GET.get('search_value')
    results = Book.objects.filter(Q(book_title__icontains=search_value) | Q(author_name__icontains=search_value))
    context = {'results': results, 'search_value':search_value}
    return render(request, 'BookStore/search_results.html', context)
