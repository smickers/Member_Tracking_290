from django.core.exceptions import ValidationError
import datetime
from spfa_mt import kvp


def validate_complainant(value):
    complainant = value

def validate_date(value):
    data = value

    if data > datetime.date.today():
        raise ValidationError("Cannot enter a future date")

    return data


def validate_status(value):
    data = value
    if data == "":
        data = 'OPEN'
        return data
    if data not in kvp.STATUS_CHOICES:
        raise ValidationError("Must enter a valid status")

    return data


def validate_case_type(value):
    data = value

    if data not in kvp.TYPE_CHOICES:
        raise ValidationError("Must enter a valid case type")

    return data


# Name:       validate_location
# Function:   Ensures that the location is a part of the location listing.
# Returns:    The data
def validate_location(value):
    data = value

    if not kvp.CAMPUS_CHOICES.__contains__(data):
        raise ValidationError("Must select a valid location")

    return data


# Name:       validate_departments
# Function:   Ensures that the department is a part of the department listing.
# Returns:    The data
def validate_department(value):
    data = value

    if not kvp.DEPARTMENT_CHOICES.__contains__(data):
        raise ValidationError("Must select a valid department")

    return data


# Name:       validate_schools
# Function:   Ensures that the school is a part of the school listing.
# Returns:    The data
def validate_school(value):
    data = value

    if not kvp.SCHOOL_CHOICES.__contains__(data):
        raise ValidationError("Must select a valid school")

    return data


# Validators to ensure that the complainant cannot be/is not entered to the Case
#   as an additional member.
# def validate_additional_members(value):
#     for curr_member in value:
#         if curr_member == complainant:
#             raise ValidationError("Complainant cannot be added as an additional member.")
