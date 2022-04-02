from dataclasses import field
from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.Serializer):
   size = serializers.CharField(max_length=20)
   order_status = serializers.HiddenField(default='PENDING')
   quantity = serializers.IntegerField()

   class Meta:
      model = Order
      fields = ['size', 'order_status', 'quantity']
