from snacks.models import Snack
from django.urls import path, include
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_details')
]


