from django.db import models

from WiredWorldProject.account.models import Profile
from WiredWorldProject.product.models import Product
from WiredWorldProject.review.validators import rating_validation


class Review(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    content = models.TextField(
        null=False,
        blank=False
    )
    stars = models.PositiveIntegerField(
        validators=[
            rating_validation
        ]
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
