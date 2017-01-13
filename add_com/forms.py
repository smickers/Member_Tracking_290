from django.forms import ModelForm
from .models import Committee
from django.core.exceptions import NON_FIELD_ERRORS


# Form used for Creating a Committee:
class ComForm(ModelForm):
    class Meta:
        model = Committee

        # Fields to be used on the form
        fields = '__all__'

        # Field labels
        labels = {
            'name': 'Name',
            'status': 'Status'
        }

        # Change the default error messages displayed
        error_messages = {
            NON_FIELD_ERRORS: {


            },
            'name': {
                'required': 'Committee name cannot be blank.',
                'max_length': 'Committee name must be less than 40 characters.',
                'min_length': 'Committee name cannot be blank.'
            },
            'status': {
                'invalid': 'Value for committee status is invalid. Please check your selection.',
                'min_value': 'Status value cannot be less than zero. Please check your selection.',
                'invalid_choice': 'Committee status may be either ACTIVE or INACTIVE. Please check your selection.'
            }
        }


