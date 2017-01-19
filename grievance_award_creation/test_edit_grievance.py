from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import GrievanceAward
from add_member.models import Person
from add_case.models import *
from django.db import DataError
import datetime

#Author David Letkeman; Brett Larose
#Class: AwardEditTest
#Purpose: Test Cases for editing a Grievance Award
#Date: Jan 19, 2017

class AwardEditTest(TestCase):
    tempPerson = Person()
    tempPerson2 = Person()
    person_pk = -1
    tempCase = Case()
    case_pk = -1
    program = CasePrograms()
    ga = GrievanceAward()

    def setUp(self):
        #Set up a program
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()


        #Set up a Member for testing
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

        #Set up second member for testing
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

        #Set up a case for testing
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

        #Set up a second Case for testing
        self.tempCase2 = Case()
        self.tempCase2.lead = self.tempPerson.id
        self.tempCase2.complainant = self.tempPerson
        self.tempCase2.campus = "Saskatoon"
        self.tempCase2.school = "School of Business"
        self.tempCase2.program = self.program
        self.tempCase2.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase2.status = "OPEN"
        self.tempCase2.date = "2016-10-20"
        self.tempCase2.full_clean()
        self.tempCase2.save()

        #Set up a grievence award to be edited
        self.ga.grievanceType = "M"
        self.ga.recipient = self.tempPerson.id
        self.ga.case = self.tempCase.id
        self.ga.awardAmount = 500.00
        self.ga.description = ""
        self.ga.date = '2016-12-01'
        self.ga.full_clean()
        self.ga.save()

    # Test 1 - Validate that a recipient can be edited to a different valid recipient
    # Input: Recipient is a valid Person
    # Expected result: Record is saved successfully
    def test_that_recipient_is_changed_to_different_member(self):
        self.ga.recipient = self.tempPerson2.id
        self.ga.clean()
        self.ga.save()

        assert self.ga.recipient == self.tempPerson2.id


    # Test 2 - Validate that a recipient cannnot be edited to a different invalid recipient
    # Input: Recipient is an invalid Person
    # Expected result: Validation Error Thrown
    def test_that_recipient_is_changed_to_an_invalid_recipient(self):
        with self.assertRaises(ValidationError):
            self.ga.recipient = 78945648794
            self.ga.full_clean()
            self.ga.save()

            # check validation error message

    # Test 3 - Validate that the case can be changed to a valid case
    # Input: Case is a valid case
    # Expected result: Record is saved successfully
    def test_that_case_can_be_changed_to_a_valid_case(self):
        self.ga.case = self.tempCase2.id
        self.ga.clean()
        self.ga.save()

        assert self.ga.case == self.tempCase2.id

    # Test 4 - Validate that the case cannot be changed to an invalid case
    # Input: Case is an invalid case
    # Expected result: Validation Error Thrown
    def test_that_case_can_not_be_changed_to_an_invalid_case(self):
        with self.assertRaisesMessage(ValidationError, "A valid case ID must be entered!"):
            self.ga.case = 1000
            self.ga.full_clean()
            self.ga.save()

            # check validation error message

    # Test 5 - Validate that the description can be changed with less than 1000 characters
    # Input: Description is less than 1000 characters
    # Expected result: Record is saved successfully
    def test_that_the_description_can_be_changed_if_under_a_size_of_1000_characters(self):
        self.ga.description = 'a' * 999
        self.ga.full_clean();
        self.ga.save();

        assert self.ga.description == 'a' * 999

    # Test 6 - Validate that the description cannot be changed with more than 1000 characters
    # Input: Description is more than 1000 characters
    # Expected result: Validation Error Thrown
    def test_that_description_cannot_be_1000_characters(self):
        with self.assertRaisesMessage(ValidationError, "Description must be 1000 characters or less!"):
            self.ga.description = 'a' * 1001
            self.ga.full_clean();
            self.ga.save();

    # check validation error message


    # Test 7 - Validate that the description can be changed with 0 characters
    # Input: Description is 0 characters
    # Expected result: Record is saved successfully
    def test_that_description_can_be_blank(self):
        self.ga.description = None
        self.ga.full_clean();
        self.ga.save();

        assert self.ga.description is None

    # Test 8 - Validate that the amount can be changed between 0.01 and 999999.99
    # Input: Amount is changed to 9850
    # Expected result: Record is saved successfully
    def test_that_amount_can_be_changed(self):
        self.ga.awardAmount = 9850
        self.ga.full_clean()
        self.ga.save()

        assert self.ga.awardAmount == 9850

    # Test 9 - Validate that the date can be changed to a valid date.
    # Input: Date is changed to 2016-01-01
    # Expected result: Record is saved successfully
    def test_that_date_can_be_changed(self):
        self.ga.date = '2016-01-01'
        self.ga.clean()
        self.ga.save()

        assert self.ga.date == '2016-01-01'

    # Test 9 - Validate that Grievence Type can be changed to valid choice
    # Input: Grievence type is changed to 'P'
    # Expected result: Record is saved successfully
    def test_that_grievance_type_can_be_changed_to_valid_choice(self):
        self.ga.grievanceType = 'P'
        self.ga.full_clean()
        self.ga.save()

        assert self.ga.grievanceType == 'P'

    # Test 10 - Validate that Grievence Type cannot be changed to invalid choice
    # Input: Grievence type is changed to 'L'
    # Expected result: Validation Error Thrown
    def test_that_grievance_type_cannot_be_changed_to_invalid_choice(self):
        with self.assertRaisesMessage(ValidationError, "A grievance type of member or policy must be selected!" ):
            self.ga.grievanceType = 'L'
            self.ga.full_clean()
            self.ga.save()

            # check validation error message