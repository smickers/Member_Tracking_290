from __future__ import unicode_literals

from django.db import models


class Case(models.Model):
    lead = models.IntegerField(max_length=9)
    complainant = models.IntegerField(max_length=9)
    campus = models.CharField(max_length=20)
    school = models.CharField(max_length=255)
    caseType = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=True)
    additionalMembers = models.IntegerField(max_length=9, blank=True, null=True)
    additionalNonMembers = models.TextField(blank=True, null=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
