import requests
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt



OPENWEATHER_APIKEY = '51221f79a18cef82c14e9e73aad25715'

@csrf_exempt
@api_view()
@permission_classes([IsAuthenticated])
def fetchweather_coords(request):
    
    if request.method=='GET':
        try:
            print(request.query_params)
            
            coords = request.query_params
            
            lat = coords.get('lat')
            long = coords.get('lon')
            
            #access openweather api
            payload = {
                'lat' : lat,
                'lon' : long,
                'appid' : OPENWEATHER_APIKEY,
                'units' : 'metric',
            }
            
            r = requests.get('https://api.openweathermap.org/data/2.5/weather', 
                            params=payload)

            return Response(r.json(), status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message" : "Couldn't fetch weather"})
    
    