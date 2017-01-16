from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *
from django import forms


# Create your models here.
class Committee(models.Model):
    """name, status"""

    # bound field choices for STATUS field
    INACTIVE = 0
    ACTIVE = 1
    COM_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    name = models.CharField(max_length=40, validators=[validate_com_name])
    status = models.IntegerField(choices=COM_STATUS, default='1', validators=[validate_status])

    # Other apps in the system use a function to re-direct upon success; as that is neither a
    # requirement nor really necessary/efficient I didn't bother with it, hence why the code
    # is no longer here.

    # Print the name of the Committee in a user-readable format.
    def __str__(self):
        return self.name
