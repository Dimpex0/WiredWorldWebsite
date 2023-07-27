from django.db import models

from WiredWorldProject.account.models import Profile
from WiredWorldProject.cart.validators import quantity_validation
from WiredWorldProject.product.models import Product


class Order(models.Model):
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
        blank=False,
    )
    quantity = models.PositiveIntegerField(
        validators=[
            quantity_validation
        ],
        null=False,
        blank=False
    )
    date = models.DateTimeField(
        null=False,
        blank=False
    )

    def get_price(self):
        return f'{self.quantity * self.product.price:.02f}'

