# SPFA MT CST Project
#  November 7, 2016
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from add_member.models import Person
from datetime import date
from django.db import models
from spfa_mt import kvp, settings
from django.core.exceptions import ValidationError


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
    contactCode = models.CharField(max_length=12, choices=kvp.CONTACT_LOG_STATUSES, default='Phone')

    # Function: get_absolute_url
    # Purpose: Returns a URL to redirect the user to after submitting
    # a new contact log entry.
    # Parameters:
    # self - the calling object
    # Returns: a URL to redirect the user to after submitting the form.
    def get_absolute_url(self): 
        return reverse(viewname='contact_log_creation:details', kwargs={'pk': self.pk})

    # Function: __str__
    # Purpose: toString method for a contactLog object
    # Returns: A string representing the current object
    def __str__(self):
        return self.member.__str__() + " - " + self.description + " " + self.date.__str__()

    # Function: containsFile
    # Purpose: Returns true or false, based on whether or not a file is associated with this
    # contact log
    # Returns: boolean
    @property
    def containsfile(self):
        return ContactLogFile.objects.filter(relatedContactLog=self.id).count() != 0

    # Overrides the clean method to ensure contact code validation.
    def clean(self):
        # If the code, being a single-character string, is not in the first part of the tuple, in the list of tuples,
        if self.contactCode not in kvp.CONTACT_LOG_STATUSES[0]:
            # raise an error
            raise ValidationError("Please select an option from the list of choices.")


# Class that creates a ContactLogFile object, which lets us associate a file (document) to a contact log
class ContactLogFile(models.Model):
    # Related fields:
    fileName = models.FileField(upload_to='contactlogs/', blank=True, null=True)
    fileDesc = models.CharField(max_length=50, blank=True, null=True)
    relatedContactLog = models.ForeignKey(contactLog)

    """
       Method: clean
       Purpose: Responsible for validating/cleaning files.
               Raises exception if problem occurs
       """
    def clean(self):
        super(ContactLogFile, self).clean()
        if self.fileName.size > settings.MAX_FILE_SIZE:
            """Check if the uploaded file has a valid file size"""
            raise ValidationError("File is too large")

        if self.fileName.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
            """ Check if the uploaded file has a valid file extension """
            raise ValidationError("Invalid File Extension")

    def __str__(self):
        return str(self.fileName.name)
