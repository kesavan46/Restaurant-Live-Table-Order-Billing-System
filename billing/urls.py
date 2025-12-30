from django.urls import path
from .views import GenerateBillAPI, PayBillAPI

urlpatterns = [
    path("bills/", GenerateBillAPI.as_view()),
    path("bills/<int:bill_id>/pay/", PayBillAPI.as_view()),
]
