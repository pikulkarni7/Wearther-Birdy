from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


from .omaster import compute_suggestions
from .serializers import ProductSerializer, SuggestionSerializer, WeatherSerializer
from .queries import save_suggestion_history, get_saved_suggestions, get_saved_dates


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def get_suggestions(request):

    if request.method == "POST":
        curr_user = request.user
        gender = curr_user.get_gender()

        if request.data["weather"] is not None:

            temp = int(request.data["weather"]["temp"])

            try:
                result = compute_suggestions(temperature=temp, gender=gender)

                save_suggestion_history(
                    result, user=request.user, weather_dict=request.data["weather"]
                )

                response = []

                for key in result:
                    product_list = []
                    for product in result[key]:
                        serializer = ProductSerializer(product)
                        product_list.append(serializer.data)
                    response.append({key: product_list})

                return Response(response, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                return Response(
                    {"message": "Couldn't fetch suggestions"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:

            return Response(
                {"message": "No weather data found in request"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def get_suggestion_history(request):

    if request.method == "POST":
        try:
            date = request.data["date"]

            queryset = get_saved_suggestions(date, request.user)

            if queryset.count() > 0:
                weather = WeatherSerializer(queryset.first().weather)
                suggestions = SuggestionSerializer(queryset, many=True)

                suggestions_list = []
                for each in suggestions.data:
                    suggestions_list.append(each["product"])

                response = {}
                response.update({"weather": weather.data})
                response.update({"suggestions": suggestions_list})

                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "No data available"}, status=status.HTTP_404_NOT_FOUND
                )

        except Exception as e:
            print(e)
            return Response(
                {"message": "Couldn't fetch history"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def get_used_dates(request):

    if request.method == "POST":
        try:
            dates_list = []

            queryset = get_saved_dates(user=request.user)
            for each in queryset:
                dates_list.append(each[0].strftime("%m/%d/%Y"))

            return Response({"used_dates": dates_list}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"message": "failed to fetch dates"}, status=status.HTTP_200_OK
            )
