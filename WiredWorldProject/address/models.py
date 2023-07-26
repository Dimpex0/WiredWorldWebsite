from django.db import models

from WiredWorldProject.account.models import Profile


class Address(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    street = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    city = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    state = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    postal_code = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    country = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.country}, {self.city}, {self.state}, {self.street}, {self.postal_code}"
