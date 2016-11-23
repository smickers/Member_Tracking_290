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
        "OPEN",
        "CLOSED",
        "PENDING",
        "ACTION REQ'D - MGMT",
        "ACTION REQ'D SPFA"
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
        "GRIEVANCES - INDIVIDUAL",
        "GRIEVANCES - GROUP",
        "GRIEVANCES - POLICY",
        "GRIEVANCES - CLASSIFICATION",
        "GRIEVANCES - COMPLAINTS",
        "DISABILITY CLAIMS",
        "ARBITRATION",
        "COMPLAINT"
    ]

    found = False
    for val in types:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must enter a valid case type")

    return data
