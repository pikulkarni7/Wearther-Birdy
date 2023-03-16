import requests
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Subscription
from .serializers import SubscriptionSerializer


CAGE_SERVICE_URL = "http://127.0.0.1:8080/"


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def create_subscription(request):

    if request.method == "POST":
        curr_user = request.user
        request_data = request.data["Subscription"]

        try:
            # if Subscription.objects.filter(user=curr_user).first() is not None:

            #     return Response({"message": "Subscription already exists!"}, status=status.HTTP_200_OK)

            subscription = Subscription.objects.create(
                user=curr_user,
                phone_number=request_data["phone_number"],
                latitude=request_data["latitude"],
                longitude=request_data["longitude"],
            )

            cage_task_notify(sub=subscription)

            return Response(
                {"message": "Subscription added for user"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            print(e)
            return Response(
                {"message": "Couldn't save user subscription"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


def cage_task_notify(sub):

    serializer_data = SubscriptionSerializer(sub).data

    payload = {
        "phone_number": serializer_data["phone_number"],
        "latitude": serializer_data["latitude"],
        "longitude": serializer_data["longitude"],
    }
    r = requests.post(CAGE_SERVICE_URL + "api/notify", data=payload)
    return None
