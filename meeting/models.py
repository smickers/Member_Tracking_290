from __future__ import unicode_literals

from django.db import models
from add_member.models import Person
from add_com.models import Committee
from datetime import date
from django.core.urlresolvers import reverse
from spfa_mt import settings
from .validators import *


# Class: Meeting
# Purpose: The class for a meeting

class Meeting(models.Model):

    # Meeting Attributes
    committee = models.ForeignKey(Committee, null=False, blank=False)
    liaison = models.CharField(max_length=10, null=False, blank=False)
    members_attending = models.ManyToManyField(Person)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField(default=date.today())

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='meeting:create_meeting_success', kwargs={'pk': self.pk})


class MeetingFiles(models.Model):
    # Attributes
    dateUploaded = models.DateTimeField(auto_now=True, blank=True, null=True)
    fileName = models.FileField(upload_to='meetings/', blank=True, null=True, validators=[validate_file_ext])
    relatedMeeting = models.ForeignKey(Meeting, blank=True, null=True)
    fileDesc = models.CharField(max_length=50, blank=True, null=True)

    # Function: clean()
    # Purpose: Override the existing clean method, in order to perform some file validation
    def clean(self):
        super(MeetingFiles, self).clean()
        if self.fileName.size > settings.MAX_FILE_SIZE:
            raise ValidationError('Upload size limit exceeded exception')
        if self.fileName.size == 0:
            raise ValidationError('The submitted file is empty.')
        if self.fileName.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
            # Check if the uploaded file has a valid extension
            raise ValidationError("Invalid File Extension")

    # Function: __str__()
    # Purpose: Provide a readable naem for the file we uploaded
    # Returns: filename, as a string.
    def __str__(self):
        return str(self.fileName.name)