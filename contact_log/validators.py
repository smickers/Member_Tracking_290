# SPFA MT CST Project
# November 7, 2016
from django.core.exceptions import ValidationError
from datetime import datetime
import re
from add_member.models import Person

# Function: validate_memberID
# Purpose: Ensure a memberID is valid
# Returns: Nothing, but can throw an exception
# if an invalid memberID is entered.
def validate_member(value):
    # Ensure the passed in value is between 1 and 9 digits (inclusive)
    if Person.objects.filter(id=value.id).exists():
        return True
    else:
        raise ValidationError("A valid member must be selected!")

# Function: validate_description
# Purpose: Ensure a description is less than 150 chars
# Returns: Nothing, but can throw an exception
# if a description that is too long is entered
""" def validate_description(value):
    DESCRIPTION_LENGTH_REGEX = re.compile(r"^.{0,150}$")
    if not DESCRIPTION_LENGTH_REGEX.match(str(value)):
        raise ValidationError("The description must be 0 to 150 characters!!!!")
        """

