from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from datetime import date
import datetime
from django.db import models
from .validators import *

# Create your models here.
class contactLog(models.Model):
    memberID = models.IntegerField(validators=[validate_memberID])
    date = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(max_length=150, null=True, blank=True, validators=[validate_description])

    def validateDate(self, toCheck):
        try:
            datetime.strptime(toCheck, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def clean(self):
        if self.memberID > 999999999:
            raise ValueError("Member ID must be 9 digits or less!")
        elif self.memberID < 1:
            raise ValueError("Member ID must be a positive number!")
        #if not self.validateDate(self.date):
         #   raise ValueError("An invalid date was entered!")

        #TODO - ENSURE THAT THIS VALIDATION IS BEING CALLED UPON SUBMISSION
        if len(self.description) > 150:
            raise ValueError("The description is limited to 150 characters!")

        #END TODO

    def get_absolute_url(self):
        return reverse(viewname='contact_log_creation:contact_log_add')