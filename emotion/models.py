from django.db import models
from datetime import datetime

# Create your models here.


class Emotion(models.Model):
    emotion = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    story = models.TextField()
