from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *
from django import forms
from spfa_mt import kvp


# Create your models here.
class Committee(models.Model):
    """name, status"""

    name = models.CharField(max_length=40, validators=[validate_com_name])
    status = models.IntegerField(choices=kvp.COM_STATUS, default='1', validators=[validate_status])

    # Other apps in the system use a function to re-direct upon success; as that is neither a
    # requirement nor really necessary/efficient I didn't bother with it, hence why the code
    # is no longer here.

    # Print the name of the Committee in a user-readable format.
    def __str__(self):
        return self.name

    # This method will redirect the user to the detail page of the current committee.
    # It is currently only called by editing a committee.
    def get_absolute_url(self):
        return reverse(viewname='add_com:committee_detail', kwargs={'pk': self.pk})
