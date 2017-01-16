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

    def test_valid_postal_code(self):
        self.tempPerson.pCode = 'H0H 0H0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    def test_lowercase_postal_code(self):
        self.tempPerson.pCode = 'h0h 0h0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    def test_valid_postal_code_no_space(self):
        self.tempPerson.pCode = 'H0H0H0'
        self.tempPerson.full_clean()
        self.tempPerson.save()
        self.assertTrue(self.tempPerson.pCode == 'H0H 0H0')

    def test_invalid_postal_code(self):
        #Change to specific error check
        with self.assertRaises(ValidationError):
            self.tempPerson.pCode = 'H@H 0H0'
            self.tempPerson.full_clean()
            self.tempPerson.save()

    def test_invalid_postal_code_more_than_seven_characters(self):
        #Change to Specific error check
        with self.assertRaises(ValidationError):
            self.tempPerson.pCode = 'H0H 0H0H0'
            self.tempPerson.full_clean()
            self.tempPerson.save()

    def test_invalid_postal_code_one_character(self):
        # Change to Specific error check
        with self.assertRaises(ValidationError):
            self.tempPerson.pCode = 'H'
            self.tempPerson.full_clean()
            self.tempPerson.save()
