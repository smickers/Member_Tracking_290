from django.forms import ModelForm, SelectDateWidget, Textarea
from .models import GrievanceAward


class GrievanceAwardForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = GrievanceAward

        fields = '__all__'
        labels = {
            'Grievance Type:': 'grievanceType',
            'Related Recipient:': 'recipient',
            'Related Case:': 'case',
            'Award Amount:': 'awardAmount',
            'Description:' : 'description',
            'Date Awarded:' : 'date'
        }

        widgets = {
            'date': SelectDateWidget(),
            'description' : Textarea()
        }
