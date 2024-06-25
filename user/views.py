from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from user.models import User, Payment
from user.serializers import UserSerializer, PaymentSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
