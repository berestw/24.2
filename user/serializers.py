from rest_framework.serializers import ModelSerializer

from user.models import User, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    payment_history = PaymentSerializer(source='payment_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
