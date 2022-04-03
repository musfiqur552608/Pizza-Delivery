from dataclasses import field
from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.Serializer):
   size = serializers.CharField(max_length=20)
   order_status = serializers.HiddenField(default='PENDING')
   quantity = serializers.IntegerField()

   class Meta:
      model = Order
      fields = ['id','size', 'order_status', 'quantity']

   def create(self, validated_data):
      return Order.objects.create(**validated_data)


class OrderDetailSerializer(serializers.Serializer):
   size = serializers.CharField(max_length=20)
   order_status = serializers.CharField(default='PENDING')
   quantity = serializers.IntegerField()
   created_at = serializers.DateTimeField()
   updated_at = serializers.DateTimeField()

   class Meta:
      model = Order
      fields = ['id','size', 'order_status', 'quantity', 'created_at', 'updated_at']
   

   def create(self, validated_data):
      return Order.objects.create(**validated_data)

class OrderStatusUpdateSerializer(serializers.Serializer):
   order_status = serializers.CharField(default='PENDING')

   class Meta:
      model = Order
      field = ['order_status']