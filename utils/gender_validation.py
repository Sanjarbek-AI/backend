from django.core.exceptions import ValidationError


def validate_gender(value):
    """ Function to validate if rate is greater than 1 """
    if value > 1:
        raise ValidationError('Gender value can be only 0 or 1!')
