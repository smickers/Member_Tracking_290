from __future__ import unicode_literals

from django.db import models

# Create your models here.

class meeting(models.Model):

    committee = models.ForeignKey