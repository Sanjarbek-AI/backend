from rest_framework.exceptions import ValidationError


def phone_validation(phone_number):
    """Function for validating a phone number"""
    phone_number = phone_number.replace(" ", "")

    if phone_number.isdigit():
        if len(phone_number) < 9 or len(phone_number) > 9:
            raise ValidationError({'phone_number': ["Phone number must contain 12 numbers."]})
    else:
        raise ValidationError({'phone_number': ["Phone number must not contain any symbols."]})

    # Added: enter phone number without +998
    phone_number = '+998{}'.format(str(phone_number))

    return phone_number
