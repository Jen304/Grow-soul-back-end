from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from django.utils.timezone import now

# Create your models here.


class Emotion(models.Model):
    value = models.IntegerField()
    created_at = UnixDateTimeField(default=now)
    story = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
