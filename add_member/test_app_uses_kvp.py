from django.test import TestCase
from spfa_mt import kvp

class KVPTestCase(TestCase):
    print("hello")
    # bound fields choices for gender field
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNDEFINED', 'Undefined'),
    ]

    # bound fields choices for campus field
    CAMPUS_CHOICE = [
        ('SASKATOON', 'SASKATOON'),
        ('REGINA', 'REGINA'),
        ('MOOSEJAW', 'MOOSE JAW'),
        ('PA', 'PRINCE ALBERT'),
    ]

    # bound fields choices for position field
    POSITION_CLASS_CHOICE = [
        ('FTO', 'Full-time ongoing'),
        ('FTED', 'Full-time end dated'),
        ('PTO', 'Part-time ongoing'),
        ('PTED', 'Part-time end dated'),
    ]

    # bound fields choices for membership status field
    MEMBERSHIP_STATUS = [
        ('RESOURCE', 'RESOURCE'),
        ('COMCHAIR', 'COMMITTEE CHAIR'),
        ('RECORDER', 'RECORDER'),
    ]

    EMPLOYEE_STATUS = [
        ('A', 'ACTIVE'),
        ('T', 'TERMINATED')
    ]

    def test_that_kvp_contains_proper_gender_choices(self):
        for x in range(0, len(self.GENDER_CHOICE)):
            self.assertEquals(kvp.GENDER_CHOICE[x], self.GENDER_CHOICE[x])

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

