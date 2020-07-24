from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from analytics.utils import get_client_ip
from .signals import object_viewed_signal
User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s viewed on %s' % (self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    content_type = ContentType.objects.get_for_model(sender)  # instance.__class__
    new_view_obj = ObjectViewed.objects.update_or_create(
        user=request.user,
        content_type=content_type,
        ip_address=get_client_ip(request),
        object_id=instance.id,
    )


object_viewed_signal.connect(object_viewed_receiver)
