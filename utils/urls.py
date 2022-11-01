from django.urls import path

from .weather import fetchweather_coords

urlpatterns = [
    path('weather/fetchcurrent/', fetchweather_coords),

]
