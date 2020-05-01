from django.urls import path
from .views import EmotionList

urlpatterns = [
    path("emotions/", EmotionList.as_view(), name="emotions_list")
]
