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
        ("Business","Business"),
        ("Construction", "Construction"),
        ("Health Sciences", "Health Sciences"),
        ("Hospitality and Tourism", "Hospitality and Tourism"),
        ("Human Services and Community Safety", "Human Services and Community Safety"),
        ("Information and Communications Technology", "Information and Communications Technology"),
        ("Mining, Energy and Manufacturing", "Mining, Energy and Manufacturing"),
        ("Natural Resources and Built Environment", "Natural Resources and Built Environment"),
        ("Nursing", "Nursing"),
        ("Transportation", "Transportation"),
    ]


    DEPARTMENTS=[
        ("Fitness Centre", "Fitness Centre"),
        ("ILDC", "ILDC"),
        ("Learning Services", "Learning Services"),
        ("Learning Technologies","Learning Technologies"),
        ("Library","Library"),
        ("PLAR","PLAR"),
        ("Simulation Lab","Simulation Lab"),
        ("Student Development","Student Development"),
    ]

    lead = models.IntegerField(max_length=9)
    #complainant = models.IntegerField(max_length=9)
    #IMPORTANT: NEED TO CHANGE TEST CASES BEFORE DOING THIS
    #note for future references: the select box will show what the parent's to string method returns
    complainant = models.ForeignKey('add_member.Person', on_delete=models.CASCADE, blank=True)
    campus = models.CharField(choices=CAMPUS_CHOICE, default='Saskatoon', max_length=20)
    school = models.CharField(choices=SCHOOLS, default='Business', max_length=255)
    department = models.CharField(choices=DEPARTMENTS,default='Learning Technologies', max_length=255, null=True)
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
