from django.db import models
from django.conf import settings
from BookStore.models import Book
from django.db.models.signals import m2m_changed
from simple_history.models import HistoricalRecords

User = settings.AUTH_USER_MODEL


class MyLibraryManager(models.Manager):
    def new_or_get(self, request):
        my_library_id = request.session.get("my_library_id", None)
        qs = self.get_queryset().filter(id=my_library_id)
        # print('me abhi my_libraryManager me hu')
        # print(qs)
        if qs.count() == 1:
            # print('me abhi chutiya hu')
            new_obj = False
            my_library_obj = qs.first()
            if request.user.is_authenticated and my_library_obj.user is None:
                # print('me abhi if me hu')
                if self.get_queryset().filter(user=request.user).first() is not None:
                    # print('me abhi if ke if me hu')
                    my_library_obj1 = self.get_queryset().filter(user=request.user).first()
                    for item in my_library_obj.books.all():
                        my_library_obj1.books.add(item)
                    my_library_obj.delete()
                    my_library_obj = self.get_queryset().filter(user=request.user).first()
                    request.session['my_library_id'] = my_library_obj.id
                my_library_obj.user = request.user
                my_library_obj.save()
        elif request.user.is_authenticated and self.get_queryset().filter(user=request.user).first() is not None:
            new_obj = False
            # print('me abhi elif me hu')
            my_library_obj = self.get_queryset().filter(user=request.user).first()
            request.session['cart_id'] = my_library_obj.id
            my_library_obj.user = request.user
            my_library_obj.save()
        else:
            my_library_obj = self.my_new_library(user=request.user)
            new_obj = True
            request.session['my_library_id'] = my_library_obj.id
        return my_library_obj, new_obj

    def my_new_library(self, user=None):
        print(user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class MyLibrary(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    objects = MyLibraryManager()

    def __str__(self):
        return str(self.id)


def pre_save_my_library_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        books = instance.books.all()
        total = 0
        for x in books:
            total += x.book_price
        instance.total = total
        instance.save()


m2m_changed.connect(pre_save_my_library_receiver, sender=MyLibrary.books.through)

