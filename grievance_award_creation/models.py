from __future__ import unicode_literals
from add_member.models import Person
from add_case.models import Case
from django.db import models
import validators
from django.core.urlresolvers import reverse
from datetime import date

class GrievanceFilesManager(models.Manager):
    def get_files(self, instance):
        return GrievanceFiles.objects.filter(award=instance)


# Class: GrievanceAward
# Purpose: The class for a grievance award.
class GrievanceAward(models.Model):

    GRIEVANCE_TYPES = [
        ('M', 'Member'),
        ('P', 'Policy')
    ]

    # Object properties
    grievanceType = models.CharField(max_length=1, choices=GRIEVANCE_TYPES, validators=[validators.validate_grievance_type], default='M')
    #recipient = models.ManyToManyField(Person, blank=True, validators=[validators.validate_recipient])
    recipient = models.CharField(max_length=50, validators=[validators.validate_recipient])
    #case = models.ManyToManyField(Case, blank=True, validators=[validators.validate_case])
    case = models.CharField(max_length=50, validators=[validators.validate_case],blank=True, null=True)
    awardAmount = models.FloatField(default=500.00, validators=[validators.validate_award_amt])
    description = models.CharField(max_length=1000, null=True,blank=True, validators=[validators.validate_description])
    date = models.DateField(default=date.today())
    files = GrievanceFilesManager()



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




class GrievanceFiles(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='/files/', )
    award = models.ForeignKey(GrievanceAward)
    description = models.CharField(max_length=50)

