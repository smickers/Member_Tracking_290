from unittest import TestCase
from contact_log import contact_log


class TestContactLog(TestCase):
    def test_createContactLog(self):
        #Unit Test Information

        #Test: Test that a contact log is saved to the DB
        #       if all entered information is valid

        #Input:
        #   Date: 10/05/2015
        #   Description: "Hello"
        #   Member ID: NULL

        #Expected Result: Contact Log is saved to the DB

        # Input:
        #   Date: 10/35/2015
        #   Description: "Hello"
        #   Member ID: NULL

        # Expected Result: Contact Log is NOT saved, error is displayed

        # Input:
        #   Date: 10/05/2015
        #   Description: ""
        #   Member ID: NULL

        # Expected Result: Contact Log is saved to the DB

        # Input:
        #   Date: 10/05/2015
        #   Description: "Hello"
        #   Member ID: 1

        #Assumption: A member with ID 1 is present in the Member table
        # Expected Result: Contact Log is saved to the DB

        # Input:
        #   Date: 10/05/2015
        #   Description: "Hello"
        #   Member ID: 50

        # Assumption: A member with ID 50 is NOT present in the Member table
        # Expected Result: Contact Log is NOT saved to the DB, error is displayed
        self.fail()

    def test_validateDate(self):
        self.fail()

    def test_validateDescription(self):
        #Test: test that description is 150 characters or less


        '''
        Input:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque commodo viverra lacinia. Proin id sollicitudin
        urna. Cras a massa eleifend, interdum mi nec, tempus enim. Donec eget ligula nec leo fermentum imperdiet vel
        et turpis. Donec dapibus nec enim ut rhoncus. Donec dictum est eleifend sollicitudin maximus. Morbi viverra
        volutpat ullamcorper. Nulla interdum ornare elementum. Nullam orci leo, faucibus at semper id, malesuada ac mi.
        Quisque facilisis sem arcu, in ultricies erat lobortis vitae. Vestibulum pellentesque tempus ex, ac fringilla
        erat euismod sit amet. Etiam vel nisi euismod, malesuada nisi id, vulputate nisi. Quisque nec interdum tortor.

        Suspendisse varius nisl metus, in rutrum tellus pharetra et. In nulla ligula, maximus quis sodales ac, semper
        nec neque. Etiam porttitor tortor in luctus rutrum. In elementum magna sed augue consectetur iaculis. Donec
        ornare, diam in accumsan eleifend, tortor odio suscipit dui, nec auctor orci lacus ut urna. Cras ac purus nec dui.

        Expected Result: true
        '''

        self.fail()

    def test_validateMemberID(self):
        # Unit Test Information
        # Test: Test that a memberID is exactly nine digits
        # Input: 123456789
        # Expected return: true

        #Input: 000000000
        #Expected return: true

        #Input: 999999999
        #Expected return: true

        #Input: 0
        #Expected return: false

        #Input helloWorld
        #Expected return: false

        #Input "" (N/A)
        #Expected return: false
        self.fail()

    def test_setContactLogID(self):
        self.fail()
