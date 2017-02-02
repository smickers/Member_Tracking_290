from django.core.exceptions import ValidationError
import re


# Ensure award amount exists, is at least 1, and is less than 10,000:
def validate_award_amt(amount):
    if amount >= 1 and amount <= 99999:
        return True
    else:
        raise ValidationError("Cost must be between .01 and 999999")
def validate_desc(value):
    # null and whitespace validation
    if not (value and not value.isspace()):
        raise ValidationError("Award description cannot be left blank.")
    # A-Z in both cases, numbers, hyphen, space, apostrophe. Not in Acceptance Tests, but good to have.
    sc_regex = re.compile(r'^[a-zA-Z0-9\-\s\']{1,40}$')
    if not sc_regex.match(str(value)):
        raise ValidationError("Description may only contain letters, numbers, spaces, hyphens, and apostrophes.")


# Ensure description exists, and is less than 150 characters:
def validate_description(description):
    """"""

def validate_amt(value):
    # 5 digits or less
    if len(str(value)) > 5:
        raise ValidationError("Amount must be greater than $0 and less than $10,000.")
    # Required
    if len(str(value)) == 0 or value <= 0:
        raise ValidationError("Award value is required.")
    # No decimals
    if not isinstance(value, int):
        raise ValidationError("Award value must be a whole number (no decimals).")
