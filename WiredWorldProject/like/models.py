from django.db import models

from WiredWorldProject.account.models import Profile
from WiredWorldProject.product.models import Product


class Like(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
