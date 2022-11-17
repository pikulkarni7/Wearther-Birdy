from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "is_staff", "token"]

    def create(self, validated_data):
        if validated_data["is_staff"] == 1:
            return User.objects.create_superuser(
                validated_data["username"],
                validated_data["email"],
                validated_data["password"],
            )
        return User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ["username", "email", "password"]

    def validate(self, data):

        username = data.get("username", None)
        password = data.get("password", None)

        print(username)

        if username is None:
            raise serializers.ValidationError("A username is required to log in.")

        if password is None:
            raise serializers.ValidationError("A password is required to log in.")
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this credentials was not found."
            )

        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated.")

        return {"email": user.email, "username": user.username, "token": user.token}


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "username", "password", "is_staff")
        # read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        instance.save()

        return instance
