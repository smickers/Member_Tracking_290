from unittest import TestCase
#from contact_log import contact_log


class TestContactLog(TestCase):
    def test_createContactLog(self):
        self.assertEquals('a', 'a')
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
        # self.fail()

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

        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.
        Aenean massa. Cum sociis natoque penatibus et magnis dis p

        Above is 150 characters.
        Expected Result: true


        Input

        Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pa

        Above is 151 characters.
        Expected Result: False
        '''

        self.fail()

    def test_boundsMemberID(self):
        # Unit Test Information
        # Test: Test that a memberID can be a value up to
        # 2147483647
        # Input: 2147483647
        # Expected return: true

        #Input: 0
        #Expected return: true

        #Input: -1
        #Expected return: true

        #Input: 2147483648 - one above the maximum Int32 value
        #Expected return: false

        #Input helloWorld
        #Expected return: false

        #Input "" (N/A)
        #Expected return: true
        self.fail()

    def test_setContactLogID(self):
        self.fail()
