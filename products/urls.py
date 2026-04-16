from django.urls import path
from .views import ItemView, FeaturedItemView, ItemViewSet, ItemIngredientsView, MenuItemViewSet, MenuItemsByCategory
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewSet)
router.register('menu', MenuItemViewSet)

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('featured-items/', FeaturedItemView.as_view()),
    path('items/<int:pk/ingredients/', ItemIngredientsView.as_view()),
    path('menu-items/', MenuItemsByCategory.as_view()),

]

urlpatterns += router.urls