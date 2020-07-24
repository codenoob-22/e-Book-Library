from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from BookStore.models import Book
from mylibrary.models import MyLibrary
from analytics.models import ObjectViewed


# My Library
@login_required
def my_library_home(request):
    book_viewed = ObjectViewed.objects.order_by('-timestamp').filter(user=request.user)
    if book_viewed.count() >= 12:
        book_viewed = book_viewed[:12]
    my_library_obj, new_obj = MyLibrary.objects.new_or_get(request)
    return render(request, "mylibrary/my_library.html", {'my_library': my_library_obj, 'book_viewed': book_viewed})


@login_required
def add_to_my_library(request):
    book_id = request.POST.get('book_id')
    print(book_id)
    book_obj = Book.objects.get(id=book_id)
    my_library_obj, new_obj = MyLibrary.objects.new_or_get(request)
    if book_obj not in my_library_obj.books.all():
        my_library_obj.books.add(book_obj)
    return redirect("mylibrary:my_library_home")


@login_required
def remove_from_my_library(request):
    book_id = request.POST.get('book_id')
    print(book_id)
    product_obj = Book.objects.get(id=book_id)
    my_library_obj, new_obj = MyLibrary.objects.new_or_get(request)
    if product_obj in my_library_obj.books.all():
        my_library_obj.books.remove(product_obj)
    return redirect("mylibrary:my_library_home")
