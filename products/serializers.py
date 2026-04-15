from rest_framework import serializers
from .models import Item, Ingredient, MenuItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class IngredientSerializer(serializers. ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
    def validate_price(selft, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value