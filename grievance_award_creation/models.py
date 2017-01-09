from __future__ import unicode_literals
from add_member.models import Person
from add_case.models import Case
from django.db import models
import validators
from django.core.urlresolvers import reverse

# Create your models here.
class GrievanceAward(models.Model):

    GRIEVANCE_TYPES = [
        ('M', 'Member'),
        ('P', 'Policy'),
    ]

    grievanceType = models.CharField(max_length=1, choices=GRIEVANCE_TYPES, validators=[validators.validate_grievance_type])
    recipient = models.ManyToManyField(Person, blank=True, validators=[validators.validate_recipient])
    case = models.ManyToManyField(Case, blank=True, validators=[validators.validate_case])
    awardAmount = models.FloatField(validators=[validators.validate_award_amt])
    description = models.CharField(max_length=1000, null=True,blank=True, validators=[validators.validate_description])
    date = models.DateField()


    def get_absolute_url(self):
        return reverse(viewname='grievance_award_creation:create_grievance_award_success', kwargs={'pk': self.pk})

    def clean(self):
        validators.validate_grievance_type(self.grievanceType)
        #validators.validate_recipient(self.recipient)
        #validators.validate_case(self.case)
        validators.validate_award_amt(self.awardAmount)
        validators.validate_description(self.description)

    def __str__(self):
        return self.id