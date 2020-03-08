

from django.shortcuts import render, redirect
from BookStore.models import Book
from .models import Cart


def cart_home(request):
    cart = Cart(request.session)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.book_price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, "carts/cart.html", {'cart': cart_obj})


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    product_obj = Book.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj not in cart_obj.products.all():
        cart_obj.products.add(product_obj)
    return redirect("carts:cart_home")


def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    product_obj = Book.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    return redirect("carts:cart_home")
