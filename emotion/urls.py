from django.urls import path, re_path
from .views import EmotionList, EmotionDetail, EmotionTimeRange

urlpatterns = [
    path("emotions/", EmotionList.as_view(), name="emotions_list"),
    path("emotions/<int:pk>", EmotionDetail.as_view(), name="emotion_detail"),
    re_path("emotions/(?P<start>.*)", EmotionTimeRange.as_view(),
            name="emotion_time_range"),

]
