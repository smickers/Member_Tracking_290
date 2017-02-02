from django.core.exceptions import ValidationError


# Ensure award amount exists, is at least 1, and is less than 10,000:
def validate_award_amt(amount):
    if amount >= 1 and amount <= 99999:
        return True
    else:
        raise ValidationError("Cost must be between .01 and 999999")


# Ensure description exists, and is less than 150 characters:
def validate_description(description):
    """"""
