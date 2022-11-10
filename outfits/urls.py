from django.urls import path

from .views import get_suggestions


app_name = 'outfits'

urlpatterns = [
    path('masterapi/getsuggestions/', get_suggestions),

]
