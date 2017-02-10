from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *
from add_member.models import Person
from datetime import date
import validators
from spfa_mt import kvp
import datetime

 
# Models for Education Awards
class EducationAward(models.Model):



    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True, validators=[validate_desc])
    awardAmount = models.IntegerField(max_length=5, null=True, validators=[validate_amt])
    awardedMember = models.ForeignKey(Person, null=True, blank=True)
    awardRecipient = models.CharField(max_length=60, null=True, blank=True)
    awardType = models.CharField(max_length=8, choices=kvp.EDU_AWARD_TYPES, null=True, blank=True)
    yearAwarded = models.IntegerField(max_length=4, choices=kvp.EDU_YEAR_CHOICES, null=True, blank=True)

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='award:edu_detail', kwargs={'pk': self.pk})

    # Method: __str__
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description.__str__()

    #Method: clean
    #Purpose Cleans the model before submitting to database
    def clean(self):
            # First, ensure both the member and recipient have been entered
            if (self.awardedMember != None and self.awardRecipient != None and self.awardRecipient != ""):
                if EducationAward.objects.exclude(id=self.id).filter(awardedMember=self.awardedMember).filter(awardRecipient=self.awardRecipient).count() > 0:
                    raise ValidationError('Cannot assign recipient to more than one award')
            else:
                if self.awardedMember != None and (self.awardRecipient == None or self.awardRecipient == ""):
                    raise ValidationError('Cannot assign an award with only a member')
                elif self.awardedMember == None and (self.awardRecipient != None or self.awardRecipient != ""):
                    raise ValidationError('Cannot assign an award without an associcated member')


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

    def clean(self):
       if self.endDate.__str__() < self.startDate.__str__():
            raise ValidationError("End Date must be the same as or come after start date")

