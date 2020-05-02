from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
# add the urls to emotion application
urlpatterns += [
    path('v1/', include('emotion.urls')),
]
