import requests
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .timezone import getLocalTime


OPENWEATHER_APIKEY = "51221f79a18cef82c14e9e73aad25715"


@csrf_exempt
@api_view()
@permission_classes([IsAuthenticated])
def fetchweather_coords(request):

    if request.method == "GET":
        try:

            coords = request.query_params

            lat = coords.get("lat")
            long = coords.get("lon")
            payload = {
                "lat": lat,
                "lon": long,
                "appid": OPENWEATHER_APIKEY,
                "units": "metric",
            }

            data = fetch_openweather_data(payload=payload)
            filtered_data = filter_weather_data(data)
            filtered_data["dt"] = getLocalTime(lat=lat, lon=long)
            request.session["weather"] = filtered_data  # add weather to session

            return Response(filtered_data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"message": "Couldn't fetch weather"})


def fetch_openweather_data(payload) -> dict:

    # access openweather api

    r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)

    return json.loads(r.text)


def filter_weather_data(weather) -> dict:

    fields = {
        "name",
        "dt",
        "description",  # main weather description
        "temp",
        "temp_min",
        "temp_max",
        "speed",  # wind speed
        "1h",  # rain 1 hr
        "country",
        "pressure",
        "humidity",
        "feels_like",
        "icon",
    }

    result = {}

    for key, value in weather.items():
        if key in fields:
            result[key] = value

        if isinstance(value, dict):
            result.update(filter_weather_data(value))

        if isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    result.update(filter_weather_data(i))

    if "rain" not in weather.keys():
        result["rain"] = "N/A"

    return result
