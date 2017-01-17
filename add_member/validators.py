from django.core.exceptions import ValidationError
import re

#validators for postal code
def validate_pCode(value):
    # Check to see if postal code is too short
    if value:
        if len(value) < 6:
            raise ValidationError("Postal code entered is too short. Must be in the form A#A #A#.")
        elif len(value) > 7:
            raise ValidationError("Postal code entered is too long. Must be in the form A#A #A#.")
        else:
            PCODE_REGEX = re.compile(r"^[a-zA-Z]\d[a-zA-Z]\s?\d[a-zA-Z]\d$")
            if not PCODE_REGEX.match(str(value)):
                raise ValidationError("Invalid postal code entered! Postal code must be in the form A#A #A#.")

#validators for phone numbers
def validate_numbers(value):
    HNUM_REGEX = re.compile(r"^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$")
    if not HNUM_REGEX.match(str(value)):
        raise ValidationError("Invalid number format")


#validators for 9 digit chars
def validate_ninedigits(value):
    if len(str(value)) > 9:
        raise ValidationError("Must be 9 digit number")


#validators for 20 characters string
def validate_rightstringlen20(value):
    if len(str(value)) > 20:
        raise ValidationError("Character length must be less than or equal to 20")

#validators for 30 characters string
def validate_rightstringlen30(value):
    strrep = str(value)
    if len(str(value))  > 30:
        raise ValidationError("Character length must be less than or equal to 30")


#validators for
def validate_rightstringlen50(value):
    if len(str(value)) > 50:
        raise ValidationError("Character length must be less than or equal to 50")
