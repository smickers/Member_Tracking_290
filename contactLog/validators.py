from django.core.exceptions import ValidationError
from datetime import datetime
import re

def validate_memberID(value):
    MEMBER_ID_REGEX = re.compile(r"^\d{1,9}$")
    if not MEMBER_ID_REGEX.match(str(value)):
        raise ValidationError("An invalid member ID was entered!")

def validate_description(value):
    DESCRIPTION_LENGTH_REGEX = re.compile(r"^.{0,150}$")
    if not DESCRIPTION_LENGTH_REGEX.match(str(value)):
        raise ValidationError("The description must be 0 to 150 characters!!!!")

