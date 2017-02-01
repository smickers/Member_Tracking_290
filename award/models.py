from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Models for Education Awards
class EducationAward(models.Model):
    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True, help_text="Enter a description here.")
    award_amount = models.IntegerField(max_length=5, null=True, help_text="1250")

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='awards:create_edu_award_success', kwargs={'pk': self.pk})

    # Method: __str__ (toString)
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description + " ($" + self.award_amount + ")"
