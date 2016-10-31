from django.test import TestCase
from .models import contactLog
# Create your tests here.
class ContactLogTests(TestCase):
    #def setUp(self):
        #x = 5 + 2

    #def test_fakeTest(self):
    #    self.assertTrue(True)

    def test_validateDateOne(self):
        date = '2016/01/01'
        self.assertTrue(contactLog.validateDate(date))

    def test_validateDateTwo(self):
        date = '2016/12/12'
        self.assertTrue(contactLog.validateDate(date))

    def test_validateDateThree(self):
        date = 'January 1, 2016'
        self.assertFalse(contactLog.validateDate(date))

    def test_validateDateFour(self):
        date = '30/02/2016'
        self.assertFalse(contactLog.validateDate(date))

    def test_validateDateFive(self):
        date = '29/02/2015'
        self.assertFalse(contactLog.validateDate(date))

    def test_validateDateSix(self):
        date = '2016/01/30'
        self.assertTrue(contactLog.validateDate(date))