from __future__ import unicode_literals
from .validators import *
from django.db import models
from django.core.urlresolvers import reverse
import datetime
from add_member.models import Person
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

'''
Name:       CaseSatellite
Purpose:    This is a satellite location to be selected. Saves data to the DB.
'''
class CaseSatellite(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

'''
Name:       CasePrograms
Purpose:    This model is for the Programs to be chosen when a valid school is picked. Saves to DB.
'''
class CasePrograms(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

'''
Name:       Case
Purpose:    This is the model for the case. This is used by the web page to help generate the form. And saves data to the DB.
'''
#if __name__ == '__main__':
class Case(models.Model):
    CAMPUS_CHOICES = [
        ('Saskatoon', 'Saskatoon'),
        ('Regina', 'Regina'),
        ('MJ', 'Moose Jaw'),
        ('PA', 'Prince Albert'),
    ]

    TYPE_CHOICES = [
        ("GRIEVANCES - INDIVIDUAL", "GRIEVANCES - INDIVIDUAL"),
        ("GRIEVANCES - GROUP", "GRIEVANCES - GROUP"),
        ("GRIEVANCES - POLICY", "GRIEVANCES - POLICY"),
        ("GRIEVANCES - CLASSIFICATION", "GRIEVANCES - CLASSIFICATION"),
        ("GRIEVANCES - COMPLAINTS", "GRIEVANCES - COMPLAINTS"),
        ("DISABILITY CLAIMS", "DISABILITY CLAIMS"),
        ("ARBITRATION", "ARBITRATION"),
        ("COMPLAINT", "COMPLAINT")
    ]

    STATUS_CHOICES = [
        ("OPEN", "OPEN"),
        ("CLOSED", "CLOSED"),
        ("PENDING", "PENDING"),
        ("ACTION REQ'D - MGMT", "ACTION REQ'D - MGMT"),
        ("ACTION REQ'D SPFA", "ACTION REQ'D SPFA")
    ]

    SCHOOL_CHOICES = [
        ("School of Business", "School of Business"),
        ("School of Construction", "School of Construction"),
        ("School of Health Sciences", "School of Health Sciences"),
        ("School of Human Services and Community Safety", "School of Human Services and Community Safety"),
        ("School of Information and Communications Technology", "School of Information and Communications Technology"),
        ("School of Mining, Energy and Manufacturing", "School of Mining, Energy and Manufacturing"),
        ("School of Natural Resources and Built Environment", "School of Natural Resources and Built Environment"),
        ("School of Nursing", "School of Nursing"),
        ("School of Transportation", "School of Transportation"),
        ("Other", "Other"),
    ]

    DEPARTMENT_CHOICES = [
        ("Learning Technologies", "Learning Technologies"),
        ("ILDC", "ILDC"),
        ("Library", "Library"),
        ("PLAR", "PLAR"),
        ("Simulation Lab", "Simulation Lab"),
        ("Student Development", "Student Development"),
        ("Learning Services", "Learning Services"),
        ("Fitness Centre", "Fitness Centre")
    ]

    lead = models.IntegerField(max_length=9)
    complainant = models.ForeignKey(Person, related_name='case_complainant')
    campus = models.CharField(choices=CAMPUS_CHOICES, max_length=25, validators=[validate_location], default="Saskatoon")
    satellite = models.CharField(max_length=50, default=None, null=True, blank=True)
    school = models.CharField(choices=SCHOOL_CHOICES, max_length=255)
    program = models.ForeignKey(CasePrograms, default=None, null=True, blank=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=255, null=True, default=None, blank=True)
    caseType = models.CharField(choices=TYPE_CHOICES, max_length=50, validators=[validate_case_type])
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, blank=True, validators=[validate_status])
    additionalMembers = models.ManyToManyField(Person, default=None, null=True, blank=True)
    additionalNonMembers = models.TextField(blank=True, null=True)
    docs = models.TextField(blank=True, null=True)
    logs = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True, default=datetime.date.today, validators=[validate_date])

    def get_absolute_url(self):
        return reverse(viewname='cases:case_detail', kwargs={'pk': self.pk})

    def clean(self):
        if len(self.status) == 0:
            self.status = 'OPEN'
        if self.program is not None:
            self.department = None

    def __str__(self):
        return self.complainant.id.__str__()





class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.TextField()



@receiver(m2m_changed, sender=Case.additionalMembers.through)
def additional_member_signal(sender, **kwargs):
    #print("----------------- SIGNAL CALLED -----------------------")
    #print("ARGS: " + kwargs.__str__())
    pks = kwargs.pop('pk_set', None)
    instance = kwargs.pop('instance', None)
    complainant = instance.complainant
    #print (pks)
    #print "Sender: "
    #print vars(sender)
    #print "Complainant: "
    #print vars(complainant)
    validate_additional_members(complainant, pks)
    #pass

