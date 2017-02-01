from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Models for Education Awards
class EducationAward(models.Model):
    """Fields for data entry re: education awards"""
    description = models.CharField(max_length=150, null=True)
    award_amount = models.IntegerField(max_length=5, null=True)

    # TODO I need to make this into validators
    def clean(self):
        if len(str(self.award_amount)) > 5:
            raise ValueError("Amount must be greater than $0 and less than $10,000.")
        elif len(str(self.award_amount)) == 0:
            raise ValueError("Award value is required.")
        # elif not (int(self.award_amount) % 1 == 0):
        #     raise ValueError()

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='award:edu_detail', kwargs={'pk': self.pk})

    # Method: __str__
    # Purpose: Return a string representation of an education award. Shows the description, and the award amount.
    def __str__(self):
        return self.description.__str__()
