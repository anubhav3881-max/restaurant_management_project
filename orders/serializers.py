from rest_framework import serializers
from .models import Order, OrderItem #OrderItem tab use hoga agar items alag model hai
# Order Item Serializer(nested)
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    # "items" related_name hona chahiye OrderItem me
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_price', 'items']