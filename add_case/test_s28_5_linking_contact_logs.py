from django.test import TestCase
from add_case.models import *
from contact_log.models import contactLog
from add_member.models import Person
from django.core.urlresolvers import reverse


# Class:    CaseContactLogLinking
# Purpose:  Unit tests to ensure that behavior for relating contact logs to cases functions correctly.
class CaseContactLogLinking_S28_5(TestCase):
    member_one = Person()
    cl_w_relatedCase = contactLog()
    cl_no_relatedCase = contactLog()
    cl_no_relatedCase2 = contactLog()
    case_w_contactlogs = Case()
    case_no_contactlogs = Case()
    program = CasePrograms()



    # Function: setUp
    # Purpose:  Set up some objects for use in the following unit tests.
    def setUp(self):

        # First, empty out the case table
        Case.objects.all().delete()
        # Set up the person
        self.member_one.memberID = 4204444
        self.member_one.firstName = 'First'
        self.member_one.middleName = 'Middle'
        self.member_one.lastName = 'Last'
        self.member_one.socNum = 123456789
        self.member_one.city = 'Sample City'
        self.member_one.mailAddress = 'Sample address'
        self.member_one.mailAddress2 = 'Sample Address 2'
        self.member_one.pCode = 's7k5j8'
        self.member_one.hPhone = '(306)812-1234'
        self.member_one.cPhone = '(306)812-1234'
        self.member_one.hEmail = 'sample@sample.com'
        self.member_one.campus = 'SASKATOON'
        self.member_one.jobType = 'FTO'
        self.member_one.committee = 'Sample Commitee'
        self.member_one.memberImage = 'image.img'
        self.member_one.bDay = '2012-03-03'
        self.member_one.hireDate = '2012-03-03'
        self.member_one.gender = 'MALE'
        self.member_one.membershipStatus = 'RESOURCE'
        self.member_one.programChoice = 'Sample Program'
        self.member_one.full_clean()
        self.member_one.save()

        # Set up the three contact logs
        self.cl_w_relatedCase.member = self.member_one
        self.cl_w_relatedCase.date = '2017-02-02'
        self.cl_w_relatedCase.description = 'Hello'
        self.cl_w_relatedCase.contactCode = 'F'
        self.cl_w_relatedCase.relatedCase = None
        self.cl_w_relatedCase.clean()
        self.cl_w_relatedCase.save()

        self.cl_no_relatedCase.member = self.member_one
        self.cl_no_relatedCase.date = '2017-02-02'
        self.cl_no_relatedCase.description = 'Hello'
        self.cl_no_relatedCase.contactCode = 'F'
        self.cl_no_relatedCase.relatedCase = None
        self.cl_no_relatedCase.clean()
        self.cl_no_relatedCase.save()

        self.cl_no_relatedCase2.member = self.member_one
        self.cl_no_relatedCase2.date = '2017-02-02'
        self.cl_no_relatedCase2.description = 'Hello'
        self.cl_no_relatedCase2.contactCode = 'F'
        self.cl_no_relatedCase2.relatedCase = None
        self.cl_no_relatedCase2.clean()
        self.cl_no_relatedCase2.save()

        # Set up a program for the case
        self.program.name = 'CST'
        self.program.full_clean()
        self.program.save()

        # Set up the case
        self.case_w_contactlogs.lead = 123456789
        self.case_w_contactlogs.complainant = self.member_one
        self.case_w_contactlogs.campus = "Saskatoon"
        self.case_w_contactlogs.school = "School of Business"
        self.case_w_contactlogs.program = self.program
        self.case_w_contactlogs.caseType = 3
        self.case_w_contactlogs.status = "OPEN"
        self.case_w_contactlogs.additionalNonMembers = ""
        self.case_w_contactlogs.docs = None
        self.case_w_contactlogs.logs = None
        self.case_w_contactlogs.date = "2016-10-20"
        self.case_w_contactlogs.full_clean()
        self.case_w_contactlogs.save()

        self.cl_w_relatedCase = self.case_w_contactlogs
        self.cl_w_relatedCase.full_clean()
        self.cl_w_relatedCase.save()

        self.case_no_contactlogs.lead = 123456789
        self.case_no_contactlogs.complainant = self.member_one
        self.case_no_contactlogs.campus = "Saskatoon"
        self.case_no_contactlogs.school = "School of Business"
        self.case_no_contactlogs.program = self.program
        self.case_no_contactlogs.caseType = 3
        self.case_no_contactlogs.status = "OPEN"
        self.case_no_contactlogs.additionalNonMembers = ""
        self.case_no_contactlogs.docs = None
        self.case_no_contactlogs.logs = None
        self.case_no_contactlogs.date = "2016-10-20"
        self.case_no_contactlogs.full_clean()
        self.case_no_contactlogs.save()




    def test_link_contact_log_to_existing_case_w_no_logs(self):
        self.cl_no_relatedCase.relatedCase = self.case_no_contactlogs
        self.cl_no_relatedCase.full_clean()
        self.cl_no_relatedCase.save()

        response = self.client.get('http://127.0.0.1:8000/api-root/contact_log/search/', {"relatedCase": self.case_no_contactlogs.pk})
        self.assertEqual(response.json()['count'], 1)



    def test_link_contact_log_to_existing_case_w_logs(self):
        self.cl_no_relatedCase2.relatedCase = self.case_w_contactlogs
        self.cl_no_relatedCase2.full_clean()
        self.cl_no_relatedCase2.save()

        response = self.client.get('http://127.0.0.1:8000/api-root/contact_log/search/',{"relatedCase": self.case_w_contactlogs.pk})
        self.assertEqual(response.json()['count'], 1)
