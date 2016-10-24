from django.test import TestCase
from .models import contactLog
# Create your tests here.
class ContactLogTests(TestCase):
    #def setUp(self):
        #x = 5 + 2

    def test_validateDateOne(self):
        date = '01/01/2016'
        self.AssertTrue(validateDate(date))

    def test_validateDateTwo(self):
        date = '12/12/2016'
        self.AssertTrue(validateDate(date))


    def test_validateDateThree(self):
        date = 'January 1, 2016'
        self.AssertTrue(validateDate(date))

    def test_validateDateFour(self):
        date = '30/02/2016'
        self.AssertFalse(validateDate(date))

    def test_validateDateFive(self):
        date = '29/02/2015'
        self.AssertFalse(validateDate(date))

    def test_validateDateFive(self):
        date = '01/30/2016'
        self.AssertFalse(validateDate(date))