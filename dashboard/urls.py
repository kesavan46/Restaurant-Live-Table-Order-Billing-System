from django.urls import path
from .views import TableDashboardAPI

urlpatterns = [
    path("dashboard/tables/", TableDashboardAPI.as_view()),
]
