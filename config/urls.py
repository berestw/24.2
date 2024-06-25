from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('lms/', include('lms.urls', namespace='lms')),
]
