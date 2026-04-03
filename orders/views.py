from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon
from datetime import date
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
# Create your views here.

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code') # request se code lena
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response({"error": 'Invalid coupon'},
            status= status.HTTP_400_BAD_REQUEST)
            # check conditions
            if not coupon.is_active:
                return Response({"error" : "Coupon is inactive"},
                status= status.HTTP_400_BAD_REQUEST)
                today = date.today()
                if not (coupon.valid_from <= today <= coupon.valid_until):
                    return Response({"error": "Coupon expired or not valid yet"},
                    status = status.HTTP_400_BAD_REQUEST)
                    # valid coupon
                    return Response({"message": "Coupon is valid", "discount_percentage": coupon.discount_percentage},
                    status=status.HTTP_200_ok)

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request): # sirf logged-in user ke orders
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
            