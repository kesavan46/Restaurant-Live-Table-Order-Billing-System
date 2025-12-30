from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Frontend
    path("", include("frontend.urls")),

    # APIs
    path("api/", include("orders.urls")),
    path("api/", include("billing.urls")),
    path("api/", include("dashboard.urls")),
]
