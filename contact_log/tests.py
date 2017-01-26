# SPFA MT CST Project
# November 7, 2016
from django.test import TestCase
from .models import contactLog
# Create your tests here.
class ContactLogTests(TestCase):

    # Test that when a valid date is entered, true is returned
    # Input: 2016-01-01
    # Expected return: true
    def test_validateDateOne(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-01-01'
        self.assertTrue(tempCLog.validateDate(tempCLog.date))

    # Test that when a valid date is entered, true is returned
    # Input: 2016-12-12
    # Expected return: true
    def test_validateDateTwo(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-12-12'
        self.assertTrue(tempCLog.validateDate(tempCLog.date))

    # Test that when an invalid date format is entered, false is returned
    # Input: January 1, 2016
    # Expected return: false
    def test_validateDateThree(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = 'January 1, 2016'
        self.assertFalse(tempCLog.validateDate(tempCLog.date))

    # Test that when an invalid date is entered, false is returned
    # Input: 30-02-2016
    # Expected return: false
    def test_validateDateFour(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = '30-02-2016'
        self.assertFalse(tempCLog.validateDate(tempCLog.date))

    # Test that when an invalid date is entered, false is returned
    # Input: 29-02-2015
    # Expected return: false
    def test_validateDateFive(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = '29-02-2015'
        self.assertFalse(tempCLog.validateDate(tempCLog.date))

    # Test that when a valid date is entered, true is returned
    # Input: 2016-01-30
    # Expected return: true
    def test_validateDateSix(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'Hello World'
        tempCLog.date = '2016-01-30'
        self.assertTrue(tempCLog.validateDate(tempCLog.date))

    # Test that an empty description is accepted
    # Input '' (empty string)
    #Expected result: No error
    def test_validateDescriptionOne(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = ''
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
                self.fail("Description 1 failed!")

    # Test that a 149 char description is accepted
    # Input '' (empty string)
    # Expected result: No error
    def test_validateDescriptionTwo(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
            self.fail("Description 2 failed!")


    # Test that a 150 char description is accepted
    # Input '' (empty string)
    # Expected result: No error
    def test_validateDescriptionThree(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
            self.fail("Description 3 failed!")


    # Test that a 151 char description is rejected
    # Input '' (empty string)
    # Expected result: An error occurs
    def test_validateDescriptionFour(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'A012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.fail("Description 4 failed!")
        except ValueError:
            self.assertTrue(True)

    # Test that an empty member ID is accepted
    # Input: '' (empty member ID)
    # Expected result: All checks pass
    def test_validatememberIDOne(self):
        tempCLog = contactLog()
        tempCLog.memberID = None
        tempCLog.description = ''
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
            self.fail("Member ID 1 failed!")

    # Test that an invalid member ID is rejected
    # Input: 0
    # Expected result: All checks pass
    def test_validatememberIDTwo(self):
        tempCLog = contactLog()
        tempCLog.memberID = '0'
        tempCLog.description = 'A'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.fail("Member ID 2 failed!")
        except ValueError:
            self.assertTrue(True)

    # Test that a valid member ID is accepted
    # Input: 1
    # Expected result: All checks pass
    def test_validatememberIDThree(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1
        tempCLog.description = 'A'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
            self.fail("Member ID 3 failed!")


    # Test that a valid member ID is accepted
    # Input: 999999999
    # Expected result: All checks pass
    def test_validatememberIDFour(self):
        tempCLog = contactLog()
        tempCLog.memberID = 999999999
        tempCLog.description = 'A'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.assertTrue(True)
        except ValueError:
            self.fail("Member ID 4 failed!")


    # Test that an invalid member ID is rejected
    # Input: 1000000000
    # Expected result: All checks pass
    def test_validatememberIDFive(self):
        tempCLog = contactLog()
        tempCLog.memberID = 1000000000
        tempCLog.description = 'A'
        tempCLog.date = '2016-01-01'
        try:
            tempCLog.clean()
            self.fail("Member ID 5 failed!")
        except ValueError:
            self.assertTrue(True)