import typing
from .models import Product, Category, Suggestion, Weather
from utils.weather import filter_weather_data


def get_products_by_category(category: str) -> typing.List[dict]:

    if category == "all":
        return Product.objects.all()
    category_obj = Category.objects.get(name=category)

    return Product.objects.filter(category=category_obj)


def save_suggestion_history(suggestion_dict, user, weather_dict) -> None:

    weather = filter_weather_data(weather=weather_dict)
    weather_obj = Weather(**weather)
    weather_obj.save()

    for key in suggestion_dict:
        for product in suggestion_dict[key]:
            Suggestion.objects.create(user=user, product=product, weather=weather_obj)


def get_saved_suggestions(date, user):
    return (
        Suggestion.objects.filter(user=user, date__istartswith=date)
        .order_by("product_id")
        .distinct("product_id")
    )
