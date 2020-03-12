from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views
app_name = 'mylibrary'


urlpatterns = [
    path('', views.my_library_home, name='my_library_home'),
    path('add-to-mylibrary/', views.add_to_my_library, name='add_to_my_library'),
    path('remove-from-my-library/', views.remove_from_my_library, name='remove_from_my_library'),
    # path('viewed_items', views.viewed_items_home, name='viewed_items_home'),
    # path('add_to_viewed_items/', views.add_to_viewed_items, name='add_to_viewed_items'),
    # path('remove_from_viewed_items/', views.remove_from_viewed_items, name='remove_from_viewed_items'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)