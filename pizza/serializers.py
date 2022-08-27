from .models import Order
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from authentication.models import User
from authentication.serializers import UserCreationSerailizer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'size', 'order_status', 'quantity',]


class UpdateOrderSerializer(serializers.ModelSerializer):

    order_status = serializers.IntegerField(default='PENDING')

    class Meta:
        model = Order
        fields = ['customer', 'size', 'order_status', 'quantity',]

