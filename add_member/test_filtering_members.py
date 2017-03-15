from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, CoreAPIClient
from django.core.exceptions import ValidationError
from .models import Person
from views import MemberFilterView
from rest_framework.test import RequestsClient

class FilterMembers(TestCase):

    def setUp(self):
        client = Client()

        tempPerson = Person()
        tempPerson.memberID = 111111111
        tempPerson.firstName = 'Jill'
        tempPerson.middleName = 'Ana'
        tempPerson.lastName = 'Smith'
        tempPerson.socNum = 111111112
        tempPerson.city = 'Saskatoon'
        tempPerson.mailAddress = '123 street'
        tempPerson.mailAddress2 = '123 street'
        tempPerson.pCode = 'S7L 1Y7'
        tempPerson.hPhone = '(306)111-1112'
        tempPerson.cPhone = '(306)555-5555'
        tempPerson.hEmail = 'email@abc.com'
        tempPerson.campus = 'Saskatoon'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '1985-09-10'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()

    def test_filter_first_name(self):
        response = self.client.get('/api-root/member/filter/', {'firstName': ''})
        print(response.content)
        print(response.json())
        self.assertEqual(response.json()['count'], 1)

    def test_filter_last_name(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?lastName=Smith')
        self.assertEqual(len(request.data), 2)

    def test_filter_middle_name(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?middleName=Ana')
        self.assertEqual(len(request.data), 1)

    def test_filter_saskpolytech_id(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?memberID=111111111')
        self.assertEqual(len(request.data), 1)

    def test_filter_SIN(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?socNum=111111112')
        self.assertEqual(len(request.data), 1)

    def test_filter_city(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?city=Saskatoon')
        self.assertEqual(len(request.data), 2)

    def test_filter_mail_address(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?mailAddress=123 street')
        self.assertEqual(len(request.data), 1)

    def test_filter_mail_address_2(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?mailAddress2=123 street')
        self.assertEqual(len(request.data), 1)

    def test_filter_pcode(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?pCode=S7L 1Y7')
        self.assertEqual(len(request.data), 2)

    def test_filter_from_birthdate_and_on(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?bDateFrom=1985-09-10')
        self.assertEqual(len(request.data), 1)

    def test_filter_between_birth_dates(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?bDateFrom=1990-01-01&bDateTo=1985-12-31')
        self.assertEqual(len(request.data), 1)

    def test_filter_gender(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?gender=MALE')
        self.assertEqual(len(request.data), 2)

    def test_filter_hphone(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?hPhone=(306)111-1112')
        self.assertEqual(len(request.data), 1)

    def test_filter_cphone(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?cPhone=(306)555-5555')
        self.assertEqual(len(request.data), 1)

    def test_filter_hemail(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?hEmail=email@abc.com')
        self.assertEqual(len(request.data), 1)

    def test_filter_campus(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?campus=Saskatoon')
        self.assertEqual(len(request.data), 2)

    def test_filter_job_type(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?jobType=FTO')
        self.assertEqual(len(request.data), 1)

    def test_filter_committee(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?committee=Spring Dance')
        self.assertEqual(len(request.data), 1)

    def test_filter_program_choice(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?programChoice=Sample')
        self.assertEqual(len(request.data), 3)

    def test_filter_membership_status(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?membershipStatus=RESOURCE')
        self.assertEqual(len(request.data), 2)

    def test_filter_from_hire_date_and_on(self):
        factory = APIRequestFactory()
        request = factory.get('/api-root/member/filter/?hireDateFrom=2012-03-01')
        self.assertEqual(len(request.data), 2)

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