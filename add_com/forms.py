from django.forms import ModelForm
from .models import Committee


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
