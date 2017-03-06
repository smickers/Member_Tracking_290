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
    grievanceType = models.CharField(max_length=1, choices=GRIEVANCE_TYPES, default='M')
    case = models.ForeignKey(Case, related_name="ga_case")
    awardAmount = models.FloatField(default=500.00, validators=[validators.validate_award_amt])
    description = models.CharField(max_length=1000, null=True,blank=True, validators=[validators.validate_description])
    date = models.DateField(default=date.today())

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='grievance_award_creation:create_grievance_award_success', kwargs={'pk': self.pk})

    @property
    def recipient(self):
        """
        Returns the recipient of a case
        :return: recipients/recipient related to the case
        """
        if self.case.caseType == 7: #return the primary complainant
            return self.case.complainant
        else:
            # combine additional members to the primary complainant
            return list(self.case.additionalMembers.all()).append(self.case.complainant)

    # Method: __str__ (toString)
    # Purpose: Return a string representation of this object.
    def __str__(self):
        return "Grievance Type: " + self.grievanceType + "\nDescription: " + self.description

    # def clean(self, *args, **kwargs):
    #     """
    #     Documentation: https://docs.djangoproject.com/en/1.10/ref/models/instances/
    #     """
    #
    #     # if self.case.caseType > 2:             # if it is a type of grievance
    #     #     self.recipient.add(self.case.complainant)
    #     #     if self.case.caseType != 7:        # if the grievance type is for policy
    #     #         for single_member in self.case.additionalMembers.all():
    #     #             self.recipient.add(single_member)
    #     #         self.grievanceType = 'P'
    #     #     else:
    #     #         self.grievanceType = 'M'
    #     )
    #     super(GrievanceAward, self).clean(*args, **kwargs


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
        if(self.file.size > MAX_FILE_SIZE):
            """Check if the uploaded file has a valid file size"""
            raise ValidationError("File is too large")

        if(self.file.name.split(".")[-1] not in FILE_EXT_TO_ACCEPT):
            """ Check if the uploaded file has a valid file extension """
            raise ValidationError("Invalid File Extension")

    def __str__(self):
        return str(self.file.name)