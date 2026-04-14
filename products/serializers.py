from rest_framework import serializers
from .models import Item, Ingredient

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class IngredientSerializer(serializers. ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'