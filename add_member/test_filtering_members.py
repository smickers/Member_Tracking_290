from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, CoreAPIClient
from django.core.exceptions import ValidationError
from .models import Person
from views import MemberFilterView
from rest_framework.test import RequestsClient

class FilterMembers(TestCase):
    tempPerson = Person()
    tempPerson2 = Person()
    tempPerson3 = Person()

    def setUp(self):
        client = Client()

        self.tempPerson.memberID = 111111111
        self.tempPerson.firstName = 'Bob'
        self.tempPerson.middleName = 'Joe'
        self.tempPerson.lastName = 'Smith'
        self.tempPerson.socNum = 111111111
        self.tempPerson.city = 'Saskatoon'
        self.tempPerson.mailAddress = '123 street'
        self.tempPerson.mailAddress2 = 'abc street'
        self.tempPerson.pCode = 'S7L 1Y7'
        self.tempPerson.hPhone = '(306)111-1111'
        self.tempPerson.cPhone = '(306)222-2222'
        self.tempPerson.hEmail = 'bob@abc.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Committee 2'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '1990-03-03'
        self.tempPerson.hireDate = '2012-03-03'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.membershipStatus = 'RESOURCE'
        self.tempPerson.programChoice = 'Sample Program'
        self.tempPerson.full_clean()
        self.tempPerson.save()

        self.tempPerson2.memberID = 111111112
        self.tempPerson2.firstName = 'Jill'
        self.tempPerson2.middleName = 'Ana'
        self.tempPerson2.lastName = 'Smith'
        self.tempPerson2.socNum = 999111888
        self.tempPerson2.city = 'Saskatoon'
        self.tempPerson2.mailAddress = 'abc street'
        self.tempPerson2.mailAddress2 = '123 street'
        self.tempPerson2.pCode = 'S7L 1Y7'
        self.tempPerson2.hPhone = '(306)111-1112'
        self.tempPerson2.cPhone = '(306)555-5555'
        self.tempPerson2.hEmail = 'jill@abc.com'
        self.tempPerson2.campus = 'SASKATOON'
        self.tempPerson2.jobType = 'FTO'
        self.tempPerson2.committee = 'Sample Committee'
        self.tempPerson2.memberImage = 'image.img'
        self.tempPerson2.bDay = '1989-09-10'
        self.tempPerson2.hireDate = '2009-03-20'
        self.tempPerson2.gender = 'FEMALE'
        self.tempPerson2.membershipStatus = 'RESOURCE'
        self.tempPerson2.programChoice = 'Sample Program'
        self.tempPerson2.full_clean()
        self.tempPerson2.save()

        self.tempPerson3.memberID = 111111113
        self.tempPerson3.firstName = 'John'
        self.tempPerson3.middleName = 'Bill'
        self.tempPerson3.lastName = 'Dale'
        self.tempPerson3.socNum = 999111444
        self.tempPerson3.city = 'Regina'
        self.tempPerson3.mailAddress = 'fgh street'
        self.tempPerson3.mailAddress2 = '777  street'
        self.tempPerson3.pCode = 'S0J 1Y6'
        self.tempPerson3.hPhone = '(306)111-1113'
        self.tempPerson3.cPhone = '(306)444-4444'
        self.tempPerson3.hEmail = 'john.bill@abc.org'
        self.tempPerson3.campus = 'REGINA'
        self.tempPerson3.jobType = 'PTO'
        self.tempPerson3.committee = 'Sample Committee'
        self.tempPerson3.memberImage = 'image.img'
        self.tempPerson3.bDay = '1985-09-10'
        self.tempPerson3.hireDate = '2012-10-20'
        self.tempPerson3.gender = 'MALE'
        self.tempPerson3.membershipStatus = 'RESOURCE'
        self.tempPerson3.programChoice = 'Sample Program'
        self.tempPerson3.full_clean()
        self.tempPerson3.save()

    def test_filter_first_name(self):
        response = self.client.get('/api-root/member/filter/', {'firstName': 'Jill'})
        # self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson2.firstName)

    def test_filter_last_name(self):
        response = self.client.get('/api-root/member/filter/', {'lastName': 'Smith'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)

    def test_filter_middle_name(self):
        response = self.client.get('/api-root/member/filter/', {'middleName': 'Joe'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)

    def test_filter_saskpolytech_id(self):
        response = self.client.get('/api-root/member/filter/', {'memberID': 111111111})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)

    def test_filter_SIN(self):
        response = self.client.get('/api-root/member/filter/', {'SIN': 999111444})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson3.memberID)

    def test_filter_city(self):
        response = self.client.get('/api-root/member/filter/', {'city': 'Saskatoon'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)

    def test_filter_mail_address(self):
        response = self.client.get('/api-root/member/filter/', {'mailAddress': 'fgh street'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson3.memberID)

    def test_filter_mail_address_2(self):
        response = self.client.get('/api-root/member/filter/', {'mailAddress2': '123 street'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson2.memberID)

    def test_filter_pcode(self):
        response = self.client.get('/api-root/member/filter/', {'pCode': 'S7L 1Y7'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)

    def test_filter_from_birthdate_and_on(self):
        response = self.client.get('/api-root/member/filter/', {'min_bDay': '1990-03-03'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)

    def test_filter_between_birth_dates(self):
        response = self.client.get('/api-root/member/filter/', {'min_bDay': '1985-09-10', 'max_bDay': '1990-03-03'})
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)
        self.assertEqual(response.json()['results'][2]['memberID'], self.tempPerson3.memberID)

    def test_filter_gender(self):
        response = self.client.get('/api-root/member/filter/', {'gender': 'MALE'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson3.memberID)

    def test_filter_hphone(self):
        response = self.client.get('/api-root/member/filter/', {'hPhone': '(306)111-1113'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson3.memberID)

    def test_filter_cphone(self):
        response = self.client.get('/api-root/member/filter/', {'cPhone': '(306)111-1113'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson3.memberID)

    def test_filter_hemail(self):
        response = self.client.get('/api-root/member/filter/', {'hEmail': 'john.bill@abc.org'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson3.memberID)

    def test_filter_campus(self):
        response = self.client.get('/api-root/member/filter/', {'campus': 'SASKATOON'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)

    def test_filter_job_type(self):
        response = self.client.get('/api-root/member/filter/', {'jobType': 'FTO'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)

    def test_filter_committee(self):
        response = self.client.get('/api-root/member/filter/', {'committee': 'Sample Committee 2'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)

    def test_filter_program_choice(self):
        response = self.client.get('/api-root/member/filter/', {'programChoice': 'Sample Program'})
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)
        self.assertEqual(response.json()['results'][2]['memberID'], self.tempPerson3.memberID)

    def test_filter_membership_status(self):
        response = self.client.get('/api-root/member/filter/', {'membershipStatus': 'RESOURCE'})
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)
        self.assertEqual(response.json()['results'][2]['memberID'], self.tempPerson3.memberID)

    def test_filter_from_hire_date_and_on(self):
        response = self.client.get('/api-root/member/filter/', {'min_hDay': '2012-03-03'})
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['memberID'], self.tempPerson.memberID)
        self.assertEqual(response.json()['results'][1]['memberID'], self.tempPerson2.memberID)
        self.assertEqual(response.json()['results'][2]['memberID'], self.tempPerson3.memberID)

    def test_filter_between_hire_dates(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?hireDateFrom=2010-01-01&hireDateTo=2012-12-31')
        self.assertEqual(len(request.data), 2)

    def test_filter_firstname_AND_city(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?firstName=Bob&city=Saskatoon')
        self.assertEqual(len(request.data), 1)

    def test_filter_lastname_city(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?lastName=Smith&city=Saskatoon')
        self.assertEqual(len(request.data), 2)

    def test_filter_jobtype_AND_campus(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?city=Regina&jobType=Full-time ongoing')
        self.assertEqual(len(request.data), 1)

    def test_filter_hiredate_AND_campus(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?hireDateFrom=2012-01-01&hireDateTo=2012-12-31&campus=Saskatoon')
        self.assertEqual(len(request.data), 1)

    def test_filter_firstname_OR_lastname(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?firstName=John&lastName=Smith')
        self.assertEqual(len(request.data), 3)

    def test_filter_city_OR_jobtype(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?city=Regina&jobType=Full-time ongoing')
        self.assertEqual(len(request.data), 3)

    def test_filter_on_conditions_and_which_no_members_returned(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?city=Moose Jaw&jobType=Part-time end')
        self.assertEqual(len(request.data), 0)

    def test_filter_name_with_wild_cards(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?abc.com')
        self.assertEqual(len(request.data), 2)

    def test_filter_pcode_with_wild_cards(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?pCode=S7L')
        self.assertEqual(len(request.data), 2)