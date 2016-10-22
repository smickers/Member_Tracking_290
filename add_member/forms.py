from django.forms import ModelForm, NumberInput, TextInput, SelectDateWidget
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person

        fields = '__all__'
        labels = {
            'memberID': 'Member ID/Saskpoly ID',
            'firstName': 'First Name',
            'middleName': 'Middle Name',
            'socNum': 'SIN',
            'city':'City',
            'mailAddress': 'Mail Address',
            'mailAddress2': 'Mail Address 2',
            'pCode':'Postal Code',
            'bDay':'Birth Date',
            'gender': 'Gender',
            'hPhone': 'Home Phone',
            'cPhone': 'Cell Phone',
            'hEmail': 'Home Email',
            'campus': 'Campus',
            'jobType': 'Job Type',
            'committee': 'Committee',
            'memberImage': 'Member Image',
            }

        widgets = {
            'memberID': NumberInput(attrs={'min':0,'max':999999999}),
            'socNum': NumberInput(attrs={'min': 0, 'max': 999999999}),
            'bDay': SelectDateWidget()
            }



