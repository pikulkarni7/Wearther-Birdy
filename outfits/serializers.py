from rest_framework import serializers


from authentication.serializers import UserSerializer
from .models import Product, Suggestion, Weather


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class SuggestionSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = Suggestion
        fields = [
            "product",
        ]
