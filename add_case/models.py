from __future__ import unicode_literals
from .validators import *
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import *
from django.core.urlresolvers import reverse
import datetime
from add_member.models import Person
from spfa_mt import kvp
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT


# Name:       CaseSatellite
# Purpose:    This is a satellite location to be selected. Saves data to the DB.
class CaseSatellite(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    # Name: __str__
    # Purpose: toString method
    # Returns: A string representation of the object.
    def __str__(self):
        return self.name


# Name:       CasePrograms
# Purpose:    This model is for the Programs to be chosen when a valid school is picked. Saves to DB.
class CasePrograms(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    # Name: __str__
    # Purpose: toString method
    # Returns: A string representation of the object.
    def __str__(self):
        return self.name


# Name:       Case
# Purpose:    This is the model for the case. This is used by the web page to help generate the form.
#               Also saves data to the DB.
class Case(models.Model):
    lead = models.IntegerField(max_length=9)
    complainant = models.ForeignKey(Person, related_name='case_complainant')
    campus = models.CharField(choices=kvp.CAMPUS_CHOICES.iteritems(), max_length=25, validators=[validate_location],
                              default="Saskatoon")
    satellite = models.CharField(max_length=50, default=None, null=True, blank=True)
    school = models.CharField(choices=kvp.SCHOOL_CHOICES.iteritems(), max_length=255)
    program = models.ForeignKey(CasePrograms, default=None, null=True, blank=True)
    department = models.CharField(choices=kvp.DEPARTMENT_CHOICES.iteritems(), max_length=255, null=True, default=None, blank=True)
    caseType = models.CharField(choices=kvp.TYPE_CHOICES.iteritems(), max_length=50, validators=[validate_case_type]) #TODO: Change to IntegerField
    status = models.CharField(choices=kvp.STATUS_CHOICES.iteritems(), max_length=50, blank=True, validators=[validate_status])
    additionalMembers = models.ManyToManyField(Person, default=None, null=True, blank=True)
    additionalNonMembers = models.TextField(blank=True, null=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, default=datetime.date.today, validators=[validate_date])

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='add_case:case_detail', kwargs={'pk': self.pk})

    # clean method
    # Purpose: Clean data before saving it to the database.
    def clean(self):
        if len(self.status) == 0:
            self.status = 'OPEN'
        if self.program is not None:
            self.department = None

    # Name: __str__
    # Purpose: toString method
    # Returns: A string representation of the object.
    def __str__(self):
        return self.complainant.__str__() + ' - ' + self.date.strftime("%d, %b. %Y")

    #TODO: Code this property to return the instance of the related Case Type (eg. Grivance Instance)
    """
    @property #Denotes that this a property
    def eval_case_types(self):
        pass
    """

# Class: CaseMembers
# Purpose: Joining class for Members to a Case.
class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.TextField()

# Class: CaseFiles
# Purpose: File wrapper for case files.
class CaseFiles(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True,blank=True,null=True)
    file = models.FileField(upload_to='case/',blank=True,null=True)
    case = models.ForeignKey(Case,blank=True,null=True)
    description = models.CharField(max_length=50,blank=True,null=True)


    """
    Method: clean
    Purpose: Responsible for validating/cleaning files.
            Raises exception if problem occurs
    """
    def clean(self):
        super(CaseFiles, self).clean()
        if (self.file.size > MAX_FILE_SIZE):
            """Check if the uploaded file has a valid file size"""
            raise ValidationError("File is too large")

        if (self.file.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT):
            """ Check if the uploaded file has a valid file extension """
            raise ValidationError("Invalid File Extension")


# This is called when the form submits and the many to many field has been changed
# It checks to see if the complainant is in the additionalMembers field and if so
# it removes it.
@receiver(m2m_changed, sender=Case.additionalMembers.through)
def additional_member_signal(sender, **kwargs):
    pks = kwargs.pop('pk_set', None)
    instance = kwargs.pop('instance', None)
    if instance.complainant.id in pks:
        pks.remove(instance.complainant.id)
