from django.core.exceptions import ValidationError
import re
#from .models import EducationAward

#PD AWARDS
# Ensure award amount exists, is at least 0.01, and is less than 1,000,000:
def validate_award_amt(amount):
    if amount and amount > 0 and amount < 1000000:
        return True
    else:
        raise ValidationError("Amount must be greater than $0 and less than $1,000,000.")

#def validate_end_date(endDate, startDate):
#    if endDate < startDate:
 #       raise ValidationError("End Date must be the same as or come after start date")

#EDUCATION AWARDS
# Validator for ensuring a valid description has been entered:
def validate_eduaward_desc(value):
    # null and whitespace validation
    if not (value and not value.isspace()):
        raise ValidationError("Award description cannot be left blank.")
    # A-Z in both cases, numbers, hyphen, space, apostrophe. Not in Acceptance Tests, but good to have.
    sc_regex = re.compile(r'^[a-zA-Z0-9\-\s\']{1,150}$')
    if not sc_regex.match(str(value)):
        raise ValidationError("Description may only contain letters, numbers, spaces, hyphens, and apostrophes.")

