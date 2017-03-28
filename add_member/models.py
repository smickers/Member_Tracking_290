from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .validators import *

# Create your models here.
class PersonBase(models.Model):

    #bound fields choices for gender field
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNDEFINED', 'Undefined'),
    ]

    # bound fields choices for campus field
    CAMPUS_CHOICE = [
        ('SASKATOON', 'SASKATOON'),
        ('REGINA', 'REGINA'),
        ('MOOSEJAW', 'MOOSE JAW'),
        ('PA', 'PRINCE ALBERT'),
    ]

    # bound fields choices for position field
    POSITION_CLASS_CHOICE = [
        ('FTO', 'Full-time ongoing'),
        ('FTED', 'Full-time end dated'),
        ('PTO', 'Part-time ongoing'),
        ('PTED', 'Part-time end dated'),
    ]

    # bound fields choices for membership status field
    MEMBERSHIP_STATUS = [
        ('RESOURCE', 'RESOURCE'),
        ('COMCHAIR', 'COMMITTEE CHAIR'),
        ('RECORDER', 'RECORDER'),
    ]

    EMPLOYEE_STATUS = [
        ('A', 'ACTIVE'),
        ('T', 'TERMINATED')
    ]

    firstName = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    lastName = models.CharField(max_length=30, validators=[validate_rightstringlen30])
    # jobType = models.CharField(max_length=30, choices=POSITION_CLASS_CHOICE)  # TODO:  Accepts Employee Class Long Description
    jobType = models.CharField(max_length=50)
    membershipStatus = models.CharField(max_length=30, choices=MEMBERSHIP_STATUS, null=True, blank=True)
    hireDate = models.DateField( null=True, blank=True)  # TODO: change to current hire date

    class Meta:
        abstract = True


class Person(PersonBase):
    memberID = models.IntegerField(validators=[validate_ninedigits], null=True, blank=True)
    middleName = models.CharField(max_length=30, validators=[validate_rightstringlen30], null=True, blank=True)
    socNum = models.IntegerField(validators=[validate_ninedigits],  null=True, blank=True)
    city = models.CharField(max_length=20, validators=[validate_rightstringlen20],  null=True, blank=True)
    mailAddress = models.CharField(max_length=50, validators=[validate_rightstringlen50],  null=True, blank=True)
    mailAddress2 = models.CharField(max_length=50, null=True, blank=True, validators=[validate_rightstringlen50])
    pCode = models.CharField(null=True, max_length=7, blank=True, validators=[validate_pCode])
    bDay = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=PersonBase.GENDER_CHOICE, max_length=10,  null=True, blank=True)
    hPhone = models.CharField(max_length=13, null=True, blank=True, validators=[validate_numbers])
    cPhone = models.CharField(max_length=13, null=True, blank=True, validators=[validate_numbers])
    hEmail = models.EmailField(null=True, blank=True)
    # campus = models.CharField(max_length=20, choices=PersonBase.CAMPUS_CHOICE, null=True, blank=True)
    campus = models.CharField(max_length=20, null=True, blank=True)

    committee = models.CharField(max_length=30, validators=[validate_rightstringlen30],  null=True, blank=True)
    memberImage = models.CharField(max_length=30, blank=True, null=True)
    programChoice = models.CharField(max_length=30,blank=True, null=True, validators=[validate_rightstringlen30])
    posBeginDate = models.DateField(blank=True, null=True)
    posEndDate = models.DateField(blank=True, null=True)
    terminationDate = models.DateField(blank=True, null=True)
    employeeClass = models.CharField(blank=True, null=True, max_length=4)
    department = models.CharField(blank=True, null=True, max_length=50)
    jobSuffix = models.CharField(blank=True, null=True, max_length=4)
    posTitle = models.CharField(blank=True, null=True, max_length=50)
    position = models.CharField(blank=True, null=True, max_length=50)
    employeeStatus = models.CharField(blank=True, null=True, choices=PersonBase.EMPLOYEE_STATUS, max_length=1)

    # when model gets updated, user will be routed to the member_detail url
    class Meta:
        # docs: https://docs.djangoproject.com/en/1.10/ref/models/options/#unique-together
        unique_together = ("firstName", "lastName", "campus")


    def get_absolute_url(self):
        return reverse(viewname='add_member:member_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.firstName + " " + self.lastName

    def clean(self):
        # Validate the postal code, if it has been entered
        if self.pCode:
            self.pCode = self.pCode.upper()
            if len(self.pCode) == 6:
                self.pCode = self.pCode[:3] + ' ' + self.pCode[3:]


class PersonFile(models.Model):
    file = models.FileField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    # TODO: Add department field
    # FUNCTION:     containsFile
    # PURPOSE:      Returns true or false, based on whether or not a file is associated with this member
    # RETURNS:      boolean value: true if a file is associated to this Member, false otherwise.
    @property
    def containsfile(self):
        return MemberFiles.objects.filter(relatedMember=self.id).count() != 0

    # FUNCTION:     get_files
    # PURPOSE:      Returns all files associated to the relatedMember
    # RETURNS:      the array of files associated to the relatedMember
    @property
    def get_files(self):
        file_array = MemberFiles.objects.filter(relatedMember=self.id)
        return file_array

    # FUNCTION:     has_cl
    # PURPOSE:      Returns a boolean, indicating if there are contact logs related to the current member.
    # RETURNS:      True if there is more than one contact log related to the member; False otherwise.
    @property
    def has_cl(self):
        return self.contact_log_contactlog_related != 0


# Joining class for Members and their associated files:
class MemberFiles(models.Model):
    # Attributes
    dateUploaded = models.DateTimeField(auto_now=True, blank=True, null=True)
    fileName = models.FileField(upload_to='members/', blank=True, null=True, validators=[validate_file_ext])
    relatedMember = models.ForeignKey(Person, blank=True, null=True)
    fileDesc = models.CharField(max_length=50, blank=True, null=True)

    # FUNCTION:     clean()
    # PURPOSE:      Override the existing clean method, in order to perform some file validation
    def clean(self):
        super(MemberFiles, self).clean()
        if self.fileName.size > settings.MAX_FILE_SIZE:
            raise ValidationError('Upload size limit exceeded exception')
        if self.fileName.size == 0:
            raise ValidationError('The submitted file is empty.')
        if self.fileName.name.split(".")[-1] not in settings.FILE_EXT_TO_ACCEPT:
            # Check if the uploaded file has a valid file extension
            raise ValidationError("Invalid File Extension")

    # FUNCTION:     __str__()
    # PURPOSE:      Provide a readable name for the file we uploaded.
    # RETURNS:      fileName, as a string.
    def __str__(self):
        return str(self.fileName.name)
