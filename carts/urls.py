from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views
app_name = 'carts'


urlpatterns = [
    path('', views.cart_home, name='cart_home'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_home, name='checkout_home'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)