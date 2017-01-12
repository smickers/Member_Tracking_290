from django.core.exceptions import ValidationError
import re


# validators for Committee name
def validate_com_name(value):
    # max length validation
    if len(str(value)) >= 40:
        raise ValidationError("Committee name must be less than 40 characters.")
    # min length validation
    elif len(str(value)) < 1:
        raise ValidationError("Committee name cannot be blank.")

    # null and whitespace validation
    if not (value and not value.isspace()):
        raise ValidationError("Committee name cannot be blank.")

    # special characters validation
    sc_regex = re.compile(r'^[a-zA-Z0-9\s\']{1,40}$')
    if not sc_regex.match(str(value)):
        raise ValidationError("Committee name must contain letters (A-Z) and/or numbers(0-9).")


# validators for the status selector
def validate_status(value):
    status = [
        1,    # Active
        0     # Inactive
    ]

    # length validation
    if len(str(value)) != 1:
        raise ValidationError("Value for committee status is invalid. Please check your selection.")
    # integer validation
    elif not isinstance(value, int):
        raise ValidationError("Committee value not an integer. Please check your selection.")
    # ensure value is never less than 0
    elif not value >= 0:
        raise ValidationError("Status value cannot be less than zero. Please check your selection.")
    # ensure no mucking about in source code
    else:
        found = False

        for val in status:
            if val == value:
                found = True
        if not found:
            raise ValueError("Committee status may be either ACTIVE or INACTIVE. Please check your selection.")
