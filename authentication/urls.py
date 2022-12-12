from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = "authentication"
urlpatterns = [
    path("users/register/", RegistrationAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("users/retrieve/", UserRetrieveUpdateAPIView.as_view()),
]
