from django.urls import path
from .views import PlaceOrderAPI

urlpatterns = [
    path("orders/", PlaceOrderAPI.as_view()),
]
