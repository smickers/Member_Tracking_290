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

        #Input: 01/01/2016
        #Expected Results: Date will be correct

        # Input: 12/12/2016
        # Expected Results: Date will be correct

        # Input: January 1, 2016
        # Expected Results: Date will be correct

        # Input: 30/02/2016
        # Expected Results: Date will be incorrect because Feb has 29 days in 2016

        # Input: 29/02/2015
        # Expected Results: Date will be incorrect because Feb has 28 days in 2015

        # Input: 01/30/2016
        # Expected Results: Date will be incorrect because there are only up to 12 months


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


        Input
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque commodo viverra lacinia. Proin id sollicitudin
        urna. Cras a massa eleifend, interdum mi nec, tempus enim. Donec eget ligula nec leo fermentum imperdiet vel
        et turpis. Donec dapibus nec enim ut rhoncus. Donec dictum est eleifend sollicitudin maximus. Morbi viverra
        volutpat ullamcorper. Nulla interdum ornare elementum. Nullam orci leo, faucibus at semper id, malesuada ac mi.
        Quisque facilisis sem arcu, in ultricies erat lobortis vitae. Vestibulum pellentesque tempus ex, ac fringilla
        erat euismod sit amet. Etiam vel nisi euismod, malesuada nisi id, vulputate nisi. Quisque nec interdum tortor.

        Suspendisse varius nisl metus, in rutrum tellus pharetra et. In nulla ligula, maximus quis sodales ac, semper
        nec neque. Etiam porttitor tortor in luctus rutrum. In elementum magna sed augue consectetur iaculis. Donec
        ornare, diam in accumsan eleifend, tortor odio suscipit dui, nec auctor orci lacus ut urna. Cras ac purus nec dui. Lorem

        Expected Result: False
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
