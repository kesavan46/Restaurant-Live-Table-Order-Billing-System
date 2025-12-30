from django.urls import path
from .views import dashboard_view, place_order_view, billing_view, pay_bill_view   ,mark_order_served_view


urlpatterns = [
    path("dashboard/", dashboard_view),
    path("order/", place_order_view),
    path("billing/", billing_view),
    path("billing/pay/<int:bill_id>/", pay_bill_view),
    path("order/served/<int:order_id>/", mark_order_served_view),
]
