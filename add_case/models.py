from __future__ import unicode_literals
from .validators import *
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse
import datetime


# Creating the model for the case
class Case(models.Model):
    lead = models.IntegerField(max_length=9)
    complainant = models.IntegerField(max_length=9)
    campus = models.CharField(max_length=20)
    school = models.CharField(max_length=255)
    department = models.CharField(max_length=255, null=True)
    caseType = models.CharField(max_length=50, validators=[validate_case_type])
    status = models.CharField(max_length=50, blank=True, default='OPEN', validators=[validate_status])
    additionalMembers = models.IntegerField(max_length=9, blank=True, null=True)
    additionalNonMembers = models.TextField(blank=True, null=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, default=datetime.date.today, validators=[validate_date])

    def clean(self):
        if len(self.status) == 0:
            self.status = 'OPEN'

    def get_absolute_url(self):
        return reverse(viewname='add_case:case_add')
