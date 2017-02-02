from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from add_member.models import Person
from datetime import date


# Models for Education Awards
class EducationAward(models.Model):
    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True)
    award_amount = models.IntegerField(max_length=5, null=True)

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='award:create_edu_award_detail/', kwargs={'pk': self.pk})

    # Method: __str__ (toString)
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description + " ($" + self.award_amount + ")"

#Model for PD Award
class PDAward(models.Model):
    #Fields for creating a pd award
    awardName = models.CharField(max_length=50)
    memberAwarded = models.ForeignKey(Person)
    awardCost = models.FloatField(min(.01), max(99999))
    startDate = models.DateField(default=date.today())
    endDate = models.DateField(default=date.today())

    #Default get_absolute_url_method
    def get_absolute_url(self):
        return reverse(viewname='award:create_pd_award_detail', kwargs={'pk':self.pk})