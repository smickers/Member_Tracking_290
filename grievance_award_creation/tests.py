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
        self.tempCase.lead = self.tempPerson.id
        self.tempCase.complainant = self.tempPerson
        self.tempCase.campus = "Lorem ipsum"
        self.tempCase.school = "School of Business"
        self.tempCase.department = "Business Certificate"
        self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase.status = "OPEN"
        #self.tempCase.additionalMembers = 0
        #self.tempCase.additionalNonMembers = ""
        #self.tempCase.docs = None
        #self.tempCase.logs = None
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()



# Test 1 - Validate that a valid recipient can be added to a GrievanceAward
# Input: Recipient is a valid PK
# Expected result: Record is saved successfully
    def test_valid_recipient(self):
        ga = GrievanceAward()
        ga.grievanceType = "M"
        ga.recipient = self.tempPerson.id
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
            ga = GrievanceAward()
            ga.grievanceType = 'M'
            #ga.recipient = -3000
            ga.awardAmount = 500.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()

# Test 3 - Validate that a valid case can be linked to a GrievanceAward
# Input: case is a valid case PK
# Expected result: Record is saved successfully
    def test_valid_case(self):
        ga = GrievanceAward()
        ga.grievanceType = 'P'
        #ga.recipient = self.person_pk
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
            ga = GrievanceAward()
            #ga.recipient = self.person_pk
            ga.grievanceType = 'P'
            #ga.case = -1
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
            ga = GrievanceAward()
            ga.recipient = self.tempPerson.id
            ga.grievanceType = 'M'
            ga.awardAmount = 0.00
            ga.description = ""
            ga.date = '2016-12-01'
            #GrievanceAward.full_clean(ga)
            ga.full_clean()
            ga.save()

# Test 6 - Award Amount - Valid
# Input: Award amount as 100.00
# Expected result: Record is saved to the DB.
    def test_award_amount_valid(self):
            ga = GrievanceAward()
            ga.recipient = self.tempPerson.id
            ga.grievanceType = 'M'
            ga.awardAmount = 100.00
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
            self.assertTrue(True)

# Test 7 - Award Amount - Upper bounds
# Input: Award amount as 999999.99
# Expected result: Record is saved to the DB.
    def test_award_upper_valid(self):
            ga = GrievanceAward()
            ga.grievanceType = 'M'
            ga.recipient = self.tempPerson.id
            ga.awardAmount = 999999.99
            ga.description = ""
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
            self.assertTrue(True)

# Test 8 - Award Amount - Upper Bounds Invalid
# Input: Award amount as 1000000.00
# Expected result: Error is thrown, record is not saved
    def test_amount_upper_invalid(self):
            with self.assertRaises(ValidationError):
                ga = GrievanceAward()
                ga.recipient = self.tempPerson.id
                ga.awardAmount = 1000000.00
                ga.description = ""
                ga.date = '2016-12-01'
                ga.full_clean()
                ga.save()

# Test 9 - Empty Description
# Input: Description is left empty. All required fields are filled in.
# Expected result: Record is successfully saved to the DB
    def test_empty_description(self):
        ga = GrievanceAward()
        ga.recipient = self.tempPerson.id
        ga.grievanceType = 'M'
        ga.awardAmount = 100.00
        ga.description = ""
        ga.date = '2016-12-01'
        ga.full_clean()
        ga.save()
        self.assertTrue(True)

# Test 10 - 1000 Character Description
# Input: 1000 character description. All required fields are filled in.
# Expected result: Record is successfully saved to the DB
    def test_thousand_description(self):
        ga = GrievanceAward()
        ga.recipient = self.tempPerson.id
        ga.grievanceType = 'M'
        ga.awardAmount = 100.00
        ga.description = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N"
        ga.date = '2016-12-01'
        ga.full_clean()
        ga.save()
        self.assertTrue(True)

# Test 11 - 1001 Character Description
# Input: 1001 character description. All required fields are filled in.
# Expected result: Exception is raised. Record is not saved to the DB.
    def test_thousand_and_one_description(self):
        with self.assertRaises(ValidationError):
            ga = GrievanceAward()
            ga.grievanceType = 'M'
            ga.recipient = self.tempPerson.id
            ga.awardAmount = 100.00
            ga.description = "ALorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N"
            ga.date = '2016-12-01'
            ga.full_clean()
            ga.save()
