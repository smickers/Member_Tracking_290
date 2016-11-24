from __future__ import unicode_literals

from django.db.transaction import on_commit

from .validators import *
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse
import datetime



# Creating the model for the case
class Case(models.Model):
    STATUS = [
        ("OPEN","OPEN"),
        ("CLOSED","CLOSED"),
        ("PENDING","PENDING"),
        ("ACTION REQ'D - MGMT","ACTION REQ'D - MGMT"),
        ("ACTION REQ'D SPFA","ACTION REQ'D SPFA"),
    ]

    CASE_TYPE = [
        ("GRIEVANCES - INDIVIDUAL","GRIEVANCES - INDIVIDUAL"),
        ("GRIEVANCES - GROUP","GRIEVANCES - GROUP"),
        ("GRIEVANCES - POLICY","GRIEVANCES - POLICY"),
        ("GRIEVANCES - CLASSIFICATION","GRIEVANCES - CLASSIFICATION"),
        ("GRIEVANCES - COMPLAINTS","GRIEVANCES - COMPLAINTS"),
        ("DISABILITY CLAIMS","DISABILITY CLAIMS"),
        ("ARBITRATION","ARBITRATION"),
        ("COMPLAINT","COMPLAINT"),
    ]
    CAMPUS_CHOICE = [
        ('Saskatoon', 'Saskatoon'),
        ('Regina', 'Regina'),
        ('Moose Jaw', 'Moose Jaw'),
        ('Prince Albert', 'Prince Albert'),
    ]
    SCHOOLS=[
        ("School of Business","Business"),
        ("School of Construction", "Construction"),
        ("School of Health Sciences", "Health Sciences"),
        ("School of Hospitality and Tourism", "Hospitality and Tourism"),
        ("School of Human Services and Community Safety", "Human Services and Community Safety"),
        ("School of Information and Communications Technology", "Information and Communications Technology"),
        ("School of Mining, Energy and Manufacturing", "Mining, Energy and Manufacturing"),
        ("School of Natural Resources and Built Environment", "Natural Resources and Built Environment"),
        ("School of Nursing", "Nursing"),
        ("School of Transportation", "Transportation"),
    ]


    #for another story - have both departments and non school departments as valid
    """NON_SCHOOL_DEPARTMENTS=[
        ("Fitness Centre", "Fitness Centre"),
        ("ILDC", "ILDC"),
        ("Learning Services", "Learning Services"),
        ("Learning Technologies","Learning Technologies"),
        ("Library","Library"),
        ("PLAR","PLAR"),
        ("Simulation Lab","Simulation Lab"),
        ("Student Development","Student Development"),
    ]"""

    lead = models.IntegerField(max_length=9)
    complainant = models.IntegerField(max_length=9)
    campus = models.CharField(choices=CAMPUS_CHOICE, default='Saskatoon', max_length=20)
    school = models.CharField(choices=SCHOOLS, default='Business', max_length=255)
    department = models.CharField(max_length=255, null=True)
    caseType = models.CharField(choices=CASE_TYPE, max_length=50, default='GRIEVANCES - INDIVIDUAL', validators=[validate_case_type])
    status = models.CharField(choices=STATUS,  default='OPEN', max_length=50, blank=True,validators=[validate_status])
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
