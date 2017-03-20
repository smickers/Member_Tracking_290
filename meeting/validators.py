from django.core.exceptions import ValidationError
from spfa_mt import settings

# Validator for file upload extension
def validate_file_ext(value):
    if value.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
        raise ValidationError('Invalid File Extension')
