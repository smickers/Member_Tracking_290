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
        "Learning Technologies",
        "ILDC",
        "Library",
        "PLAR",
        "Simulation Lab",
        "Student Development",
        "Learning Services",
        "Fitness Centre"
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
        "School of Business",
        "School of Construction",
        "School of Health Sciences",
        "School of Human Services and Community Safety",
        "School of Information and Communications Technology",
        "School of Mining, Energy and Manufacturing",
        "School of Natural Resources and Built Environment",
        "School of Nursing",
        "School of Transportation",
        "Other",
    ]

    found = False
    for val in schools:
        if val == data:
            found = True

    if found is False:
        raise ValidationError("Must select a valid school")

    return data

# Validators to ensure that the complainant cannot be/is not entered to the Case
#   as an additional member.
def validate_additional_members(complainant, additional_members):
    """things here"""
    # Loop through additional members
        # Ensure current != complainant
    #for curr_member in additional_members:
    print(additional_members.__str__())
    print("Additional member ID: " + additional_members.id.__str__())
    print("Complainant member ID: " + complainant.id.__str__())
    if additional_members.id == complainant.id:
        raise ValidationError("Complainant cannot be added as an additional member.")

