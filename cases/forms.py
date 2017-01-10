from django.forms import ModelForm, ModelMultipleChoiceField
from add_case.models import Case
from add_member.models import Person


class CaseMembersForm(ModelForm):

        class Meta:
            model = Case
            fields = ('additionalMembers', 'additionalNonMembers')
        # field from which you will pick additional members to add to the case, after the case has
        # been created.
        additionalMembers = ModelMultipleChoiceField(queryset=(), to_field_name="pk", label='Members', required=False)

        # constructor method.
        def __init__(self, **kwargs):
            super(CaseMembersForm, self).__init__(**kwargs)
            self.fields['additionalMembers'].queryset = Person.objects.exclude(case=self.instance)


        # combines the initial and the new set of additional members
        def clean_additionalMembers(self):
            return self.initial['additionalMembers'] | self.cleaned_data['additionalMembers']