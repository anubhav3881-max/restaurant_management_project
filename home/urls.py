from django.urls import path
from .views import *
from .views import MenuCategoryListView, TableDetailView #view import

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view()),
    # Ye URL hit karne par sab categories ka data milega
    path('api/tables/<int:pk>/', TableDetailView.as_view()),
]