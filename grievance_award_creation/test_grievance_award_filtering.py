from django.test import TestCase, Client
from .models import GrievanceAward, Case, Person
from add_case.models import CasePrograms
from django.test import LiveServerTestCase


class FilterGrievanceAwards(TestCase):
    client = Client()
    ga1 = GrievanceAward()
    ga2 = GrievanceAward()
    ga3 = GrievanceAward()
    def setUp(self):
        GrievanceAward.objects.all().delete()
        # Set up a program
        self.program = CasePrograms()
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

        # Set up a Member for testing
        self.tempPerson1 = Person()
        self.tempPerson1.memberID = 689054
        self.tempPerson1.firstName = 'First'
        self.tempPerson1.middleName = 'Middle'
        self.tempPerson1.lastName = 'Last'
        self.tempPerson1.socNum = 123456789
        self.tempPerson1.city = 'Sample City'
        self.tempPerson1.mailAddress = 'Sample address'
        self.tempPerson1.mailAddress2 = 'Sample Address 2'
        self.tempPerson1.pCode = 's7k5j8'
        self.tempPerson1.hPhone = '(306)812-1234'
        self.tempPerson1.cPhone = '(306)812-1234'
        self.tempPerson1.hEmail = 'sample@sample.com'
        self.tempPerson1.campus = 'SASKATOON'
        self.tempPerson1.jobType = 'FTO'
        self.tempPerson1.committee = 'Sample Commitee'
        self.tempPerson1.memberImage = 'image.img'
        self.tempPerson1.bDay = '2012-03-03'
        self.tempPerson1.hireDate = '2012-03-03'
        self.tempPerson1.gender = 'MALE'
        self.tempPerson1.membershipStatus = 'RESOURCE'
        self.tempPerson1.programChoice = 'Sample Program'
        self.tempPerson1.full_clean()
        self.tempPerson1.save()

        self.tempPerson2 = Person()
        self.tempPerson2.memberID = 99999
        self.tempPerson2.firstName = 'Last'
        self.tempPerson2.middleName = 'Middle'
        self.tempPerson2.lastName = 'First'
        self.tempPerson2.socNum = 987654321
        self.tempPerson2.city = 'Sample Town'
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



        # Set up the cases for testing purposes
        self.tempCase1 = Case()
        self.tempCase1.lead = self.tempPerson1.id
        self.tempCase1.complainant = self.tempPerson1
        self.tempCase1.campus = "Saskatoon"
        self.tempCase1.school = "School of Business"
        self.tempCase1.program = self.program
        self.tempCase1.caseType = 7
        self.tempCase1.status = "OPEN"
        self.tempCase1.date = "2016-10-20"
        self.tempCase1.full_clean()
        self.tempCase1.save()


        self.tempCase2 = Case()
        self.tempCase2.lead = self.tempPerson2.id
        self.tempCase2.complainant = self.tempPerson2
        self.tempCase2.campus = "Saskatoon"
        self.tempCase2.school = "School of Business"
        self.tempCase2.program = self.program
        self.tempCase2.caseType = 4
        self.tempCase2.status = "OPEN"
        self.tempCase2.date = "2016-10-20"
        self.tempCase2.full_clean()
        self.tempCase2.save()
        self.tempCase2.additionalMembers.add(self.tempPerson1)
        self.tempCase2.save()

        self.tempCase3 = Case()
        self.tempCase3.lead = self.tempPerson2.id
        self.tempCase3.complainant = self.tempPerson2
        self.tempCase3.campus = "Saskatoon"
        self.tempCase3.school = "School of Information and Communications Technology"
        self.tempCase3.program = self.program
        self.tempCase3.caseType = 7
        self.tempCase3.status = "OPEN"
        self.tempCase3.date = "2016-10-20"
        self.tempCase3.full_clean()
        self.tempCase3.save()

        # Set up a grievence award to be edited
        self.ga1.case = self.tempCase1
        self.ga1.awardAmount = 2500.00
        self.ga1.description = "Test"
        self.ga1.date = '2017-12-01'
        self.ga1.full_clean()
        self.ga1.save()

        self.ga2.case = self.tempCase2
        self.ga2.awardAmount = 50.00
        self.ga2.description = ""
        self.ga2.date = '2015-12-01'
        self.ga2.full_clean()
        self.ga2.save()

        self.ga3.case = self.tempCase3
        self.ga3.awardAmount = 500.00
        self.ga3.description = "Rest"
        self.ga3.date = '2016-12-01'
        self.ga3.full_clean()
        self.ga3.save()

    # Test that you can filter on the Award Type
    def test_type_filetering(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'case__caseType': 7})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['id'], self.ga1.id)
        self.assertEqual(response.json()['results'][1]['id'], self.ga3.id)

    # Test that you can filter on Award Amount
    def test_award_amount_filtering(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'awardAmount': '50.00'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], self.ga2.id)

    # Test that you can filter on an Award Amount Range
    def test_award_aamount_range(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'min_amount': '50.00', 'max_amount': '2000.00'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['id'], self.ga2.id)
        self.assertEqual(response.json()['results'][1]['id'], self.ga3.id)

    # Test that you can filter on Award Description
    def test_award_description(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'description__contains': 'es'})
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['id'], self.ga1.id)
        self.assertEqual(response.json()['results'][1]['id'], self.ga3.id)

    # Test that you can filter on Award Date
    def test_award_date(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'date': '2016-12-01'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], self.ga3.id)

    # Test that you can filter on an Award Date Range
    def test_award_date_range(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'limit': 3, 'min_date': '2015-12-01', 'max_date': '2017-12-01'})
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['id'], self.ga1.id)
        self.assertEqual(response.json()['results'][1]['id'], self.ga2.id)
        self.assertEqual(response.json()['results'][2]['id'], self.ga3.id)

    # Test that you can filter on Type and Amount in one Query
    def test_type_and_amount(self):
        response = self.client.get('/api-root/grievance_award/filter/', {'type': 'M', 'awardAmount': '500.00'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], self.ga3.id)

    # Test that you can filter with an Empty Filter
    def test_empty_filter(self):
        response = self.client.get('/api-root/grievance_award/filter/?limit=3')
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(response.json()['results'][0]['id'], self.ga1.id)
        self.assertEqual(response.json()['results'][1]['id'], self.ga2.id)
        self.assertEqual(response.json()['results'][2]['id'], self.ga3.id)

    # Test that you can test all fields in one query
    def test_all_fields_in_one_filter(self):
        response = self.client.get('/api-root/grievance_award/filter/',
                                   {'format': 'json', 'min_date': '2015-12-01', 'max_date': '2017-12-01',
                                    'awardAmount': "2500.00", 'description': 'Test', 'type': 'M'})
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], self.ga1.id)
