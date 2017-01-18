from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Event

class DateFormatTestCase(TestCase):
    #Test that the date is loading in the proper format in the proper format
    def test_proper_date_format_is_loading(self):
        # Instantiate the Client
        client = Client()
        # Connect to the actual sites
        response = client.get('/add_event/add/')
        # Get the initial values found in the model & view
        #print(response.context)
        oldresponsevalues = response.context['form']
        print(oldresponsevalues);
        #self.assertRegexpMatches(oldresponsevalues.__str__(),
        #            "^(?s).*(id_bDay_day).(?s).*(id_bDay_month)(?s).*(id_bDay_year)(?s).*$")

    # def test_old_format_is_not_loading(self):
    #     event_to_edit = Event.objects.filter(id=1)[0]
    #     # Instantiate the Client
    #     client = Client()
    #     # Connect to the actual sites
    #     response = client.get('/add_event/add/' + str(event_to_edit.pk) + '/')
    #     # Get the initial values found in the model & view
    #     # print(response.context)
    #     oldresponsevalues = response.context['form']
    #     self.assertNotRegexpMatches(oldresponsevalues.__str__(),
    #             "^(?s).*(id_bDay_month).(?s).*(id_bDay_day)(?s).*(id_bDay_year)(?s).*$")
