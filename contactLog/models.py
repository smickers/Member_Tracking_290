# SPFA MT CST Project
# November 7, 2016
from __future__ import unicode_literals
from django.core.urlresolvers import reverse


import datetime
from django.db import models
from .validators import *

# Contact Log Class
# Purpose: This class will hold a contact log, and
# all attributes associated with a contact log. This
# class extends the default Model class.
class contactLog(models.Model):
    # A contact log will include a memberID, date of contact,
    # and description
    memberID = models.IntegerField(validators=[validate_memberID], blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=150, blank=True, null=True)

    # Function: validateDate
    # Purpose: Takes in a date, and ensures
    # that the entered date is valid.
    # Parameters:
    # self - the calling object
    # toCheck - the entered date to validate
    # Returns: true/false, depending on whether the
    # date was valid or not
    def validateDate(self, toCheck):
        try:
            datetime.strptime(toCheck, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validateMemberID(self):
        if self.memberID:
            if self.memberID > 999999999:
                raise ValueError("Member ID must be 9 digits or less!")
            elif self.memberID < 1:
                raise ValueError("Member ID must be a positive number!")

    def validateDescription(self):
        if self.description:
            if not self.validateDate(str(self.date)):
                raise ValueError("An invalid date was entered!")
            # Contact description validation
            if self.description:
                if len(self.description) > 150:
                    raise ValueError("The description is limited to 150 characters!")

    # Function: clean
    # Purpose: Ensures all variables in this object
    # are in the correct format for storage in the DB.
    # Also saves the object to the DB.
    # Parameters:
    # self - the calling object
    # Returns: Nothing, but can throw an exception
    # if a value doesn't meet its requirements.
    def clean(self):

        #Member ID validation
        self.validateMemberID()
        # Date validation
        if not self.validateDate(str(self.date)):
            raise ValueError("An invalid date was entered!")
        # Contact description validation
        self.validateDescription()

    # Function: get_absolute_url
    # Purpose: Returns a URL to redirect the user to after submitting
    # a new contact log entry.
    # Parameters:
    # self - the calling object
    # Returns: a URL to redirect the user to after submitting the form.
    def get_absolute_url(self):
        return reverse(viewname='contact_log_creation:success', kwargs={'pk':self.pk})
