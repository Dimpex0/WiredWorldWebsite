from django.core.exceptions import ValidationError


def quantity_validation(quantity: int):
    if quantity <= 0:
        raise ValidationError("Quantity can't be 0 or less")
