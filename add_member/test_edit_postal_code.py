from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Person

class PostalCodeTestCase(TestCase):
    #Set Up - Used to set up a person to edit
    tempPerson = Person()
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

    # Test 1 - Validate a valid postal code
    # Input: H0H 0H0
    # Expected result: Postal code is saved as H0H 0H0
    def test_valid_postal_code(self):
        self.tempPerson.pCode = 'H0H 0H0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    # Test 2 - Validate a valid lowercase postal code
    # Input: h0h 0h0
    # Expected result: Postal code is saved as H0H 0H0
    def test_lowercase_postal_code(self):
        self.tempPerson.pCode = 'h0h 0h0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    # Test 3 - Validate a valid postal code without spaces
    # Input: H0H 0H0
    # Expected result: Postal code is saved as H0H 0H0
    def test_valid_postal_code_no_space(self):
        self.tempPerson.pCode = 'H0H0H0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    # Test 4 - Validate an invalid postal code
    # Input: H@H 0H0
    # Expected result: Error is thrown
    def test_invalid_postal_code(self):
        #Change to specific error check
        with self.assertRaisesRegexp(ValidationError, "Invalid postal code entered! Postal code must be in the form A#A #A#."):
            self.tempPerson.pCode = 'H@H 0H0'
            self.tempPerson.full_clean()
            self.tempPerson.save()

    # Test 5 - Validate an invalid postal code (too long)
    # Input: H0H 0H0H0
    # Expected result: Error is thrown
    def test_invalid_postal_code_more_than_seven_characters(self):
        #Change to Specific error check
        with self.assertRaisesRegexp(ValidationError, "Postal code entered is too long. Must be in the form A#A #A#."):
            self.tempPerson.pCode = 'H0H 0H0H0'
            self.tempPerson.full_clean()
            self.tempPerson.save()

    # Test 6 - Validate an invalid postal code (too short)
    # Input: H
    # Expected result: Error is thrown
    def test_invalid_postal_code_one_character(self):
        # Change to Specific error check
        with self.assertRaisesRegexp(ValidationError, "Postal code entered is too short. Must be in the form A#A #A#."):
            self.tempPerson.pCode = 'H'
            self.tempPerson.full_clean()
            self.tempPerson.save()
