from django.urls import path
from .views import ItemAPIView, ItemParamAPIView

urlpatterns = [
    path('', ItemAPIView.as_view()),
    path('<str:itemId>/', ItemParamAPIView.as_view()),
]