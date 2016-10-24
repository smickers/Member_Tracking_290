from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.
class contactLog(models.Model):
    memberID = models.IntegerField()
    date = models.DateField(default=date.today())
    description = models.TextField(max_length=150)

