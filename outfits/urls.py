from django.urls import path

from .views import get_suggestions, get_suggestion_history


app_name = "outfits"

urlpatterns = [
    path("masterapi/getsuggestions/", get_suggestions),
    path("masterapi/fetchhistory/", get_suggestion_history),
]
