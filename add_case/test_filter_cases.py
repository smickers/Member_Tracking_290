from django.test import LiveServerTestCase
from add_member.models import Person
from .models import Case, CasePrograms
from rest_framework.test import APIRequestFactory


# Courtesy of:
# http://stackoverflow.com/questions/9890364/combine-two-dictionaries-and-remove-duplicates-in-python
def result_combine(list1, list2):
    for item in list1:
        if item not in list2:
            list2.append(item)
    return list2


# Class for testing Case filtering:
class TestFilteringCases(LiveServerTestCase):
    requestFactory = APIRequestFactory()
    # Initialize the objects required for the unit tests


    # Setup Method
    def setUp(self):
        Case.objects.all().delete()
        CasePrograms.objects.all().delete()
        dw = Person()
        kk = Person()
        ww = Person()
        jc = Person()
        c1 = Case()
        c2 = Case()
        c3 = Case()
        c4 = Case()
        dw.memberID = 4204444
        dw.firstName = 'Deborah'
        dw.middleName = 'Mary'
        dw.lastName = 'Williams'
        dw.socNum = 123456789
        dw.city = 'Saskatoon'
        dw.mailAddress = 'Sample address'
        dw.mailAddress2 = 'Sample Address 2'
        dw.pCode = 'S7K5J8'
        dw.hPhone = '(306)812-1234'
        dw.cPhone = '(306)812-1234'
        dw.hEmail = 'sample@sample.com'
        dw.campus = 'SASKATOON'
        dw.jobType = 'FTO'
        dw.committee = 'Sample Commitee'
        dw.memberImage = 'image.img'
        dw.bDay = '2012-03-03'
        dw.hireDate = '2012-03-03'
        dw.gender = 'MALE'
        dw.membershipStatus = 'RESOURCE'
        dw.programChoice = 'Sample Program'
        dw.full_clean()
        dw.save()

        kk.memberID = 4204444
        kk.firstName = 'Kelly'
        kk.middleName = 'Mason'
        kk.lastName = 'Kentucky'
        kk.socNum = 123456789
        kk.city = 'Regina'
        kk.mailAddress = 'Sample address'
        kk.mailAddress2 = 'Sample Address 2'
        kk.pCode = 'S7K5J8'
        kk.hPhone = '(306)812-1234'
        kk.cPhone = '(306)812-1234'
        kk.hEmail = 'sample@sample.com'
        kk.campus = 'REGINA'
        kk.jobType = 'PTED'
        kk.committee = 'Sample Commitee'
        kk.memberImage = 'image.img'
        kk.bDay = '2012-03-03'
        kk.hireDate = '2012-03-03'
        kk.gender = 'MALE'
        kk.membershipStatus = 'RESOURCE'
        kk.programChoice = 'Sample Program'
        kk.full_clean()
        kk.save()

        ww.memberID = 4204444
        ww.firstName = 'Walky'
        ww.middleName = 'E'
        ww.lastName = 'Walkerton'
        ww.socNum = 123456789
        ww.city = 'Prince Albert'
        ww.mailAddress = 'Sample address'
        ww.mailAddress2 = 'Sample Address 2'
        ww.pCode = 'S7K5J8'
        ww.hPhone = '(306)812-1234'
        ww.cPhone = '(306)812-1234'
        ww.hEmail = 'sample@sample.com'
        ww.campus = 'PA'
        ww.jobType = 'PTO'
        ww.committee = 'Sample Commitee'
        ww.memberImage = 'image.img'
        ww.bDay = '2012-03-03'
        ww.hireDate = '2012-03-03'
        ww.gender = 'MALE'
        ww.membershipStatus = 'RESOURCE'
        ww.programChoice = 'Sample Program'
        ww.full_clean()
        ww.save()

        jc.memberID = 4204444
        jc.firstName = 'Joyce'
        jc.middleName = 'A'
        jc.lastName = 'Christian'
        jc.socNum = 123456789
        jc.city = 'Moose Jaw'
        jc.mailAddress = 'Sample address'
        jc.mailAddress2 = 'Sample Address 2'
        jc.pCode = 'S7K5J8'
        jc.hPhone = '(306)812-1234'
        jc.cPhone = '(306)812-1234'
        jc.hEmail = 'sample@sample.com'
        jc.campus = 'PA'
        jc.jobType = 'PTO'
        jc.committee = 'Sample Commitee'
        jc.memberImage = 'image.img'
        jc.bDay = '2012-03-03'
        jc.hireDate = '2012-03-03'
        jc.gender = 'MALE'
        jc.membershipStatus = 'RESOURCE'
        jc.programChoice = 'Sample Program'
        jc.full_clean()
        jc.save()

        c1prog = CasePrograms(name="Dental Hygiene - Diploma")
        c1prog.save()
        c1.lead = 123456789
        c1.complainant = dw
        c1.campus = "Saskatoon"
        c1.school = "School of Health Sciences"
        c1.program = c1prog
        c1.caseType = 1
        c1.status = "OPEN"
        c1.docs = None
        c1.logs = None
        c1.date = "2016-10-20"
        c1.full_clean()
        c1.save()

        c2prog = CasePrograms(name="Carpentry - Certificate")
        c2prog.save()
        c2.lead = 123456789
        c2.complainant = kk
        c2.campus = "Regina"
        c2.school = "School of Construction"
        c2.program = c2prog
        c2.caseType = 2
        c2.status = "OPEN"
        c2.docs = None
        c2.logs = None
        c2.date = "2016-11-20"
        c2.full_clean()
        c2.save()

        c3prog = CasePrograms(name="Aboriginal Policing Preparation - Certificate")
        c3prog.save()
        c3.lead = 123456789
        c3.complainant = ww
        c3.campus = "Saskatoon"
        c3.school = "School of Human Services and Community Safety"
        c3.program = c3prog
        c3.caseType = 3
        c3.status = "OPEN"
        c3.docs = None
        c3.logs = None
        c3.date = "2015-10-20"
        c3.full_clean()
        c3.save()

        c4.lead = 123456789
        c4.complainant = jc
        c4.campus = "MJ"
        c4.school = "Other"
        c4.department = "Student Development"
        c4.caseType = 2
        c4.status = "OPEN"
        c4.docs = None
        c4.logs = None
        c4.date = "2017-03-28"
        c4.full_clean()
        c4.save()

    # Test 1: Filters can be applied to a cases's complainant
    def test_filter_complainant(self):
        # Test full name filter
        request = self.client.get("/api-root/case_list/search/", {"complainant": "Deborah Williams"})
        print(request.json())
        self.assertEquals(request.json()['count'], 1)
        self.assertEquals(request.json()['results'][0]["id"], self.c1.complainant.pk)
        # Test partial first name filter
        r2 = self.client.get("/api-root/case_list/search/?", {"complainant": "Deb"})
        self.assertEquals(r2.json()['count'], 1)
        self.assertEquals(r2.json()['results'][0]["complainant"], self.c1.complainant)
        # Test partial last name filter
        r3 = self.client.get("/api-root/case_list/search/?", {"complainant": "Williams"})
        self.assertEquals(r3.json()['count'], 1)
        self.assertEquals(r3.json()['results'][0]["complainant"], self.c1.complainant)

    # Test 2: Filters can be applied to a case's campus
    def test_filter_campus(self):
        request = self.client.get("/api-root/case_list/search/?", {"campus": "Saskatoon"})
        self.assertEquals(request.json()['count'], 1)

    # Test 3: Filters can be applied to a case's school
    def test_filter_school(self):
        request = self.client.get("/api-root/case_list/search/?", {"school": "School of Health Sciences"})
        self.assertEquals(request.json()['count'], 1)

    # Test 4: Filters can be applied to a case's program
    def test_filter_program(self):
        request = self.client.get("/api-root/case_list/search/?", {"program": "School of Health Sciences"})
        self.assertEquals(request.json()['count'], 1)

    # Test 5: Filters can be applied to a case's department
    def test_filter_dept(self):
        request = self.client.get("/api-root/case_list/search/?", {"department": "Student Development"})
        self.assertEquals(request.json()['count'], 1)
        r2 = self.client.get("/api-root/case_list/search/", {"department": "PLAR"})
        self.assertEquals(r2.json()['count'], 0)

    # Test 6: Filters can be applied to a case's case type
    def test_filter_caseType(self):
        request = self.client.get("/api-root/case_list/search/?", {"caseType": 2})
        self.assertEquals(request.json()['count'], 2)

    # Test 7: Filters can be applied to a case's status
    def test_filter_status(self):
        request = self.client.get("/api-root/case_list/search/?", {"status": "OPEN"})
        self.assertEquals(request.json()['count'], 4)

    # Test 8: Multiple filters can be applied with a logical AND
    def test_AND_filter(self):
        request = self.client.get("/api-root/case_list/search/?", {"complainant": "Walky", "campus": "MJ"})
        self.assertEquals(request.json()['count'], 2)

    # Test 9: Multiple filters can be applied with a logical OR
    def test_OR_filter(self):
        request = self.client.get("/api-root/case_list/search/?", {"complainant": "Walky"})
        r1 = request.json()['results']
        request2 = self.client.get("/api-root/case_list/search/?", {"school": "Other"})
        r2 = request.json()['results']
        everything = result_combine(r1, r2)
        self.assertEquals(len(everything), 2)

    # Test 10: Logical AND/OR can be strung together
    def test_logic_chaining(self):
        request = self.client.get("/api-root/case_list/search/?", {"complainant": "Walky", "caseType": 2})
        r1 = request.json()['results']
        request2 = self.client.get("/api-root/case_list/search/?", {"school": "Other"})
        r2 = request.json()['results']
        everything = result_combine(r1, r2)
        self.assertEquals(len(everything), 3)

    # Test 11: Filter cases on a date
    def test_filter_dates(self):
        response = self.client.get('/api-root/case_list/search/?', {"date": "2016-10-20"})
        self.assertEquals(response.json()['count'], 2)

    # Test 12: Filter cases on a range of dates
    def test_filter_dates_with_range(self):
        response = self.client.get('/api-root/case_list/search/?', {"date": "2016-09-20", "date": "2016-12-20"})
        self.assertEquals(response.json()['count'], 2)

    # Test 13: Empty filter returns the entire list
    def test_filter_with_empty_filter(self):
        request = self.client.get("/api-root/case_list/search/?")
        self.assertEqual(request.json()['count'], 4)
