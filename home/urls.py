from django.urls import path
from .views import * #view import

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view()),
    # Ye URL hit karne par sab categories ka data milega
]