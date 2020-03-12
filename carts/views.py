from django.shortcuts import render, redirect
from BookStore.models import Book
from orders.models import Order
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/cart.html", {'cart': cart_obj})


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    print(product_id)
    product_obj = Book.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj not in cart_obj.products.all():
        cart_obj.products.add(product_obj)
    return redirect("carts:cart_home")


def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    print(product_id)
    product_obj = Book.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    return redirect("carts:cart_home")


def checkout_home(request):
    print('checkout_home is running')
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if not cart_created or cart_obj.objects.count() == 0:
        return redirect('carts:cart_home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(request).first()
    return render(request, "carts/checkout.html", {'order': order_obj})
