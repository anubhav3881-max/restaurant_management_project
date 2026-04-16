from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView # DRF ki ListAPIView import
from .models import MenuCategory, Table # MenuCategory model import
from rest_framework import serializers # Serializer ke liye import
from .serializers import TableSerializer
# Serializer banaya jo MenuCategory ke data JSON me convert karega
# Create your views here.
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
# Kaunsa model use ho rha hai
        fields = ['name']
# sirf 'name' field return hogi
# view banayi jo sabhi menu categories ko list karegi
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    # Database se saara data fetch karega
    serializer_class = MenuCategorySerializer # Kaunsa serializer use hoga

class TableDetailView(RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
