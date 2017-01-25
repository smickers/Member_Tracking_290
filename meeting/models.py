from __future__ import unicode_literals

from django.db import models
from add_member.models import Person
from add_com.models import Committee
from datetime import date
from django.core.urlresolvers import reverse

# Create your models here.


class Meeting(models.Model):

    committee = models.ForeignKey(Committee, null=False, blank=False)
    spfa_liason = models.CharField(max_length=50, null=False, blank=False)
    members_attending = models.ManyToManyField(Person)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField(default=date.today())

    def get_absolute_url(self):
        return reverse(viewname='meeting:create_meeting_success', kwargs={'pk': self.pk})
