from __future__ import unicode_literals

from django.db import models
import datetime
import validators
from django.core.urlresolvers import reverse


# Creating our model here. It has a name, description, date, and location. Validation is done in a different class.
# This simply calls on that class for validation.
class Event(models.Model):
    name = models.CharField(max_length=20, validators=[validators.validate_name])
    description = models.CharField(max_length=50, blank=True, null=True, validators=[validators.validate_desc])
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=25, validators=[validators.validate_location])

    # Name: get_absolute_url
    # Function: This function gets the url record for this object then passes in the primary key from the created record
    #           and passes it in as a parameter
    # Returns:  a URL
    def get_absolute_url(self):
        return reverse(viewname='create_event:event_create_success', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' - ' + self.date.__str__() + ' - ' + self.location
