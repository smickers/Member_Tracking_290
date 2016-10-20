from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Person(models.Model):
    GENDER_CHOICE = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNDEFINED', 'Undefined'),
    )

    CAMPUS_CHOICE = (
        ('SASKATOON', 'SASKATOON'),
        ('REGINA', 'REGINA'),
        ('MOOSEJAW', 'MOOSE JAW'),
        ('PA', 'PRINCE ALBERT'),
    )

    POSITION_CLASS_CHOICE = (
        ('FTO', 'Full-time ongoing'),
        ('FTED', 'Full-time end dated'),
        ('PTO', 'Part-time ongoing'),
        ('PTED', 'Part-time end dated'),
    )

    memberID = models.IntegerField()
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    socNum = models.IntegerField()
    city = models.CharField(max_length=20)
    mailAddress = models.CharField(max_length=30)
    mailAddress2 = models.CharField(max_length=30, null=True, blank=True)
    pCode = models.CharField(max_length=6)
    bDay = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    hPhone = models.CharField(max_length=13, null=True, blank=True)
    cPhone = models.CharField(max_length=13, null=True, blank=True)
    hEmail = models.EmailField()
    campus = models.CharField(max_length=20, choices=CAMPUS_CHOICE)
    jobType = models.CharField(max_length=30, choices=POSITION_CLASS_CHOICE)
    committee = models.CharField(max_length=30)
    memberImage = models.CharField(max_length=30, blank=True, null=True)

    def clean(self):
        if self.memberID > 999999999:
            raise ValueError("error here")

    def get_absolute_url(self):
        return reverse(viewname='add_member:member_add')

