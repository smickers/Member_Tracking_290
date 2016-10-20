from __future__ import unicode_literals

from django.db import models


class Case(models.Model):
    lead = models.IntegerField(max_length=9)
    complainant = models.IntegerField(max_length=9)
    campus = models.CharField(max_length=20)
    school = models.CharField(max_length=255)
    caseType = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    additionalMembers = models.IntegerField(max_length=9)
    additionalNonMembers = models.TextField()
    docs = models.TextField()
    logs = models.TextField()

