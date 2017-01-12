from django.core.exceptions import ValidationError
from add_member.models import Person
from add_case.models import Case

# Method: validate_recipient
# Purpose: Validates a passed-in member ID.
# Parameter: memberID - the member ID to be validated
# Returns: True if valid, raises exception if not
def validate_recipient(memberID):
    if Person.objects.filter(id=memberID).exists():
        return True
    else:
        raise ValidationError("A valid member ID must be entered!")

# Method: validate_case
# Purpose: Validates a passed-in case ID.
# Parameter: caseID - the case ID to be validated
# Returns: True if valid, raises exception if not
def validate_case(caseID):
    if Case.objects.filter(id=caseID).exists():
        return True
    else:
        raise ValidationError("A valid case ID must be entered!")

# Method: validate_award_amt
# Purpose: Validates a passed-in award amount.
# Parameter: amount - the value to be validated
# Returns: True if valid, raises exception if not
def validate_award_amt(amount):
    if amount and amount > 0 and amount < 1000000:
        return True
    else:
        raise ValidationError("Amount must be greater than $0 and less than $1,000,000.")

# Method: validate_description
# Purpose: Validates a passed-in description.
# Parameter: description - the description to be validated
# Returns: True if valid, raises exception if not
def validate_description(description):
    if description and len(description) > 1000:
        raise ValidationError("Description must be 1000 characters or less!")
    return True

# Method: validate_grievance_type
# Purpose: Validates a passed-in grievance type.
# Parameter: grievanecType - the grievance type to be validated
# Returns: True if valid, raises exception if not
def validate_grievance_type(grievanceType):
    if grievanceType:
        if grievanceType == 'M' or grievanceType == 'P':
            return True
        else:
            raise ValidationError("A grievance type of member or policy must be selected!")
    else:
        raise ValidationError("A grievance type must be selected.")