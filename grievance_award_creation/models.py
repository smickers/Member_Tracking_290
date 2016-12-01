from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GrievanceAward:
    GRIEVANCE_TYPES = [
        ('M', 'Member'),
        ('P', 'Policy'),
    ]

    grievanceType = models.CharField(choices=GRIEVANCE_TYPES)
    recipient = models.ManyToManyField()
    case = models.ManyToManyField(null=True, blank=True)
    awardAmount = models.DecimalField(min_value=0.01, max_value=999999.99)
    description = models.CharField(max_length=1000, null=True,blank=True)
    date = models.DateField()
