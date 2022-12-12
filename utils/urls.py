from django.urls import path

from .weather import fetchweather_coords
from .session import post_session_variable, get_session_variable, get_session_key

urlpatterns = [
    path("weather/fetchcurrent/", fetchweather_coords),
    path("sessions/postvariable/", post_session_variable),
    path("sessions/getvariable/", get_session_variable),
    path("sessions/getkey/", get_session_key),
]
