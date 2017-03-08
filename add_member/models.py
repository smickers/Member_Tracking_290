from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db import IntegrityError
from .validators import *
from django.core.validators import MaxValueValidator


# Create your models here.

class Person(models.Model):

    #bound fields choices for gender field
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNDEFINED', 'Undefined'),
    ]

    # bound fields choices for campus field
    CAMPUS_CHOICE = [
        ('SASKATOON', 'SASKATOON'),
        ('REGINA', 'REGINA'),
        ('MOOSEJAW', 'MOOSE JAW'),
        ('PA', 'PRINCE ALBERT'),
    ]

    # bound fields choices for position field
    POSITION_CLASS_CHOICE = [
        ('FTO', 'Full-time ongoing'),
        ('FTED', 'Full-time end dated'),
        ('PTO', 'Part-time ongoing'),
        ('PTED', 'Part-time end dated'),
    ]

    # bound fields choices for membership status field
    MEMBERSHIP_STATUS = [
        ('RESOURCE', 'RESOURCE'),
        ('COMCHAIR', 'COMMITTEE CHAIR'),
        ('RECORDER', 'RECORDER'),
    ]

    memberID = models.IntegerField(validators=[validate_ninedigits])
    firstName = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    middleName = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    lastName = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    socNum = models.IntegerField(validators=[validate_ninedigits])
    city = models.CharField(max_length=20, validators=[validate_rightstringlen20])
    mailAddress = models.CharField(max_length=50, validators=[validate_rightstringlen50])
    mailAddress2 = models.CharField(max_length=50, null=True, blank=True, validators=[validate_rightstringlen50])
    pCode = models.CharField(null=True, max_length=7, blank=True, validators=[validate_pCode])
    bDay = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    hPhone = models.CharField(max_length=13, null=True, blank=True, validators=[validate_numbers])
    cPhone = models.CharField(max_length=13, null=True, blank=True, validators=[validate_numbers])
    hEmail = models.EmailField()
    campus = models.CharField(max_length=20, choices=CAMPUS_CHOICE)
    jobType = models.CharField(max_length=30, choices=POSITION_CLASS_CHOICE)
    committee = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    memberImage = models.CharField(max_length=30, blank=True, null=True)
    programChoice = models.CharField(max_length=30, null=True, validators=[validate_rightstringlen30])
    membershipStatus = models.CharField(max_length=30, choices=MEMBERSHIP_STATUS, null=True)
    hireDate = models.DateField(null=True)

    #when model gets updated, user will be routed to thte member_detail url
    def get_absolute_url(self):
        return reverse(viewname='add_member:member_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.firstName + " " + self.lastName

    def clean(self):
        # Validate the postal code, if it has been entered
        if self.pCode:
            self.pCode = self.pCode.upper()
            if len(self.pCode) == 6:
                self.pCode = self.pCode[:3] + ' ' + self.pCode[3:]


class MemberFiles(models.Model):
    """"""