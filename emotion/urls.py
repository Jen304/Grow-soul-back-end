from django.urls import path, re_path
from .views import EmotionList, EmotionDetail, EmotionTimeRange, CreateUser
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("emotions/", EmotionList.as_view(), name="emotions_list"),
    path("emotions/<int:pk>", EmotionDetail.as_view(), name="emotion_detail"),
    re_path("emotions/timerange/(?P<start>.*)/(?P<end>.*)", EmotionTimeRange.as_view(),
            name="emotion_time_range"),

]
# add auth url to emotion application
urlpatterns += [
    path('user/create', CreateUser.as_view(), name="create_user"),
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(),
         name='login'),  # override jwt stock token
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
]
