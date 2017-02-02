from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *


# Models for Education Awards
class EducationAward(models.Model):
    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True, validators=[validate_desc])
    award_amount = models.IntegerField(max_length=5, null=True, validators=[validate_amt])

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='award:edu_detail', kwargs={'pk': self.pk})

    # Method: __str__
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description.__str__()
