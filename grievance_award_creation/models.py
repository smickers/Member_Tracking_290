from __future__ import unicode_literals
from add_member.models import Person
from add_case.models import Case
from django.db import models
import validators
from spfa_mt.settings import MAX_FILE_SIZE, FILE_EXT_TO_ACCEPT
from django.core.urlresolvers import reverse
from datetime import date
from django.core.exceptions import ValidationError

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
    grievanceType = models.CharField(max_length=1, choices=GRIEVANCE_TYPES, validators=[validators.validate_grievance_type], default='M')
    recipient = models.ForeignKey(Person, validators=[validators.validate_recipient])
    #recipient = models.CharField(max_length=50, validators=[validators.validate_recipient])
    case = models.ForeignKey(Case, validators=[validators.validate_case])
    #case = models.CharField(max_length=50, validators=[validators.validate_case],blank=True, null=True)
    awardAmount = models.FloatField(default=500.00, validators=[validators.validate_award_amt])
    description = models.CharField(max_length=1000, null=True,blank=True, validators=[validators.validate_description])
    date = models.DateField(default=date.today())

    # Default get_absolute_url method
    def get_absolute_url(self):
        return reverse(viewname='grievance_award_creation:create_grievance_award_success', kwargs={'pk': self.pk})

    # Method: clean
    # Purpose: Validate attribute values.
    def clean(self):
        validators.validate_grievance_type(self.grievanceType)
        #validators.validate_recipient(self.recipient)
        #validators.validate_case(self.case)
        validators.validate_award_amt(self.awardAmount)
        validators.validate_description(self.description)

    # Method: __str__ (toString)
    # Purpose: Return a string representation of this object.
    def __str__(self):
        # Get the complainant
        complainant = Person.objects.get(id=self.recipient)
        return self.id.__str__() + " - " + complainant.firstName + " " + complainant.lastName

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