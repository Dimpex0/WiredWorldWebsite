from django.db import models

from WiredWorldProject.product.validators import product_price_validator


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.DecimalField(
        validators=[
            product_price_validator
        ],
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    image = models.ImageField(
        upload_to='product',
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        SubCategory,
        on_delete=models.RESTRICT,
        null=False,
        blank=False
    )
    stock = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title
