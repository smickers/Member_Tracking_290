from django.test import TestCase
from django.core.exceptions import ValidationError
from add_com.models import Committee


class TestCreateCom(TestCase):

    #   METHOD :    setUp
    #   PURPOSE:    create Committee objects for testing.
    def setUp(self):
        """Set up will take place here."""

    # Test normal Committee creation.
    def test_normal_com_creation(self):
        """default status
           name: TEST """
        c = Committee()
        c.name = 'TEST'
        c.status = 1
        c.full_clean()
        c.save()

    # Test normal Committee creation with status = inactive.
    def test_inactive_com_creation(self):
        """status = inactive
           name: TEST2 """
        c = Committee()
        c.name = 'TEST2'
        c.status = 0
        c.full_clean()
        c.save()

    # Test minimum (name) boundary Committee creation
    # Expected result: PASS
    def test_min_boundary_com_creation(self):
        """default status
           name: A """
        c = Committee()
        c.name = 'A'
        c.status = 1
        c.full_clean()
        c.save()

    # Test maximum (name) boundary Committee creation
    def test_max_boundary_com_creation(self):
        """default status
           name: THIS IS THEE LONGEST TITLE IN MY HEAD"""
        c = Committee()
        c.name = 'THIS IS THEE LONGEST TITLE IN MY HEAD'
        c.status = 1
        c.save()

    # Test boundary exception Committee creation
    def test_boundary_exception_over_max_com_creation(self):
        """default status
           name: THIS IS A LONGER TITLE THAN THAT OTHER """
        #with self.assertRaises(ValidationError):
        c = Committee()
        c.name = 'THIS IS A LONGER TITLE THAN THAT OTHER'
        c.status = 1
        c.full_clean()
        c.save()

    # Test null exception Committee creation
    def test_exception_null_com_creation(self):
        """default status
           name: (blank)"""
        #with self.assertRaises(ValidationError):
        c = Committee()
        c.name = ''
        c.status = 1
        c.full_clean()
        c.save()

    # Test whitespace exception Committee creation
    def test_exception_whitespace_com_creation(self):
        """default status
           name: "        "     """
        #with self.assertRaises(ValidationError):
        c = Committee()
        c.name = '            '
        c.status = 1
        c.full_clean()
        c.save()

    # Test invalid status exception Committee creation
    def test_exception_bad_status_com_creation(self):
        """default status, will be changed manually in browser to "asdf"
           name: TEST3 """
        #with self.assertRaises(ValidationError):
        c = Committee()
        c.name = 'TEST3'
        c.status = 'asdf'
        c.full_clean()
        c.save()

    # Test special characters exception Committee creation
    def test_exception_special_characters_com_creation(self):
        """default status, name: !@#%/;"""
        #with self.assertRaises(ValidationError):
        c = Committee()
        c.name = '!@#%/;'
        c.status = 1
        c.full_clean()
        c.save()



