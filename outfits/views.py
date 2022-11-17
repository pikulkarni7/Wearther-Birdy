import requests
from django.shortcuts import render
from urllib import request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .omaster import compute_suggestions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


from .serializers import ProductSerializer, SuggestionSerializer, WeatherSerializer
from .queries import save_suggestion_history, get_saved_suggestions



@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def get_suggestions(request):
    
    if request.method == 'POST':
        curr_user = request.user
        gender = curr_user.get_gender()
        
        temp = int(request.session['weather']['temp'])
        
        try:
            result = compute_suggestions(temperature=temp, gender=gender)            
            
            save_suggestion_history(result, user=request.user, weather_dict= request.session['weather'])
            
            response = []
            
            for key in result:
                product_list = []
                for product in result[key]:
                    serializer = ProductSerializer(product)
                    product_list.append(serializer.data)
                response.append({key:product_list})
            
            
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message" : "Couldn't fetch suggestions"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def get_suggestion_history(request):
    
    if request.method == 'POST':
        try:
            date = request.data['date']
            
            queryset = get_saved_suggestions(date, request.user)
            weather = WeatherSerializer(queryset.first().weather)
            suggestions = SuggestionSerializer(queryset, many=True)
            
            response = {}            
            response.update({"weather" : weather.data})
            response.update({"suggestions": suggestions.data})
            
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message" : "Couldn't fetch history"}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            



            
        
    
    
    
    
    
    
    