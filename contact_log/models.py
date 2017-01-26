# SPFA MT CST Project
# November 7, 2016
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from add_member.models import Person


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
    member = models.ForeignKey(Person, validators=[validate_member], blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=150, blank=True, null=True)

    # Function: clean
    # Purpose: Ensures all variables in this object
    # are in the correct format for storage in the DB.
    # Also saves the object to the DB.
    # Parameters:
    # self - the calling object
    # Returns: Nothing, but can throw an exception
    # if a value doesn't meet its requirements.
    def clean(self):
        print "I'm here!"
        #Member ID validation
        #self.validateMemberID()
        # Date validation
        #if not self.validateDate(str(self.date)):
            #raise ValueError("An invalid date was entered!")
        # Contact description validation
        #self.validateDescription()

    # Function: get_absolute_url
    # Purpose: Returns a URL to redirect the user to after submitting
    # a new contact log entry.
    # Parameters:
    # self - the calling object
    # Returns: a URL to redirect the user to after submitting the form.
    def get_absolute_url(self):
        return reverse(viewname='contact_log_creation:success', kwargs={'pk':self.pk})
