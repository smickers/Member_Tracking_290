from __future__ import unicode_literals
from add_member.models import Person
from add_case.models import Case
from django.db import models
import validators
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT
from django.core.urlresolvers import reverse
from datetime import date
from django.core.exceptions import ValidationError
from spfa_mt import kvp

"""
Class: GrievanceFilesManager
This class returns files belonging to a specific instance of an award
"""
class GrievanceFilesManager(models.Manager):

    """
    Method: get_files
    Purpose: returns files belonging to a specific instance of an award
    """
    def get_files(self, instance):
        return GrievanceFiles.objects.get(award_id=instance)


"""
Class: GrievanceAward
The class for a grievance award model.
"""
class GrievanceAward(models.Model):

    GRIEVANCE_TYPES = [
        ('M', 'Member'),
        ('P', 'Policy')
    ]
    # Object properties
    case = models.OneToOneField(Case)
    awardAmount = models.FloatField(default=500.00, validators=[validators.validate_award_amt])
    description = models.CharField(max_length=1000, null=True, blank=True, validators=[validators.validate_description])
    date = models.DateField(default=date.today())

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='add_case:case_detail', kwargs={'pk': self.case.pk})

    @property
    def recipient(self):
        return self.case.members

    @property
    def grievanceType(self):
        if self.case.caseType == kvp.TYPE_CHOICES[0][0]:  # if caseType is individual
            return GrievanceAward.GRIEVANCE_TYPES[0][0]   # GA type must be "member"
        else:
            return GrievanceAward.GRIEVANCE_TYPES[1][0]   # otherwise, "policy"


"""
Class: GrievanceFiles
Model wrapper for the file uploaded associated with grievance information
"""
class GrievanceFiles(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True,blank=True,null=True)
    file = models.FileField(upload_to='grievance/',blank=True,null=True)
    award = models.ForeignKey(GrievanceAward,blank=True,null=True)
    description = models.CharField(max_length=50,blank=True,null=True)

    """
    Method: clean
    Purpose: Responsible for validating/cleaning files.
            Raises exception if problem occurs
    """
    def clean(self):

        super(GrievanceFiles, self).clean()
        if self.file.size > MAX_FILE_SIZE:
            """Check if the uploaded file has a valid file size"""
            raise ValidationError("File is too large")

        if self.file.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT:
            """ Check if the uploaded file has a valid file extension """
            raise ValidationError("Invalid File Extension")

    def __str__(self):
        return str(self.file.name)
