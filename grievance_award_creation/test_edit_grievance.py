from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import GrievanceAward
from add_member.models import Person
from add_case.models import *
from django.db import DataError
import datetime


class AwardEditTest(TestCase):
    tempPerson = Person()
    tempPerson2 = Person()
    person_pk = -1
    tempCase = Case()
    case_pk = -1
    program = CasePrograms()
    ga = GrievanceAward()

    def setUp(self):
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

        self.tempPerson.memberID = 1
        self.tempPerson.firstName = 'First'
        self.tempPerson.middleName = 'Middle'
        self.tempPerson.lastName = 'Last'
        self.tempPerson.socNum = 123456789
        self.tempPerson.city = 'Sample City'
        self.tempPerson.mailAddress = 'Sample address'
        self.tempPerson.mailAddress2 = 'Sample Address 2'
        self.tempPerson.pCode = 's7k5j8'
        self.tempPerson.hPhone = '(306)812-1234'
        self.tempPerson.cPhone = '(306)812-1234'
        self.tempPerson.hEmail = 'sample@sample.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Commitee'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '2012-03-03'
        self.tempPerson.hireDate = '2012-03-03'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.membershipStatus = 'RESOURCE'
        self.tempPerson.programChoice = 'Sample Program'
        self.tempPerson.full_clean()
        self.tempPerson.save()

        self.tempPerson2.memberID = 1
        self.tempPerson2.firstName = 'Test'
        self.tempPerson2.middleName = 'This'
        self.tempPerson2.lastName = 'Person'
        self.tempPerson2.socNum = 123456789
        self.tempPerson2.city = 'Sample City'
        self.tempPerson2.mailAddress = 'Sample address'
        self.tempPerson2.mailAddress2 = 'Sample Address 2'
        self.tempPerson2.pCode = 's7k5j8'
        self.tempPerson2.hPhone = '(306)812-1234'
        self.tempPerson2.cPhone = '(306)812-1234'
        self.tempPerson2.hEmail = 'sample@sample.com'
        self.tempPerson2.campus = 'SASKATOON'
        self.tempPerson2.jobType = 'FTO'
        self.tempPerson2.committee = 'Sample Commitee'
        self.tempPerson2.memberImage = 'image.img'
        self.tempPerson2.bDay = '2012-03-03'
        self.tempPerson2.hireDate = '2012-03-03'
        self.tempPerson2.gender = 'MALE'
        self.tempPerson2.membershipStatus = 'RESOURCE'
        self.tempPerson2.programChoice = 'Sample Program'
        self.tempPerson2.full_clean()
        self.tempPerson2.save()

        # self.person_pk = Person.objects.get(memberID=1).pk

        self.tempCase = Case()
        self.tempCase.lead = self.tempPerson.id
        self.tempCase.complainant = self.tempPerson
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.program = self.program
        self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase.status = "OPEN"
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()

        self.ga.grievanceType = "M"
        self.ga.recipient = self.tempPerson.id
        self.ga.awardAmount = 500.00
        self.ga.description = ""
        self.ga.date = '2016-12-01'
        self.ga.full_clean()
        self.ga.save()

    def test_that_recipient_is_changed_to_different_member(self):
        self.ga.recipient = self.tempPerson2.id
        self.ga.clean()
        self.ga.save()

        assert self.ga.recipient == self.tempPerson2.id

    def test_that_recipient_is_changed_to_different_member(self):
        with self.assertRaises(ValidationError):
            self.ga.recipient = 78945648794
            self.ga.clean()
            self.ga.save()

    def test_that_amount_can_be_changed(self):
        self.ga.awardAmount = 9850
        self.ga.clean()
        self.ga.save()
        assert self.ga.awardAmount == 9850
