# SPFA MT CST Project
# November 7, 2016
from django.test import TestCase
from add_member.models import Person
from .models import contactLog
from django.core.exceptions import ValidationError
from django.db import DataError

# Create your tests here.
class ContactLogTests(TestCase):
    person1 = Person()

    def setUp(self):
        self.person1.memberID = 4204444
        self.person1.firstName = 'First'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Last'
        self.person1.socNum = 123456789
        self.person1.city = 'Sample City'
        self.person1.mailAddress = 'Sample address'
        self.person1.mailAddress2 = 'Sample Address 2'
        self.person1.pCode = 's7k5j8'
        self.person1.hPhone = '(306)812-1234'
        self.person1.cPhone = '(306)812-1234'
        self.person1.hEmail = 'sample@sample.com'
        self.person1.campus = 'SASKATOON'
        self.person1.jobType = 'FTO'
        self.person1.committee = 'Sample Commitee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

    # Test that when a valid date is entered, true is returned
    # Input: 2016-01-01
    # Expected return: true
    def test_validateDateOne(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)

    # Test that when a valid date is entered, true is returned
    # Input: 2016-12-12
    # Expected return: true
    def test_validateDateTwo(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-12-12'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)

    # Test that when an invalid date format is entered, false is returned
    # Input: January 1, 2016
    # Expected return: false
    def test_validateDateThree(self):
        with self.assertRaises(ValidationError):
            tempCLog = contactLog()
            tempCLog.member = self.person1
            tempCLog.description = 'Hello World'
            tempCLog.date = 'January 1, 2016'
            tempCLog.clean()
            tempCLog.save()

    # Test that when an invalid date is entered, false is returned
    # Input: 30-02-2016
    # Expected return: false
    def test_validateDateFour(self):
        with self.assertRaises(ValidationError):
            tempCLog = contactLog()
            tempCLog.member = self.person1
            tempCLog.description = 'Hello World'
            tempCLog.date = '30-02-2016'
            tempCLog.clean()
            tempCLog.save()
            self.assertTrue(False)

    # Test that when an invalid date is entered, false is returned
    # Input: 29-02-2015
    # Expected return: false
    def test_validateDateFive(self):
        with self.assertRaises(ValidationError):
            tempCLog = contactLog()
            tempCLog.member = self.person1
            tempCLog.description = 'Hello World'
            tempCLog.date = '29-02-2015'
            tempCLog.clean()
            tempCLog.save()
            self.assertTrue(False)

    # Test that when a valid date is entered, true is returned
    # Input: 2016-01-30
    # Expected return: true
    def test_validateDateSix(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-01-30'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)

    # Test that an empty description is accepted
    # Input '' (empty string)
    #Expected result: No error
    def test_validateDescriptionOne(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = ''
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)

    # Test that a 149 char description is accepted
    # Input '' (empty string)
    # Expected result: No error
    def test_validateDescriptionTwo(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678'
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        self.assertTrue(True)


    # Test that a 150 char description is accepted
    # Input '' (empty string)
    # Expected result: No error
    def test_validateDescriptionThree(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        self.assertTrue(True)


    # Test that a 151 char description is rejected
    # Input '' (empty string)
    # Expected result: An error occurs
    def test_validateDescriptionFour(self):
        with self.assertRaises(DataError):
            tempCLog = contactLog()
            tempCLog.member = self.person1
            tempCLog.description = 'A012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
            tempCLog.date = '2016-01-01'
            tempCLog.clean()
            tempCLog.save()

    # Test that an empty member ID is accepted
    # Input: '' (empty member ID)
    # Expected result: All checks pass
    def test_validatememberIDOne(self):
        tempCLog = contactLog()
        tempCLog.member = None
        tempCLog.description = ''
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)

    # Test that an invalid member ID is rejected
    # Input: 0
    # Expected result: All checks pass
    def test_validatememberIDTwo(self):
        with self.assertRaisesMessage(Person.DoesNotExist, "Person matching query does not exist."):
            tempCLog = contactLog()
            tempCLog.member = Person.objects.get(firstName='A ridiculous first name!')
            tempCLog.description = 'A'
            tempCLog.date = '2016-01-01'
            tempCLog.clean()
            tempCLog.save()

    # Test that a valid member ID is accepted
    # Input: 1
    # Expected result: All checks pass
    def test_validatememberIDThree(self):
        tempCLog = contactLog()
        tempCLog.member = self.person1
        tempCLog.description = 'A'
        tempCLog.date = '2016-01-01'
        tempCLog.clean()
        tempCLog.save()
        self.assertTrue(True)


    # Test that a valid member ID is accepted
    # Input: 999999999
    # Expected result: All checks pass
    def test_validatememberIDFour(self):
        with self.assertRaisesMessage(Person.DoesNotExist, "Person matching query does not exist."):
            tempCLog = contactLog()
            tempCLog.member = Person.objects.get(firstName='A ridiculous first name!')
            tempCLog.description = 'A'
            tempCLog.date = '2016-01-01'
            tempCLog.clean()
            tempCLog.save()

    # Test that an invalid member ID is rejected
    # Input: 1000000000
    # Expected result: All checks pass
    def test_validatememberIDFive(self):
        with self.assertRaisesMessage(Person.DoesNotExist, "Person matching query does not exist."):
            tempCLog = contactLog()
            tempCLog.member = Person.objects.get(firstName='A ridiculous first name!')
            tempCLog.description = 'A'
            tempCLog.date = '2016-01-01'
            tempCLog.clean()
