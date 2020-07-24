from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from analytics.mixin import ObjectViewedMixin
from .models import Post, Book


def blog(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def add(request):
    # n1 = request.POST['n1']
    # n2 = request.POST['n2']
    # res = int(n1) + int(n2)
    return render(request, 'base.html', {'result': res})


# Book Library functions
def index(request):
    latest_books = Book.objects.filter().order_by('-modified_date')[:6]
    textbooks = Book.objects.filter(Q(book_category__icontains='textbook'))[:6]
    fictions = Book.objects.filter(Q(book_category__icontains='fiction'))[:6]
    non_fictions = Book.objects.filter(Q(book_category__icontains='non_fiction'))[:6]
    stories = Book.objects.filter(Q(book_category__icontains='story'))[:6]
    poetry = Book.objects.filter(Q(book_category__icontains='poetry'))[:6]
    novels = Book.objects.filter(Q(book_category__icontains='novel'))[:6]
    other = Book.objects.filter(Q(book_category__icontains='other'))[:6]
    return render(request, 'BookStore/storepage.html', {'latest_books': latest_books, 'textbooks': textbooks,
                                                        'fictions': fictions, 'non_fictions': non_fictions,
                                                        'stories': stories, 'poetry': poetry,
                                                        'novels': novels,
                                                        'other': other})


def latest_books(request):
    latest_books = Book.objects.filter().order_by('-modified_date')
    return render(request, 'BookStore/category_details.html', {'title': 'Latest Books', 'category': latest_books})


def textbooks(request):
    textbooks = Book.objects.filter(Q(book_category__icontains='textbook'))
    return render(request, 'BookStore/category_details.html', {'title': 'Text Books', 'category': textbooks})


def fictions(request):
    fictions = Book.objects.filter(Q(book_category__icontains='fiction'))
    return render(request, 'BookStore/category_details.html', {'title': 'Fiction Books', 'category': fictions})


def non_fictions(request):
    non_fictions = Book.objects.filter(Q(book_category__icontains='non_fiction'))
    return render(request, 'BookStore/category_details.html', {'title': 'Non-Fiction Books', 'category': non_fictions})


def stories(request):
    stories = Book.objects.filter(Q(book_category__icontains='story'))
    return render(request, 'BookStore/category_details.html', {'title': 'Story Books', 'category': stories})


def poetry(request):
    poetry = Book.objects.filter(Q(book_category__icontains='poetry'))
    return render(request, 'BookStore/category_details.html', {'title': 'Poetry Books', 'category': poetry})


def novels(request):
    novels = Book.objects.filter(Q(book_category__icontains='novel'))
    return render(request, 'BookStore/category_details.html', {'title': 'Novels Books', 'category': novels})


def other(request):
    other = Book.objects.filter(Q(book_category__icontains='other'))
    return render(request, 'BookStore/category_details.html', {'title': 'Miscellaneous Books', 'category': other})


def library(request):
    books = Book.objects.all()[0:6]
    latest_books = Book.objects.filter().order_by('-book_title')
    return render(request, 'BookStore/storepage.html', {'latest_books': latest_books, 'books': books})


class BookReaderSlugView(DetailView):
    model = Book
    template_name = "BookStore/bookreader.html"


@login_required()
def bookreader(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'BookStore/bookreader.html', {'book': book})


class BookDetailSlugView(ObjectViewedMixin, DetailView):
    model = Book
    template_name = "BookStore/book_details.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            raise Http404("Not Found")
        except:
            raise Http404('Kuch nhi mila mujhe')
        # object_viewed_signal.send(instance, instance=instance, request=request)
        return instance


def search(request):
    search_value = request.GET.get('search_value')
    results = Book.objects.filter(Q(book_title__icontains=search_value) | Q(author_name__icontains=search_value))
    context = {'results': results, 'search_value': search_value}
    return render(request, 'BookStore/search_results.html', context)
