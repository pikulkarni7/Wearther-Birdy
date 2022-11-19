from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def post_session_variable(request):
    if request.method == "POST":
        try:
            request.session["new_variable"] = request.data["data"]
            request.session.modified = True
            return Response(
                {"message": "Added session data"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"message": "Error creating session variable"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def get_session_variable(request):
    if request.method == "POST":
        try:
            return Response(
                {"message": request.session["new_variable"]}, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"message": "Error fetching session variable"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@csrf_exempt
@api_view(["POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def get_session_key(request):
    if request.method == "POST":
        try:
            return Response(
                {"session_key": request.session._session_key}, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"message": "Error fetching session key"},
                status=status.HTTP_400_BAD_REQUEST,
            )
