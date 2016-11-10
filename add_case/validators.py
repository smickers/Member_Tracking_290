from django.core.exceptions import ValidationError
import re
import datetime

def validate_date(value):
    data = value
    if data == 0:
        data = datetime.datetime.now().date().strftime('%Y-%m-%d')

    if data > datetime.datetime.now().date():
        raise ValidationError("Cannot enter a future date")

    return data

def validate_status(value):
    data = value
    if data == 0:
        data = 'OPEN'

    if data is not 'OPEN' or data != 'CLOSED' or data != 'PENDING' or data != "ACTION REQ'D - MGMT" or data != "ACTION REQ'D SPFA":
        raise ValidationError("Must enter a valid status.")

    return data

def validate_case_type(value):
    data = value

    types = [
        "GREIVANCES - INDIVIDUAL",
        "GREIVANCES - GROUP",
        "GREIVANCES - POLICY",
        "GREIVANCES - CLASSIFICATION",
        "GREIVANCES - COMPLAINTS",
        "DISABILITY CLAIMS",
        "ARBITRATIONS",
        "COMPLAINTS"
    ]

    found = False
    for val in types:
        if val == data:
            found = True

    if not found:
        raise ValidationError("Must enter a valid case type")

    return data
