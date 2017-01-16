from __future__ import unicode_literals
from .validators import *
from django.db import models
from django.core.urlresolvers import reverse
import datetime
from add_member.models import Person


class CaseSatellite(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "ID " + self.id.__str__() + ": " + self.name


class Case(models.Model):
    CAMPUS_CHOICES = [
        ('Saskatoon', 'Saskatoon'),
        ('Regina', 'Regina'),
        ('MJ', 'Moose Jaw'),
        ('PA', 'Prince Albert'),
    ]

    TYPE_CHOICES = [
        ("G-I", "GRIEVANCES - INDIVIDUAL"),
        ("G-G", "GRIEVANCES - GROUP"),
        ("G-P", "GRIEVANCES - POLICY"),
        ("G-CLASS", "GRIEVANCES - CLASSIFICATION"),
        ("G-COMP", "GRIEVANCES - COMPLAINTS"),
        ("DC", "DISABILITY CLAIMS"),
        ("A", "ARBITRATION"),
        ("C", "COMPLAINT")
    ]

    STATUS_CHOICES = [
        ("O", "OPEN"),
        ("C", "CLOSED"),
        ("P", "PENDING"),
        ("A-R-M", "ACTION REQ'D - MGMT"),
        ("A-R-S", "ACTION REQ'D SPFA")
    ]

    SCHOOL_CHOICES = [
        ("")
    ]

    lead = models.IntegerField(max_length=9)
    complainant = models.ForeignKey(Person, related_name='case_complainant')
    campus = models.CharField(choices=CAMPUS_CHOICES, max_length=25, validators=[validate_location], default="Saskatoon")
    satellite = models.ForeignKey(CaseSatellite, default=None, null=True, blank=True)
    school = models.CharField(max_length=255)
    department = models.CharField(max_length=255, null=True)
    caseType = models.CharField(choices=TYPE_CHOICES, max_length=50, validators=[validate_case_type])
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, validators=[validate_status], default="O")
    additionalMembers = models.ManyToManyField(Person, default=None, null=True, blank=True)
    additionalNonMembers = models.TextField(blank=True, null=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, default=datetime.date.today, validators=[validate_date])

    def get_absolute_url(self):
        return reverse(viewname='cases:case_detail', kwargs={'pk': self.pk})


    def clean(self):
        if len(self.status) == 0:
            self.status = 'OPEN'


class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.TextField()
