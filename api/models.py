from django.db import models
from base62codec.codec import encode
from django.conf import settings


# Create your models here.
class Link(models.Model):
    source_link = models.URLField()
    short_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.short_link:
            try:
                new_link_id = Link.objects.latest('id').id + 1
            except Link.DoesNotExist:
                new_link_id = 1
            self.short_link = settings.HOST_URL + '/' + encode(new_link_id)
        return super().save(*args, **kwargs)
