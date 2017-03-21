from django.core.exceptions import ValidationError
from spfa_mt import kvp


# Function: validate_related_case
# Purpose:  Ensure that the passed-in related case can be successfully linked to a contact log
#           according to business rules.
# Params:   value - the case to link the contact log to
def validate_related_case(value):
    raise NotImplementedError("Not yet implemented!")