from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import Case
from django.db import DataError
import datetime
from add_member.models import Person

class CaseTests(TestCase):
    person1 = Person()

    def setUp(self):
        # TODO: Check this page out:
        # https://www.google.ca/webhp?sourceid=chrome-instant&rlz=1C1CHBF_enCA707CA707&ion=1&espv=2&ie=UTF-8#q=manage.py%20call%20django%20unit%20test
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