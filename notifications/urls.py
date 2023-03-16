from django.urls import path

from .views import create_subscription


app_name = "notifications"

urlpatterns = [
    path("subscribe/", create_subscription),
]
