from django.core.exceptions import ValidationError
import re

def validate_pCode(value):
    PCODE_REGEX = re.compile(r"[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ][0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]")
    if not PCODE_REGEX.match(str(value).upper()):
        raise ValidationError("Invalid postal code")

def validate_numbers(value):
    HNUM_REGEX = re.compile(r"\([0-9]{3}\)[0-9]{3}-[0-9]{4}")
    if not HNUM_REGEX.match(str(value)):
        raise ValidationError("Invalid number")