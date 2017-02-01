from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from create_event.models import Event
from django.db import DataError
import datetime
from add_member.models import Person

class EventTest(TestCase):
    testEvent = None
    tempPerson = None
    tempPerson2 = None
    not_saved_person = None

    def setUp(self):
        """
        Sets up initial data(s)
        :return:
        """
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

    def test__user_cannot_update_event_with_empty_event_name(self):
        with self.assertRaises(IntegrityError):
            self.testEvent.name = None
            self.testEvent.save()

    def test_user_can_update_event_name_with_1_character_long(self):
        self.testEvent.name = 'A'
        self.testEvent.save()
        self.assertTrue(self.testEvent.name == 'A')

    def test_can_update_event_name_with_20_characters_long(self):
        self.testEvent.name = 'adfasfdafdsafdsafdas'
        self.testEvent.save()
        self.assertTrue(self.testEvent.name == 'adfasfdafdsafdsafdas')

    def test_user_cannot_update_event_name_with_21_characters_long(self):
        with self.assertRaises(DataError):
            self.testEvent.name = 'adfasfdafdsafdsafdass'
            self.testEvent.save()

    def test_user_can_update_an_event_description_that_is_empty(self):
        self.testEvent.description = None
        self.testEvent.save()
        self.assertTrue(self.testEvent.description == None)

    def test_user_cannot_update_an_event_description_that_is_51_chars_long(self):
        with self.assertRaises(DataError):
            self.testEvent.description = 'Lorem ipsum dolor sit amet, consectetuer adipiscing'
            self.testEvent.save()

    def test_user_cannot_update_event_if_invalid_date_is_given(self):
        with self.assertRaises(ValidationError):
            self.testEvent.date = '1/3/2015'
            self.testEvent.save()

    def test_user_can_update_if_location_is_not_in_defined_location(self):
        self.testEvent.location = 'honolulu'
        self.testEvent.save()
        self.assertTrue(self.testEvent.location == 'honolulu')

    def test_user_can_update_given_location_defined_in_the_location_list(self):
        self.testEvent.location = 'Saskatoon'
        self.testEvent.save()
        self.assertTrue(self.testEvent.location == 'Saskatoon')

    # def test_user_can_add_a_member_to_an_existing_event(self):
    #     self.fail()
    #
    #
    # def test_user_can_add_multiple_member_to_an_existing_event(self):
    #     self.fail()

    def test_user_can_remove_member_to_an_event(self):
        self.testEvent.members.add(self.tempPerson)
        self.testEvent.members.add(self.tempPerson2)
        self.testEvent.save()

        self.testEvent.members.remove(self.tempPerson)
        self.assertTrue(self.testEvent.members.count() == 1)

    def test_user_can_remove_multiple_members_from_an_event(self):
        self.testEvent.members.add(self.tempPerson)
        self.testEvent.save()

        self.testEvent.members.remove(self.tempPerson)
        self.assertTrue(self.testEvent.members.count() == 0)