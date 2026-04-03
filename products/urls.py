from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('featured-items/', FeaturedItemView.as_view()),
]