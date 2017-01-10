from django.test import TestCase


class TestCreateCom(TestCase):
    #
    # Test data creation will go here.
    #

    #   METHOD :    setUp
    #   PURPOSE:    create Committee objects for testing.
    def setUp(self):
        """Set up will take place here."""

    def test_normal_com_creation(self):
        """default status
           name: TEST """

    def test_inactive_com_creation(self):
        """status = inactive
           name: TEST2 """

    def test_min_boundary_com_creation(self):
        """default status
           name: A """

    def test_max_boundary_com_creation(self):
        """default status
           name: THIS IS THEE LONGEST TITLE IN MY HEAD"""

    def test_boundary_exception_over_max_com_creation(self):
        """default status
           name: THIS IS A LONGER TITLE THAN THAT OTHER """

    def test_exception_null_com_creation(self):
        """default status
           name: (blank)"""

    def test_exception_whitespace_com_creation(self):
        """default status
           name: "        "     """

    def test_exception_bad_status_com_creation(self):
        """default status, will be changed manually in browser to "asdf"
           name: TEST3 """


