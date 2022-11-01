from django.urls import path

from .weather_util import fetchweather_coords

urlpatterns = [
    path('weather/fetchcurrent/', fetchweather_coords),

]
