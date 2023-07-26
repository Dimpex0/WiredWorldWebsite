from django.core.exceptions import ValidationError


def name_validator(name: str):
    for char in name:
        if not char.isalpha():
            raise ValidationError("Name must include only letters")
