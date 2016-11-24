from django.core.exceptions import ValidationError
import re
import datetime

def validate_name(value):
    data = value

    if data:
        if len(data) > 20:
            raise ValidationError("Name needs to be less than 20 characters")
    else:
        raise ValidationError("You need to enter a name")

    return data

def validate_desc(value):
    data = value

    if data and len(data) > 50:
        raise ValidationError("Description needs to be less than 50 characters")

    return data

def validate_location(value):
    data = value

    if not data or len(data) > 25:
        raise ValidationError("Location needs to be less than 25 characters")

    return data