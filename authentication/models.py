import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError("Users must have a username.")

        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=False, unique=False)
    gender = models.CharField(max_length=1, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
    ]

    objects = UserManager()

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_gender(self):
        return self.gender

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        print("Encoding token")

        token = jwt.encode(
            {"id": self.pk, "exp": dt.utcfromtimestamp(dt.timestamp())},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
