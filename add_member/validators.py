from django.core.exceptions import ValidationError
import re

def validate_pCode(value):
    PCODE_REGEX = re.compile(r"[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ][0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]")
    if not PCODE_REGEX.match(value):
        raise ValidationError("Invalid postal code")


