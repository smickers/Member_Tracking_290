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


def validate_ninedigits(value):
    if len(str(value)) > 9:
        raise ValidationError("Must be 9 digit number")


def validate_rightstringlen20(value):
    if len(str(value)) > 20:
        raise ValidationError("Character length must be less than or equal to 20")


def validate_rightstringlen30(value):
    strrep = str(value)
    if len(str(value))  > 30:
        raise ValidationError("Character length must be less than or equal to 30")


def validate_rightstringlen50(value):
    if len(str(value)) > 50:
        raise ValidationError("Character length must be less than or equal to 50")
