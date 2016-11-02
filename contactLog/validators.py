from django.core.exceptions import ValidationError
from datetime import datetime


def validateDate(toCheck):
    try:
        datetime.strptime(toCheck, '%Y/%m/%d')
        return True
    except ValueError:
        return False