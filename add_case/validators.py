from django.core.exceptions import ValidationError
import re
import datetime


def validate_date(value):
    data = value

    if data > datetime.date.today():
        raise ValidationError("Cannot enter a future date")

    return data


def validate_status(value):
    data = value
    found = False
    if data == "":
        data = 'OPEN'
        return data

    status = [
        "O",
        "C",
        "P",
        "A-R-M",
        "A-R-S"
    ]

    for val in status:
        if val == data:
            found = True

    if not found:
        raise ValidationError("Must enter a valid status")

    return data


def validate_case_type(value):
    data = value

    types = [
        "G-I",
        "G-G",
        "G-P",
        "G-CLASS",
        "G-COMP",
        "DC",
        "A",
        "C"
    ]

    found = False
    for val in types:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must enter a valid case type")

    return data

'''
Name:       validate_location
Function:   Ensures that the location is a part of the location listing.
Returns:    The data
'''
def validate_location(value):
    data = value

    locations = [
        "Saskatoon",
        "Regina",
        "MJ",
        "PA"
    ]

    found = False
    for val in locations:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must select a valid location")

    return data

'''
Name:       validate_departments
Function:   Ensures that the department is a part of the department listing.
Returns:    The data
'''
def validate_department(value):
    data = value

    departments = [
        "LT",
        "ILDC",
        "LIB",
        "PLAR",
        "SL",
        "SD",
        "LS",
        "FC"
    ]

    found = False
    for val in departments:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must select a valid department")

    return data


'''
Name:       validate_schools
Function:   Ensures that the school is a part of the school listing.
Returns:    The data
'''
def validate_school(value):
    data = value

    schools = [
        "BUS",
        "CON",
        "HEAL",
        "HSCS",
        "ICT",
        "MEM",
        "NRBE",
        "NURS",
        "TRAN"
    ]

    found = False
    for val in schools:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must select a valid school")

    return data
