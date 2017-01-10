from django.core.exceptions import ValidationError
from add_member.models import Person
from add_case.models import Case

def validate_recipient(memberID):
    if Person.objects.filter(id=memberID).exists():
        return True
    else:
        raise ValidationError("A valid member ID must be entered!")

def validate_case(caseID):
    if Case.objects.filter(id=caseID).exists():
        return True
    else:
        raise ValidationError("A valid case ID must be entered!")

def validate_award_amt(amount):
    if amount:
        if amount > 0 and amount < 1000000:
            return True
        else:
            raise ValidationError("Amount must be greater han $0 and less than $1,000,000.")
    else:
        raise ValidationError("An award amount must be entered.")

def validate_description(description):
    if description and len(description) > 1000:
        raise ValidationError("Description must be 1000 characters or less!")
    return True

def validate_grievance_type(grievanceType):
    if grievanceType:
        if grievanceType == 'M' or grievanceType == 'P':
            return True
        else:
            raise ValidationError("A grievance type of member or policy must be selected!")
    else:
        raise ValidationError("A grievance type must be selected.")