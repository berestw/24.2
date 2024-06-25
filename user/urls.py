from django.urls import path
from rest_framework.routers import DefaultRouter

from user.apps import UserConfig
from user.views import UserViewSet, PaymentListAPIView

app_name = UserConfig.name
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments')
] + router.urls
