from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    # overwrite default username
    username = models.CharField(blank=True, null=True,
                                max_length=255, unique=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Emotion(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(default=now)
    story = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
