from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *


# Create your models here.
class Committee(models.Model):
    """name, status"""

    # bound field choices for STATUS field
    COM_STATUS = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    name = models.CharField(max_length=40, validators=[validate_com_name])
    status = models.IntegerField(choices=COM_STATUS, validators=[validate_status])

    # When the model is updated, re-route the user to the com_detail URL
    def get_absolute_url(self):
        return reverse(viewname='add_com:committee_detail', kwargs={'pk': self.pk})

    # Print the name of the Committee in a user-readable format.
    def __str__(self):
        return self.name
