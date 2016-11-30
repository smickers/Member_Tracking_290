from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import Event
from django.db import DataError
import datetime


# region Description: Test For Event Creation
class EventTest(TestCase):

    """
    Test 1 - Validate event name, empty name
    Input: ""
    Expected result: error thrown explaining event name is required

    """

    def test_event_name_empty_error(self):
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = ""
            testEvent.description = ""
            testEvent.date = "2016-12-25"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

            # Test 2 - Validate event name, valid name
            # Input: "A"
            # Expected result: Event created and added to DB

    def test_event_name_valid(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    # Test 3 - Validate event name, name 20 characters
    # Input: "01234567890126459789"
    # Expected result: Event created and added to DB
    def test_event_name_valid_20_char(self):
        testEvent = Event()
        testEvent.name = "01234567890126459789"
        testEvent.description = ""
        testEvent.date = "2016-12-25"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    # Test 4 - Validate event name, name 21 characters
    # Input: "012345678901234567890"
    # Expected result: Error thrown explaining event name limited to 20 characters
    def test_event_name_21_chars_error(self):
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

    # Test 6 - Validate event description, desc 51 characters
    # Input: "012345678901234567890123456789012345678901234567890"
    # Expected result: Error thrown explaining event description is limited to 50 characters
    def test_event_desc_51_chars_error(self):
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

    # Test 8 - Validate event date, valid date
    # Input: "2016-11-17"
    # Expected result: Event created and added to DB
    def test_event_valid_date(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "Saskatoon"
        testEvent.full_clean()
        testEvent.save()

    # Test 9 - Validate event date, invalid date
    # Input: "2016-11-35"
    # Expected result: Error thrown explaining a valid date must be entered
    def test_event_invalid_date_format(self):
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-35"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

            # Test 10 - Validate event date, invalid date v2
            # Input: 'this is invalid'
            # Expected result: Error thrown explaining a valid date must be entered

    def test_event_invalid_date_text(self):
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "this is invalid"
            testEvent.location = "Saskatoon"
            testEvent.full_clean()
            testEvent.save()

            # Test 11 - Validate valid event location
            # Input "HONALULU"
            # Expected result: Event is created and added to DB

    def test_event_location_valid(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "HONALULU"
        testEvent.full_clean()
        testEvent.save()

    # Test 12 - Validate valid event location v2
    # Input: "REGINA"
    # Expected result: Event is created and added to DB
    def test_event_location_valid2(self):
        testEvent = Event()
        testEvent.name = "A"
        testEvent.description = ""
        testEvent.date = "2016-11-17"
        testEvent.location = "REGINA"
        testEvent.full_clean()
        testEvent.save()

    # Test 13: Validate an invalid event location
    # Input: "this city name is way too long"
    # Expected result: Error thrown explaining event location is too long
    def test_event_location_too_long(self):
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-17"
            testEvent.location = "this city name is way too long"
            testEvent.full_clean()
            testEvent.save()

            # Test 14 - Validate an invalid event location v2
            # Input: ""
            # Expected result: Error thrown explaining event location cannot be left empty.

    def test_event_location_empty(self):
        with self.assertRaises(ValidationError):
            testEvent = Event()
            testEvent.name = "A"
            testEvent.description = ""
            testEvent.date = "2016-11-17"
            testEvent.location = ""
            testEvent.full_clean()
            testEvent.save()

# endregion


# region Description: Test For Adding event to an Event
class EventTest(TestCase):
    def test_here(self):
        self.assertTrue(True)
# endregion