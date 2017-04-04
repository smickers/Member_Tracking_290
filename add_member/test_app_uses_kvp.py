from django.test import TestCase
from spfa_mt import kvp
from .models import Person

class KVPTestCase(TestCase):
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

    def test_that_kvp_contains_proper_gender_choices(self):
        for x in range(0, len(kvp.GENDER_CHOICE)):
            self.person1.gender = kvp.GENDER_CHOICE[x]
            self.assertEquals(self.person1.gender, kvp.GENDER_CHOICE[x])
        self.person1.gender = "Not a Gender"

    def test_that_kvp_contains_proper_campus_choice(self):
        for x in range(0, len(self.CAMPUS_CHOICE)):
            self.assertEquals(kvp.CAMPUS_CHOICE[x], self.CAMPUS_CHOICE[x])

    def test_that_kvp_contains_proper_position_class_choice(self):
        for x in range(0, len(self.POSITION_CLASS_CHOICE)):
            self.assertEquals(kvp.POSITION_CLASS_CHOICE[x], self.POSITION_CLASS_CHOICE[x])

    def test_that_kvp_contains_proper_membership_status(self):
        for x in range(0, len(self.MEMBERSHIP_STATUS)):
            self.assertEquals(kvp.MEMBERSHIP_STATUS[x], self.MEMBERSHIP_STATUS[x])

    def test_that_kvp_contains_proper_employee_status(self):
        for x in range(0, len(self.EMPLOYEE_STATUS)):
            self.assertEquals(kvp.EMPLOYEE_STATUS[x], self.EMPLOYEE_STATUS[x])

