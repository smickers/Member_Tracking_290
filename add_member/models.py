from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db import IntegrityError
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
    pCode = models.CharField(max_length=7)
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
            raise ValueError("Member ID should be less than 9 digits")

        if self.socNum > 999999999:
            raise ValueError("SIN should be less than 9 digits")

        if len(self.firstName) == 0:
            raise IntegrityError("First name is required")

        if len(self.firstName) > 30:
            raise ValueError("First Name should be lesser than 30 characters")

        if len(self.middleName) == 0:
            raise IntegrityError("Middle name is required")

        if len(self.middleName) > 30:
            raise ValueError("Middle Name should be lesser than 30 characters")

        if len(self.lastName) == 0:
            raise IntegrityError("Last name name is required")

        if len(self.lastName) > 30:
            raise ValueError("Last Name should be lesser than 30 characters")

        if len(self.mailAddress) == 0:
            raise IntegrityError("Mail Address is required")

        if len(self.mailAddress) > 50:
            raise ValueError("Mail Address must be less than 50 characters")

        if len(self.mailAddress2) == 0:
            raise IntegrityError("Mail Address is required")

        if len(self.mailAddress2) > 50:
            raise ValueError("Mail Address must be less than 50 characters")

        if len(self.city) == 0:
            raise IntegrityError("City is required")

        if len(self.city) > 20:
            raise ValueError("City Field must be less than 20 characters")

    def get_absolute_url(self):
        return reverse(viewname='add_member:member_add')

