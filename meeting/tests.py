from django.test import TestCase, Client
from meeting.models import *
from add_com.models import Committee
from add_member.models import Person
from django.core.exceptions import *

"""
Author Jaryd Buck, David Letkeman
Class: meetingTests
Purpose: Test Cases for creating a meeting
Date: Jan 26, 2017
"""
class MeetingTests(TestCase):
    committee = Committee()
    person1 = Person()

    '''
    Setup a test committee to use in the meeting
    Setup a test person for use in additional members field
    '''
    def setUp(self):
        self.committee.name = "Finance"
        self.committee.status = 1
        self.committee.full_clean()
        self.committee.save()

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
        self.person1.committee = 'Sample Committee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

    '''
    Name:           test_valid_committee_is_saved_to_db
    Function:       Verifies the committee is saved to DB when an option from the list is chosen.
    '''
    def test_valid_committee_is_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    '''
    Name:           test_invalid_committee_is_not_saved_to_db
    Function:       Verifies that the meeting is not saved to DB when committee is an invalid option
    '''
    def test_invalid_committee_is_not_saved_to_db(self):
        with self.assertRaises(ValidationError):
            testMeeting = Meeting()
            testMeeting.committee = None
            testMeeting.liaison = 1234
            testMeeting.date = "2016-10-20"
            testMeeting.description = 'a' * 500
            testMeeting.full_clean()
            testMeeting.save()
            testMeeting.members_attending.add(self.person1)
            testMeeting.save()

    '''
    Name:           test_valid_liaison_is_saved_to_db
    Function:       Verifies that the liaison is a valid number ( not exceeding 10 digits)
    '''
    def test_valid_liaison_is_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    '''
    Name:           test_invalid_liaison_is_not_saved_to_db
    Function:       Verifies that a invalid liaison (exceeding 10 digits) is not saved to the database
    '''
    def test_invalid_liaison_is_not_saved_to_db(self):
        with self.assertRaisesMessage(ValidationError, "Ensure this value has at most 10 characters (it has 11)."):
            testMeeting = Meeting()
            testMeeting.committee = self.committee
            testMeeting.liaison = 12345678900
            testMeeting.date = "2016-10-20"
            testMeeting.description = 'a' * 500
            testMeeting.full_clean()
            testMeeting.save()
            testMeeting.members_attending.add(self.person1)
            testMeeting.save()

    '''
    Name:           test_valid_meeting_date_is_saved_saved_to_db
    Function:       Verifies that a valid date is saved to the database
    '''
    def test_valid_meeting_date_is_saved_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    '''
    Name:           test_invalid_meeting_date_is_not_saved_saved_to_db
    Function:       Verifies that a invalid date (ex. feb.31) is not saved to the database
    '''
    def test_invalid_meeting_date_is_not_saved_saved_to_db(self):
        with self.assertRaisesMessage(ValidationError, "\'2016-02-31\' value has the correct format (YYYY-MM-DD) but it is an invalid date."):
            testMeeting = Meeting()
            testMeeting.committee = self.committee
            testMeeting.liaison = 1234
            testMeeting.date = "2016-02-31"
            testMeeting.description = 'a' * 500
            testMeeting.full_clean()
            testMeeting.save()
            testMeeting.members_attending.add(self.person1)
            testMeeting.save()

    '''
    Name:           test_valid_description_is_saved_to_db
    Function:       Verifies that a valid description is saved to db (not exceeding 1000 characters)
    '''
    def test_valid_description_is_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    '''
    Name:           test_invalid_description_is_not_saved_to_db
    Function:       Verifies that a in valid description is not saved to db (exceeding 1000 characters)
    '''
    def test_invalid_description_is_not_saved_to_db(self):
        with self.assertRaisesMessage(ValidationError, "Ensure this value has at most 1000 characters (it has 1001)."):
            testMeeting = Meeting()
            testMeeting.committee = self.committee
            testMeeting.liaison = 1234
            testMeeting.date = "2016-10-20"
            testMeeting.description = 'a' * 1001
            testMeeting.full_clean()
            testMeeting.save()
            testMeeting.members_attending.add(self.person1)
            testMeeting.save()

    '''
    Name:           test_valid_member_is_added_to_meeting_and_saved_to_db
    Function:       Verifies that a valid person is added to the meeting
    '''
    def test_valid_member_is_added_to_meeting_and_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = self.committee
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members_attending.add(self.person1)
        testMeeting.save()

    '''
    Name:           test_invalid_member_is_not_added_to_meeting_and_not_saved_to_db
    Function:       Verifies that a invalid person is not added to the meeting and not saved to DB
    '''
    def test_invalid_member_is_not_added_to_meeting_and_not_saved_to_db(self):
        with self.assertRaisesMessage(Person.DoesNotExist, "Person matching query does not exist."):
            testMeeting = Meeting()
            testMeeting.committee = self.committee
            testMeeting.liaison = 1234
            testMeeting.date = "2016-10-20"
            testMeeting.description = 'a' * 500
            testMeeting.full_clean()
            testMeeting.save()
            testMeeting.members_attending = Person.objects.get(firstName='Nonexistent member')
            testMeeting.save()
