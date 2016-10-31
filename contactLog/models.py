from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.
class contactLog(models.Model):
    memberID = models.IntegerField()
    date = models.DateField(default=date.today())
    description = models.TextField(max_length=150)

    def clean(self):
        if self.memberID > 999999999:
            raise ValueError("Member ID must be 9 digits or less!")
        if self.memberID < 1:
            raise ValueError("Member ID must be a positive number!")
        if not self.validateDate(self.date):
            raise ValueError("An invalid date was entered!")
        if len(self.description) > 150:
            raise ValueError("The description is limited to 150 characters!")

