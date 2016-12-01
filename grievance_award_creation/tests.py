from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import GrievanceAward
from add_member.models import Person
from add_case.models import Case
from django.db import DataError
import datetime

class EventTest(TestCase):
    tempPerson = Person()
    person_pk = -1
    tempCase = Case()
    case_pk = -1
    def setUp(self):
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

        self.person_pk = Person.objects.get(memberID=1).pk

        self.tempCase = Case()
        self.tempCase.lead = 1
        self.tempCase.complainant = 1
        self.tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                          "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                          "natoque penatibus et magnis dis parturient montes, nascetur " \
                          "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
        self.tempCase.school = "School of Business"
        self.tempCase.department = "Business Certificate"
        self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase.status = "OPEN"
        self.tempCase.additionalMembers = 0
        self.tempCase.additionalNonMembers = ""
        self.tempCase.docs = None
        self.tempCase.logs = None
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()

        self.case_pk = Case.objects.get(lead=1).pk

# Test 1 - Validate that a valid recipient can be added to a GrievanceAward
# Input: Recipient is a valid PK
# Expected result: Record is saved successfully
    def test_valid_recipient(self):
        ga = GrievanceAward
        ga.recipient = self.person_pk
        ga.awardAmount = 500.00
        ga.description = ""
        ga.date = '2016-12-01'
        ga.full_clean()
        ga.save()
        self.assertTrue(True)

# Test 2 - Validate that an invalid recipient throws an error
# Input: Recipient is an invalid PK
# Expected result: Error is thrown, record is not saved to DB.
    def test_invalid_recipient(self):
        with self.assertRaises(ValidationError):
            ga = GrievanceAward
            ga.recipient = -3000
            ga.awardAmount = 500.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()

# Test 3 - Validate that a valid case can be linked to a GrievanceAward
# Input: case is a valid case PK
# Expected result: Record is saved successfully
    def test_valid_case(self):
        ga = GrievanceAward
        ga.recipient = self.person_pk
        ga.case = self.case_pk
        ga.awardAmount = 500.00
        ga.description = ""
        ga.date = '2016-12-01'
        ga.full_clean()
        ga.save()
        self.assertTrue(True)

# Test 4 - Validate that an invalid case cannot be linked to a GrievanceAward
# Input: case is an invalid case PK
# Expected result: Error is thrown, record is not saved.
    def test_valid_case(self):
        with self.assertRaises(ValidationError):
            ga = GrievanceAward
            ga.recipient = self.person_pk
            ga.case = -1
            ga.awardAmount = 500.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
            self.assertTrue(True)

# Test 5 - Award Amount - Lower Bounds
# Input: Award amount as 0.00
# Expected result: Error is thrown, record is not saved
    def test_amount_lower_invalid(self):
        with self.assertRaises(ValidationError):
            ga = GrievanceAward
            ga.recipient = self.person_pk
            ga.awardAmount = 0.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()

# Test 6 - Award Amount - Valid
# Input: Award amount as 100.00
# Expected result: Record is saved to the DB.
    def test_award_amount_valid(self):
            ga = GrievanceAward
            ga.recipient = self.person_pk
            ga.awardAmount = 100.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
            self.assertTrue(True)

# Test 7 - Award Amount - Upper bounds
# Input: Award amount as 99999.99
# Expected result: Record is saved to the DB.
    def test_award_upper_valid(self):
            ga = GrievanceAward
            ga.recipient = self.person_pk
            ga.awardAmount = 99999.99
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
            self.assertTrue(True)

# Test 8 - Award Amount - Upper Bounds Invalid
# Input: Award amount as 100000.00
# Expected result: Error is thrown, record is not saved
    def test_amount_upper_invalid(self):
        with self.assertRaises(ValidationError):
            ga = GrievanceAward
            ga.recipient = self.person_pk
            ga.awardAmount = 100000.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()