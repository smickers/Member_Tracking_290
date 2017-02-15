# SPFA MT CST Project
#  November 7, 2016
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from add_member.models import Person
from datetime import date
from django.db import models


# Contact Log Class
# Purpose: This class will hold a contact log, and
# all attributes associated with a contact log. This
# class extends the default Model class.
class contactLog(models.Model):
    # A contact log will include a memberID, date of contact,
    # and description
    member = models.ForeignKey(Person, blank=True, null=True)
    date = models.DateField(default=date.today())
    description = models.CharField(max_length=150, blank=True, null=True)

    # Function: get_absolute_url
    # Purpose: Returns a URL to redirect the user to after submitting
    # a new contact log entry.
    # Parameters:
    # self - the calling object
    # Returns: a URL to redirect the user to after submitting the form.
    def get_absolute_url(self):
        return reverse(viewname='contact_log_creation:contact_log_list_default', kwargs={})

    # Function: __str__
    # Purpose: toString method for a contactLog object
    # Returns: A string representing the current object
    def __str__(self):
        return self.member.__str__() + " - " + self.description + " " + self.date.__str__()


class ContactLogFile(models.Model):

    fileName = models.CharField()
    description = models.CharField()
    relatedCase = models.ForeignKey(contactLog)

    # Leaving the stub here, unused ATM but it will be used later on to clean our uploaded files.
    # def clean(self):
