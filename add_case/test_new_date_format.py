from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class DateFormatTestCase(TestCase):

    #Test that the date is loading in the proper format in the proper format
    def test_proper_date_format_is_loading(self):
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get('/addCase/')
        # Get the initial values found in the model & view
        #print(response.context)
        oldresponsevalues = response.context['form']
        print(oldresponsevalues)
        #Compare response to the regular expression
        self.assertRegexpMatches(oldresponsevalues.__str__(),
                #This regular expression searches for date selectors to load in Day, Month, Year
                 "^(?s).*(id_date_day).(?s).*(id_date_month)(?s).*(id_date_year)(?s).*$")

    #Test that the date is not loading in the unproper format
    def test_old_format_is_not_loading(self):
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get('/addCase/')
        # Get the initial values found in the model & view
        # print(response.context)
        oldresponsevalues = response.context['form']
        print(oldresponsevalues)
        #Compare respons to the regular expression
        self.assertNotRegexpMatches(oldresponsevalues.__str__(),
                #This regular expression searches for date selectors to load in Day, Month, Year
                "^(?s).*(id_date_month).(?s).*(id_date_day)(?s).*(id_date_year)(?s).*$")
