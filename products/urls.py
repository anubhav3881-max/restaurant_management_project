from django.urls import path
from .views import ItemView, FeaturedItemView, ItemViewSet, MenuItemIngredientsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('featured-items/', FeaturedItemView.as_view()),
    path('menu-items/<int:pk/ingredients/', MenuItemIngredientsView.as_view()),
]

urlpatterns += router.urls