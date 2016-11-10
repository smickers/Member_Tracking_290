from __future__ import unicode_literals
from .validators import *
from django.db import models
from django.core.validators import MaxValueValidator


class Case(models.Model):
    lead = models.IntegerField(max_length=9)
    complainant = models.IntegerField(max_length=9)
    campus = models.CharField(max_length=20)
    school = models.CharField(max_length=255)
    caseType = models.CharField(max_length=50, validators=[validate_case_type])
    status = models.CharField(max_length=50, validators=[validate_status])
    additionalMembers = models.TextField(blank=True)
    additionalNonMembers = models.TextField(blank=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, validators=[validate_date])


class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.TextField()
    caseMember = models.CharField(max_length=18, unique='true', null='true')
