# SPFA MT CST Project
# January 26, 2017
# Cameron Auser
from django.test import TestCase
from .models import contactLog
from add_member.models import Person
from django.core.exceptions import ValidationError


class ContactLogEditTests(TestCase):

    cLog = contactLog()
    person1 = Person()
    person2 = Person()
    person3 = Person()
    # Unit test setup method
    def setUp(self):
        # Set up our people
        self.person1.memberID = 4204444
        self.person1.firstName = 'Deborah'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Williams'
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

        self.person2.memberID = 5205555
        self.person2.firstName = 'Alpha'
        self.person2.middleName = 'Middle'
        self.person2.lastName = 'Kincaid'
        self.person2.socNum = 123456789
        self.person2.city = 'Sample City'
        self.person2.mailAddress = 'Sample address'
        self.person2.mailAddress2 = 'Sample Address 2'
        self.person2.pCode = 's7k5j8'
        self.person2.hPhone = '(306)812-1234'
        self.person2.cPhone = '(306)812-1234'
        self.person2.hEmail = 'sample@sample.com'
        self.person2.campus = 'SASKATOON'
        self.person2.jobType = 'FTO'
        self.person2.committee = 'Sample Commitee'
        self.person2.memberImage = 'image.img'
        self.person2.bDay = '2012-03-03'
        self.person2.hireDate = '2012-03-03'
        self.person2.gender = 'MALE'
        self.person2.membershipStatus = 'RESOURCE'
        self.person2.programChoice = 'Sample Program'
        self.person2.full_clean()
        self.person2.save()

        self.person3.memberID = 6206666
        self.person3.firstName = 'Tim'
        self.person3.middleName = 'Middle'
        self.person3.lastName = 'Jones'
        self.person3.socNum = 123456789
        self.person3.city = 'Sample City'
        self.person3.mailAddress = 'Sample address'
        self.person3.mailAddress2 = 'Sample Address 2'
        self.person3.pCode = 's7k5j8'
        self.person3.hPhone = '(306)812-1234'
        self.person3.cPhone = '(306)812-1234'
        self.person3.hEmail = 'sample@sample.com'
        self.person3.campus = 'SASKATOON'
        self.person3.jobType = 'FTO'
        self.person3.committee = 'Sample Commitee'
        self.person3.memberImage = 'image.img'
        self.person3.bDay = '2012-03-03'
        self.person3.hireDate = '2012-03-03'
        self.person3.gender = 'MALE'
        self.person3.membershipStatus = 'RESOURCE'
        self.person3.programChoice = 'Sample Program'
        self.person3.full_clean()
        self.person3.save()

        # Set up the contact log to be edited
        self.cLog.relatedMember = self.person1
        self.cLog.date = 'Feb 12 2017'
        self.cLog.description = 'Hello world!'
        self.cLog.full_clean()
        self.cLog.save()

    # Test that a valid member can be associated with a contact log
    # Input: Set person2 to be cLog's related member
    def test_validate_related_member_valid(self):
        self.cLog.relatedMember = self.person2
        self.cLog.full_clean()
        self.cLog.save()
        self.assertTrue(True)

    # Test that an invalid member cannot be associated with a contact log
    # Input: Set person4 to be cLog's related member
    def test_validate_related_member_invalid(self):
        with(self.assertRaisesRegexp(ValidationError, "A valid member must be associated with a contact log!")):
            self.cLog.relatedMember = self.person4
            self.cLog.full_clean()
            self.cLog.save()

    # Test that a contact log cannot be saved without a related member
    # Input: Set cLog's related member to be nobody!
    def test_validate_no_related_member(self):
        with(self.assertRaisesRegexp(ValidationError, "A valid member must be associated with a contact log!")):
            self.cLog.relatedMember = None
            self.cLog.full_clean()
            self.cLog.save()

    # Test that a contact log's date can be changed
    # Input: Set cLog's contact date to be Feb 15 2017
    def test_validate_contact_date_valid(self):
        self.cLog.date = '15 Feb 2017'
        self.cLog.full_clean()
        self.cLog.save()
        self.assertTrue(True)


    # Test that a contact log cannot be saved with an invalid date
    # Input: Set cLog's contact date to Feb 31 2017
    def test_validate_contact_date_invalid(self):
        with(self.assertRaisesRegexp(ValidationError, "A valid date must be entered!")):
            self.cLog.date = '31 Feb 2017'
            self.cLog.full_clean()
            self.cLog.save()

    # Test that a contact log's description can be updated
    # Input: Set cLog's description to be 10 a's
    def test_validate_contact_log_description_valid(self):
        self.cLog.description = 'a' * 10
        self.cLog.full_clean()
        self.cLog.save()
        self.assertTrue(True)

    # Test that a contact log cannot be saved with a description > 150 chars
    # Input: Set cLog's description to 160 a's
    def test_validate_contact_log_description_invalid(self):
        with(self.assertRaisesRegexp(ValidationError, "The description must be 150 characters or less!")):
            self.cLog.description = 'a' * 160
            self.cLog.full_clean()
            self.cLog.save()