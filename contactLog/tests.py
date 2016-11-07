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