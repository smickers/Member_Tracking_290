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
    dw = Person()
    kk = Person()
    ww = Person()
    jc = Person()
    c1 = Case()
    c2 = Case()
    c3 = Case()
    c4 = Case()

    # Setup Method
    def setUp(self):
        self.dw.memberID = 4204444
        self.dw.firstName = 'Deborah'
        self.dw.middleName = 'Mary'
        self.dw.lastName = 'Williams'
        self.dw.socNum = 123456789
        self.dw.city = 'Saskatoon'
        self.dw.mailAddress = 'Sample address'
        self.dw.mailAddress2 = 'Sample Address 2'
        self.dw.pCode = 'S7K5J8'
        self.dw.hPhone = '(306)812-1234'
        self.dw.cPhone = '(306)812-1234'
        self.dw.hEmail = 'sample@sample.com'
        self.dw.campus = 'SASKATOON'
        self.dw.jobType = 'FTO'
        self.dw.committee = 'Sample Commitee'
        self.dw.memberImage = 'image.img'
        self.dw.bDay = '2012-03-03'
        self.dw.hireDate = '2012-03-03'
        self.dw.gender = 'MALE'
        self.dw.membershipStatus = 'RESOURCE'
        self.dw.programChoice = 'Sample Program'
        self.dw.full_clean()
        self.dw.save()

        self.kk.memberID = 4204444
        self.kk.firstName = 'Kelly'
        self.kk.middleName = 'Mason'
        self.kk.lastName = 'Kentucky'
        self.kk.socNum = 123456789
        self.kk.city = 'Regina'
        self.kk.mailAddress = 'Sample address'
        self.kk.mailAddress2 = 'Sample Address 2'
        self.kk.pCode = 'S7K5J8'
        self.kk.hPhone = '(306)812-1234'
        self.kk.cPhone = '(306)812-1234'
        self.kk.hEmail = 'sample@sample.com'
        self.kk.campus = 'REGINA'
        self.kk.jobType = 'PTED'
        self.kk.committee = 'Sample Commitee'
        self.kk.memberImage = 'image.img'
        self.kk.bDay = '2012-03-03'
        self.kk.hireDate = '2012-03-03'
        self.kk.gender = 'MALE'
        self.kk.membershipStatus = 'RESOURCE'
        self.kk.programChoice = 'Sample Program'
        self.kk.full_clean()
        self.kk.save()

        self.ww.memberID = 4204444
        self.ww.firstName = 'Walky'
        self.ww.middleName = 'E'
        self.ww.lastName = 'Walkerton'
        self.ww.socNum = 123456789
        self.ww.city = 'Prince Albert'
        self.ww.mailAddress = 'Sample address'
        self.ww.mailAddress2 = 'Sample Address 2'
        self.ww.pCode = 'S7K5J8'
        self.ww.hPhone = '(306)812-1234'
        self.ww.cPhone = '(306)812-1234'
        self.ww.hEmail = 'sample@sample.com'
        self.ww.campus = 'PA'
        self.ww.jobType = 'PTO'
        self.ww.committee = 'Sample Commitee'
        self.ww.memberImage = 'image.img'
        self.ww.bDay = '2012-03-03'
        self.ww.hireDate = '2012-03-03'
        self.ww.gender = 'MALE'
        self.ww.membershipStatus = 'RESOURCE'
        self.ww.programChoice = 'Sample Program'
        self.ww.full_clean()
        self.ww.save()

        self.jc.memberID = 4204444
        self.jc.firstName = 'Joyce'
        self.jc.middleName = 'A'
        self.jc.lastName = 'Christian'
        self.jc.socNum = 123456789
        self.jc.city = 'Moose Jaw'
        self.jc.mailAddress = 'Sample address'
        self.jc.mailAddress2 = 'Sample Address 2'
        self.jc.pCode = 'S7K5J8'
        self.jc.hPhone = '(306)812-1234'
        self.jc.cPhone = '(306)812-1234'
        self.jc.hEmail = 'sample@sample.com'
        self.jc.campus = 'PA'
        self.jc.jobType = 'PTO'
        self.jc.committee = 'Sample Commitee'
        self.jc.memberImage = 'image.img'
        self.jc.bDay = '2012-03-03'
        self.jc.hireDate = '2012-03-03'
        self.jc.gender = 'MALE'
        self.jc.membershipStatus = 'RESOURCE'
        self.jc.programChoice = 'Sample Program'
        self.jc.full_clean()
        self.jc.save()

        self.c1prog = CasePrograms(name="Dental Hygiene - Diploma")
        self.c1prog.save()
        self.c1.lead = 123456789
        self.c1.complainant = self.dw
        self.c1.campus = "Saskatoon"
        self.c1.school = "School of Health Sciences"
        self.c1.program = self.c1prog
        self.c1.caseType = 1
        self.c1.status = "OPEN"
        self.c1.docs = None
        self.c1.logs = None
        self.c1.date = "2016-10-20"
        self.c1.full_clean()
        self.c1.save()

        self.c2prog = CasePrograms(name="Carpentry - Certificate")
        self.c2prog.save()
        self.c2.lead = 123456789
        self.c2.complainant = self.kk
        self.c2.campus = "Regina"
        self.c2.school = "School of Construction"
        self.c2.program = self.c2prog
        self.c2.caseType = 2
        self.c2.status = "OPEN"
        self.c2.docs = None
        self.c2.logs = None
        self.c2.date = "2016-11-20"
        self.c2.full_clean()
        self.c2.save()

        self.c3prog = CasePrograms(name="Aboriginal Policing Preparation - Certificate")
        self.c3prog.save()
        self.c3.lead = 123456789
        self.c3.complainant = self.ww
        self.c3.campus = "Saskatoon"
        self.c3.school = "School of Human Services and Community Safety"
        self.c3.program = self.c3prog
        self.c3.caseType = 3
        self.c3.status = "OPEN"
        self.c3.docs = None
        self.c3.logs = None
        self.c3.date = "2015-10-20"
        self.c3.full_clean()
        self.c3.save()

        self.c4.lead = 123456789
        self.c4.complainant = self.jc
        self.c4.campus = "MJ"
        self.c4.school = "Other"
        self.c4.department = "Student Development"
        self.c4.caseType = 2
        self.c4.status = "OPEN"
        self.c4.docs = None
        self.c4.logs = None
        self.c4.date = "2017-03-28"
        self.c4.full_clean()
        self.c4.save()

    # Test 1: Filters can be applied to a cases's complainant
    def test_filter_complainant(self):
        # Test full name filter
        request = self.client.get("/api-root/case_list/filter/?", {"complainant": self.c1.complainant.pk})
        print (request.json())
        self.assertEquals(request.json()['count'], 1)
        self.assertEquals(request.json()['results'][0]["id"], self.c1.complainant.pk)
        # Test partial first name filter
        r2 = self.client.get("/api-root/case_list/filter/?", {"complainant": "Deb"})
        print(r2.json())
        self.assertEquals(r2.json()['count'], 1)
        self.assertEquals(r2.json()['results'][0]["complainant"], self.c1.complainant)
        # Test partial last name filter
        r3 = self.client.get("/api-root/case_list/filter/?", {"complainant": "Williams"})
        self.assertEquals(r3.json()['count'], 1)
        self.assertEquals(r3.json()['results'][0]["complainant"], self.c1.complainant)

    # Test 2: Filters can be applied to a case's campus
    def test_filter_campus(self):
        request = self.client.get("/api-root/case_list/filter/?", {"campus": "Saskatoon"})
        self.assertEquals(request.json()['count'], 2)

    # Test 3: Filters can be applied to a case's school
    def test_filter_school(self):
        request = self.client.get("/api-root/case_list/filter/?", {"school": "School of Health Sciences"})
        self.assertEquals(request.json()['count'], 1)

    # Test 4: Filters can be applied to a case's program
    def test_filter_program(self):
        request = self.client.get("/api-root/case_list/filter/?", {"program": "School of Health Sciences"})
        self.assertEquals(request.json()['count'], 1)

    # Test 5: Filters can be applied to a case's department
    def test_filter_dept(self):
        request = self.client.get("/api-root/case_list/filter/?", {"department": "Student Development"})
        self.assertEquals(request.json()['count'], 1)
        r2 = self.client.get("/api-root/case_list/filter/", {"department": "PLAR"})
        self.assertEquals(r2.json()['count'], 0)

    # Test 6: Filters can be applied to a case's case type
    def test_filter_caseType(self):
        request = self.client.get("/api-root/case_list/filter/?", {"caseType": 2})
        self.assertEquals(request.json()['count'], 2)

    # Test 7: Filters can be applied to a case's status
    def test_filter_status(self):
        request = self.client.get("/api-root/case_list/filter/?", {"status": "OPEN"})
        self.assertEquals(request.json()['count'], 4)

    # Test 8: Multiple filters can be applied with a logical AND
    def test_AND_filter(self):
        request = self.client.get("/api-root/case_list/filter/?", {"complainant": "Walky", "campus": "MJ"})
        self.assertEquals(request.json()['count'], 2)

    # Test 9: Multiple filters can be applied with a logical OR
    def test_OR_filter(self):
        request = self.client.get("/api-root/case_list/filter/?", {"complainant": "Walky"})
        r1 = request.json()['results']
        request2 = self.client.get("/api-root/case_list/filter/?", {"school": "Other"})
        r2 = request.json()['results']
        everything = result_combine(r1, r2)
        self.assertEquals(len(everything), 2)

    # Test 10: Logical AND/OR can be strung together
    def test_logic_chaining(self):
        request = self.client.get("/api-root/case_list/filter/?", {"complainant": "Walky", "caseType": 2})
        r1 = request.json()['results']
        request2 = self.client.get("/api-root/case_list/filter/?", {"school": "Other"})
        r2 = request.json()['results']
        everything = result_combine(r1, r2)
        self.assertEquals(len(everything), 3)

    # Test 11: Filter cases on a date
    def test_filter_dates(self):
        response = self.client.get('/api-root/case_list/filter/?', {"date": "2016-10-20"})
        self.assertEquals(response.json()['count'], 1)

    # Test 12: Filter cases on a range of dates
    def test_filter_dates_with_range(self):
        response = self.client.get('/api-root/case_list/filter/?', {"date": "2016-09-20", "date": "2016-12-20"})
        self.assertEquals(response.json()['count'], 2)

    # Test 13: Empty filter returns the entire list
    def test_filter_with_empty_filter(self):
        request = self.client.get("/api-root/case_list/filter/?")
        self.assertEqual(request.json()['count'], 4)
