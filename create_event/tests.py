from django.test import TestCase
import unittest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from create_event.models import Event
from django.db import DataError
import datetime
from add_member.models import Person


class EventTest(unittest.TestCase):
    testEvent = None
    tempPerson = None
    tempPerson2 = None
    not_saved_person = None

    def setUp(self):
        self.testEvent = Event()
        self.testEvent.name = "Sample Name"
        self.testEvent.description = ""
        self.testEvent.date = "2016-12-25"
        self.testEvent.location = "Saskatoon"
        self.testEvent.full_clean()
        self.testEvent.save()

        self.tempPerson = Person()
        self.tempPerson.memberID = 123456789
        self.tempPerson.firstName = 'First'
        self.tempPerson.middleName = 'Middle'
        self.tempPerson.lastName = 'Last'
        self.tempPerson.socNum = 123456789
        self.tempPerson.city = 'Sample City'
        self.tempPerson.mailAddress = 'Sample address'
        self.tempPerson.mailAddress2 = 'Sample Address 2'
        self.tempPerson.pCode = 's7k5j8'
        self.tempPerson.hPhone = '(306)812-1234'
        self.tempPerson.cPhone = '(306)812-1234'
        self.tempPerson.hEmail = 'sample@sample.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Commitee'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '2012-03-03'
        self.tempPerson.hireDate = '2012-03-03'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.membershipStatus = 'RESOURCE'
        self.tempPerson.programChoice = 'Sample Program'
        self.tempPerson.full_clean()
        self.tempPerson.save()

        self.tempPerson2 = Person()
        self.tempPerson2.memberID = 123456789
        self.tempPerson2.firstName = 'First'
        self.tempPerson2.middleName = 'Middle'
        self.tempPerson2.lastName = 'Last'
        self.tempPerson2.socNum = 123456789
        self.tempPerson2.city = 'Sample City'
        self.tempPerson2.mailAddress = 'Sample address'
        self.tempPerson2.mailAddress2 = 'Sample Address 2'
        self.tempPerson2.pCode = 's7k5j8'
        self.tempPerson2.hPhone = '(306)812-1234'
        self.tempPerson2.cPhone = '(306)812-1234'
        self.tempPerson2.hEmail = 'sample@sample.com'
        self.tempPerson2.campus = 'SASKATOON'
        self.tempPerson2.jobType = 'FTO'
        self.tempPerson2.committee = 'Sample Commitee'
        self.tempPerson2.memberImage = 'image.img'
        self.tempPerson2.bDay = '2012-03-03'
        self.tempPerson2.hireDate = '2012-03-03'
        self.tempPerson2.gender = 'MALE'
        self.tempPerson2.membershipStatus = 'RESOURCE'
        self.tempPerson2.programChoice = 'Sample Program'
        self.tempPerson2.full_clean()
        self.tempPerson2.save()

        self.not_saved_person = Person()
        self.not_saved_person.memberID = 123456789
        self.not_saved_person.firstName = 'First'
        self.not_saved_person.middleName = 'Middle'
        self.not_saved_person.lastName = 'Last'
        self.not_saved_person.socNum = 123456789
        self.not_saved_person.city = 'Sample City'
        self.not_saved_person.mailAddress = 'Sample address'
        self.not_saved_person.mailAddress2 = 'Sample Address 2'
        self.not_saved_person.pCode = 's7k5j8'
        self.not_saved_person.hPhone = '(306)812-1234'
        self.not_saved_person.cPhone = '(306)812-1234'
        self.not_saved_person.hEmail = 'sample@sample.com'
        self.not_saved_person.campus = 'SASKATOON'
        self.not_saved_person.jobType = 'FTO'
        self.not_saved_person.committee = 'Sample Commitee'
        self.not_saved_person.memberImage = 'image.img'
        self.not_saved_person.bDay = '2012-03-03'
        self.not_saved_person.hireDate = '2012-03-03'
        self.not_saved_person.gender = 'MALE'
        self.not_saved_person.membershipStatus = 'RESOURCE'
        self.not_saved_person.programChoice = 'Sample Program'
        self.not_saved_person.full_clean()

    # region Tests For Event Creation
    def test_event_name_empty_error(self):
        """
        Test 1 - Validate event name, empty name
        Input: ""
        Expected result: error thrown explaining event name is required
        """
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = ""
            testEvent.description = ""
            testEvent.date = "2016-12-25"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

    def test_event_name_valid(self):
        """
         Test 2 - Validate event name, valid name
         Input: "A"
         Expected result: Event created and added to DB
        """
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    def test_event_name_valid_20_char(self):
        # Test 3 - Validate event name, name 20 characters
        # Input: "01234567890126459789"
        # Expected result: Event created and added to DB
        testEvent = Event()
        testEvent.name = "01234567890126459789"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    def test_event_name_21_chars_error(self):
        # Test 4 - Validate event name, name 21 characters
        # Input: "012345678901234567890"
        # Expected result: Error thrown explaining event name limited to 20 characters
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "012345678901264597890"
            testEvent.description = ""
            testEvent.date = "2016-12-25"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

            # Test 5 - Validate event description, desc 50 characters
            # Input: "01234567890123456789012345678901234567890123456789"
            # Expected result: Event created and added to DB

    def test_event_desc_50_chars(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = "01234567890123456789012345678901234567890123456789"
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    def test_event_desc_51_chars_error(self):
        # Test 6 - Validate event description, desc 51 characters
        # Input: "012345678901234567890123456789012345678901234567890"
        # Expected result: Error thrown explaining event description is limited to 50 characters
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = "012345678901234567890123456789012345678901234567890"
            testEvent.date = "2016-12-25"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

            # Test 7 - Validate event description, empty desc
            # Input: ""
            # Expected result: Event created and added to DB

    def test_event_desc_confirm_empty_desc(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    def test_event_valid_date(self):
        # Test 8 - Validate event date, valid date
        # Input: "2016-11-17"
        # Expected result: Event created and added to DB
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    def test_event_invalid_date_format(self):
        # Test 9 - Validate event date, invalid date
        # Input: "2016-11-35"
        # Expected result: Error thrown explaining a valid date must be entered
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-35"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

    def test_event_invalid_date_text(self):
        # Test 10 - Validate event date, invalid date v2
        # Input: 'this is invalid'
        # Expected result: Error thrown explaining a valid date must be entered
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "this is invalid"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

    def test_event_location_valid(self):
        # Test 11 - Validate valid event location
        # Input "HONALULU"
        # Expected result: Event is created and added to DB
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "HONALULU"
        testEvent.full_clean()
        testEvent.save()

    def test_event_location_valid2(self):
        # Test 12 - Validate valid event location v2
        # Input: "REGINA"
        # Expected result: Event is created and added to DB
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "REGINA"
        testEvent.full_clean()
        testEvent.save()

    def test_event_location_too_long(self):
        # Test 13: Validate an invalid event location
        # Input: "this city name is way too long"
        # Expected result: Error thrown explaining event location is too long
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-17"
            testEvent.location = "this city name is way too long"
            testEvent.full_clean()
            testEvent.save()

    def test_event_location_empty(self):
        # Test 14 - Validate an invalid event location v2
        # Input: ""
        # Expected result: Error thrown explaining event location cannot be left empty.
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-17"
            testEvent.location = ""
            testEvent.full_clean()
            testEvent.save()

    # endregion

    def test_if_user_can_add_member_to_an_event(self):
        """
        :parameter self
        """
        self.testEvent.members.add(self.tempPerson)
        self.assertEqual(self.members.count == 1)

    def test_if_user_can_add_multiple_member_to_an_event(self):
        """
        :parameter self
        """
        self.testEvent.members.add(self.tempPerson)
        self.testEvent.members.add(self.tempPerson2)
        self.assertEqual(self.members.count == 2)

    def test_if_user_cannot_add_a_member_that_already_exist_on_an_event(self):
        """
        :parameter self
        """
        self.testEvent.members.add(self.tempPerson)
        self.testEvent.members.add(self.tempPerson)
        self.assertEqual(self.members.count == 1)

    def test_if_user_cannnot_add_member_that_doesnt_exist_in_db(self):
        """
        :parameter self
        """
        with self.assertRaises(Person.DoesNotExist):
            self.testEvent.members.add(self.not_saved_person)

    def test_if_usr_cannot_add_a_member_to_an_event_that_doesnt_exist(self):
        """
        :parameter self
        :return:
        """
        with self.assertRaises(Event.DoesNotExist):
            target_event = Event.objects.get(name='Sample Event')
            target_event.members.add(self.tempPerson)
