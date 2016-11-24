from __future__ import unicode_literals

from django.db import models
import datetime
import validators
from django.core.urlresolvers import reverse

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=20, validators=[validators.validate_name])
    description = models.CharField(max_length=50, blank=True, null=True, validators=[validators.validate_desc])
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=25, validators=[validators.validate_location])

    def get_absolute_url(self):
        return reverse(viewname='create_event:event_create_success', kwargs={'pk':self.pk})
