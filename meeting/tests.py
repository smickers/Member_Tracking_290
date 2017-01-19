from django.test import TestCase, Client
from meeting.models import *
from add_com.models import Committee
from add_member import Person
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# Create your tests here.

class MeetingTests(TestCase):
    committee = Committee()
    person1 = Person()

    '''
    Setup a test committee to use in the meeting
    Setup a test person for use in additional members field
    '''
    def setUp(self):
        self.committee.name = "Finance"
        self.committee.status = "ACTIVE"
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
        testMeeting.members.add(self.person1)
        testMeeting.save()

    '''
        Name:           test_invalid_committee_is_not_saved_to_db
        Function:       Makes sure the meeting is not saved to DB when committee is an invalid option
        '''
    def test_invalid_committee_is_not_saved_to_db(self):
        testMeeting = Meeting()
        testMeeting.committee = None
        testMeeting.liaison = 1234
        testMeeting.date = "2016-10-20"
        testMeeting.description = 'a' * 500
        testMeeting.full_clean()
        testMeeting.save()
        testMeeting.members.add(self.person1)
        testMeeting.save()


