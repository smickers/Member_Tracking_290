from __future__ import unicode_literals
from add_member.models import Person
from add_case.models import Case
from django.db import models

# Create your models here.
class GrievanceAward(models.Model):

    GRIEVANCE_TYPES = [
        ('M', 'Member'),
        ('P', 'Policy'),
    ]

    grievanceType = models.CharField(max_length=1, choices=GRIEVANCE_TYPES)
    recipient = models.ManyToManyField(Person, blank=True)
    case = models.ManyToManyField(Case, blank=True)
    awardAmount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=1000, null=True,blank=True)
    date = models.DateField()
