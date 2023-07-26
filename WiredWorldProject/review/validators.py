from django.core.exceptions import ValidationError


def rating_validation(rating: int):
    if 0 > rating > 5:
        raise ValidationError("Rating must be between 0 and 5")
