from django.core.exceptions import ValidationError


def product_price_validator(price: float):
    if price < 0:
        raise ValidationError("Price can't be a negative number")
