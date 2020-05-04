from django.contrib import admin
from .models import Emotion, User


class CustomUserAdmin(admin.ModelAdmin):
    model = User


# Register your models here
admin.site.register(Emotion)
admin.site.register(User, CustomUserAdmin)

