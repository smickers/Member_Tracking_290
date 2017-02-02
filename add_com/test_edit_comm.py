from django.test import TestCase
from django.core.exceptions import ValidationError
from add_com.models import Committee


# Name:     TestEditComm
# Purpose:  This class will test to ensure that the edit functionality is
#           working as intended.
# Author:   Brett LaRose
# Date:     January 31, 2017
class TestEditComm(TestCase):
    testCom = Committee()

    # Setups up a committee to be edited
    def setUp(self):
        self.testCom.name = "Test Committee"
        self.testCom.status = 1
        self.testCom.full_clean()
        self.testCom.save()

    # Testing to see if you can change the name to a valid value
    # Expected result: pass, no errors
    def test_change_valid_name(self):
        self.testCom.name = "Test 2"
        self.testCom.full_clean()
        self.testCom.save()
        self.assertEqual(self.testCom.name, "Test 2")

    # Testing to see if you can change the name to a string with 40 characters
    # Expected result: pass, no errors
    def test_change_40_character_name(self):
        self.testCom.name = 'a' * 40
        self.testCom.full_clean()
        self.testCom.save()
        self.assertEqual(self.testCom.name, "a" * 40)

    # Testing to see if you can change the name to a string with 41 characters
    # Expected result: ValidationError is raised
    def test_change_41_character_name_fail(self):
        with self.assertRaisesMessage(ValidationError, "Committee name must be less than 40 characters."):
            self.testCom.name = 'a' * 41
            self.testCom.full_clean()
            self.testCom.save()

    # Testing to see if you can enter a string of symbols as the name
    # Expected result: ValidationError is raised
    def test_change_symbols_in_committee_name_fail(self):
        with self.assertRaisesMessage(ValidationError, "Committee name must contain letters (A-Z) and numbers(0-9), or spaces/apostrophes."):
            self.testCom.name = "!@#$%^&*()"
            self.testCom.full_clean()
            self.testCom.save()

    # Testing to see if you can enter a blank name
    # Expected result: ValidationError is raised
    def test_blank_name_fail(self):
        with self.assertRaisesMessage(ValidationError, "{'name': [u'This field cannot be blank.']}"):
            self.testCom.name = ""
            self.testCom.full_clean()
            self.testCom.save()

    # Testing to see if you can change the status to inactive
    # Expected result: pass, no errors raised
    def test_change_status_to_inactive(self):
        self.testCom.status = 0
        self.testCom.full_clean()
        self.testCom.save()
        self.assertEqual(self.testCom.status, 0)

    # Testing to see if you can change the status to a string
    # Expected result: ValidationError is raised
    def test_change_status_to_string_fail(self):
        with self.assertRaisesMessage(ValidationError, '{\'status\': [u"\'Active\' value must be an integer."]}'):
            self.testCom.status = "Active"
            self.testCom.full_clean()
            self.testCom.save()

    # Testing to see if you can change the status to an empty string
    # Expected result: ValidationError is raised
    def test_change_status_blank_fail(self):
        with self.assertRaisesMessage(ValidationError, '{\'status\': [u"\'\' value must be an integer."]}'):
            self.testCom.status = ""
            self.testCom.full_clean()
            self.testCom.save()

    # Testing to see if you can change the status to an int other than 0 or 1
    # Expected result: ValidationError is raised
    def test_change_status_int_other_than_0_or_1_fail(self):
        with self.assertRaisesMessage(ValidationError, "{'status': [u'Value 5 is not a valid choice.']}"):
            self.testCom.status = 5
            self.testCom.full_clean()
            self.testCom.save()
