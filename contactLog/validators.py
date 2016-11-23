# SPFA MT CST Project
# November 7, 2016
from django.core.exceptions import ValidationError
from datetime import datetime
import re

# Function: validate_memberID
# Purpose: Ensure a memberID is valid
# Returns: Nothing, but can throw an exception
# if an invalid memberID is entered.
def validate_memberID(value):
    # Ensure the passed in value is between 1 and 9 digits (inclusive)
    MEMBER_ID_REGEX = re.compile(r"^\d{1,9}$")
    if not MEMBER_ID_REGEX.match(str(value)):
        raise ValidationError("An invalid member ID was entered!")

# Function: validate_description
# Purpose: Ensure a description is less than 150 chars
# Returns: Nothing, but can throw an exception
# if a description that is too long is entered
def validate_description(value):
    DESCRIPTION_LENGTH_REGEX = re.compile(r"^.{0,150}$")
    if not DESCRIPTION_LENGTH_REGEX.match(str(value)):
        raise ValidationError("The description must be 0 to 150 characters!!!!")

