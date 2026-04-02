from django.urls import path
from .views import *

urlpatterns = [
    path('coupons/validate/', CouponValidationView.as_view()),
]