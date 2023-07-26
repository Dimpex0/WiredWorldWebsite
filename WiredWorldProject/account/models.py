from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from WiredWorldProject.account.managers import ClientManager
from WiredWorldProject.account.validators import name_validator


class Client(AbstractUser):
    username = models.CharField(
        max_length=4,
        default='None',
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    objects = ClientManager()

    def __str__(self):
        return self.email


UserModel = get_user_model()


class Profile(models.Model):
    client = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=50,
        validators=[
            name_validator,
            MinLengthValidator(2)
        ],
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            name_validator,
            MinLengthValidator(2)
        ],
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )
    image = models.ImageField(
        upload_to='profile',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.email

