from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=25)

# def clean(self):
# TODO think of later
