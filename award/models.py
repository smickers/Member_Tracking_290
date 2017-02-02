from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *
from add_member.models import Person
from datetime import date
import validators


# Models for Education Awards
class EducationAward(models.Model):
    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True, validators=[validate_desc])
    award_amount = models.IntegerField(max_length=5, null=True, validators=[validate_amt])

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='award:edu_detail', kwargs={'pk': self.pk})

    # Method: __str__
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description.__str__()

#Model for PD Award
class PDAward(models.Model):
    #Fields for creating a pd award
    awardName = models.CharField(max_length=50)
    memberAwarded = models.ForeignKey(Person)
    awardCost = models.FloatField(validators=[validators.validate_award_amt])
    startDate = models.DateField(default=date.today())
    endDate = models.DateField(default=date.today())

    #Default get_absolute_url_method
    def get_absolute_url(self):
        return reverse(viewname='award:award_pd_detail', kwargs={'pk':self.pk})

    #def clean(self):
    #    if self.endDate < self.startDate:
    #        raise ValidationError("End Date must be the same as or come after start date")

