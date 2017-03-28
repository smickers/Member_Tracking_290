from django.test import TestCase
from add_case.models import *
from contact_log.models import contactLog
from add_member.models import Person
from django.core.exceptions import ValidationError
from rest_framework.test import APIRequestFactory
from forms import CaseForm

# Class:    CaseContactLogLinking
# Purpose:  Unit tests to ensure that behavior for relating contact logs to cases functions correctly.
class CaseContactLogLinking(TestCase):
    member_one = Person()
    cl_one = contactLog()
    cl_two = contactLog()
    case_one = Case()
    case_two = Case()
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

        # Set up the two contact logs
        self.cl_one.member = self.member_one
        self.cl_one.date = '2017-02-02'
        self.cl_one.description = 'Hello'
        self.cl_one.contactCode = 'F'
        self.cl_one.relatedCase = None
        self.cl_one.clean()
        self.cl_one.save()

        self.cl_two.member = self.member_one
        self.cl_two.date = '2017-02-02'
        self.cl_two.description = 'Hello'
        self.cl_two.contactCode = 'F'
        self.cl_two.relatedCase = None
        self.cl_two.clean()
        self.cl_two.save()

        # Set up a program for the case
        self.program.name = 'CST'
        self.program.full_clean()
        self.program.save()

        # Set up the case
        self.case_one.lead = 123456789
        self.case_one.complainant = self.member_one
        self.case_one.campus = "Saskatoon"
        self.case_one.school = "School of Business"
        self.case_one.program = self.program
        self.case_one.caseType = 3
        self.case_one.status = "OPEN"
        self.case_one.additionalNonMembers = ""
        self.case_one.docs = None
        self.case_one.logs = None
        self.case_one.date = "2016-10-20"
        self.case_one.full_clean()
        self.case_one.save()
        self.case_one.additionalMembers.add(self.member_one)
        self.case_one.save()

        self.case_two.lead = 123456789
        self.case_two.complainant = self.member_one
        self.case_two.campus = "Saskatoon"
        self.case_two.school = "School of Business"
        self.case_two.program = self.program
        self.case_two.caseType = 3
        self.case_two.status = "OPEN"
        self.case_two.additionalNonMembers = ""
        self.case_two.docs = None
        self.case_two.logs = None
        self.case_two.date = "2016-10-20"
        self.case_two.full_clean()
        self.case_two.save()
        self.case_two.additionalMembers.add(self.member_one)
        self.case_two.save()

    # Function: test_adding_contact_log_to_case
    # Purpose:  Ensure that a contact log can be linked to a case by creating a case and linking the contact log to the
    #           case.
    def test_adding_contact_log_to_case(self):
        # Link contact log #1 to case #1 and try to save the changes
        try:
            self.cl_one.related_case = self.case_one
            self.cl_one.full_clean()
            self.cl_one.save()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


    # Function: test_linking_an_already_linked_contact_log
    # Purpose:  Ensure that the user cannot link an already-linked contact log to a new case.
    def test_linking_an_already_linked_contact_log(self):
        # Link contact log #1 to case #1, then save the changes
        self.cl_one.relatedCase = self.case_one
        self.cl_one.full_clean()
        self.cl_one.save()

        data = {
            'lead' :'1',
            'complainant': self.member_one.pk,
            'caseType' : 5,
            'related_contact_logs': {self.cl_one.pk},
            'school': 'School of Nursing',
            'status': 'OPEN',
            'campus': 'Saskatoon'
        }

        # Build up a request to send off. Then, validate that it throws an exception.
        with self.assertRaisesMessage(ValidationError, "Contact log is already related to a case!"):
            self.client.post("/addCase/", data)

    # Function: test_linking_unlinking_and_relinking_a_contact_log
    # Purpose: Link a contact log to a case, manually un-link the contact log, and then ensure that the contact log
    #           can be re-linked to a new case.
    def test_linking_unlinking_and_relinking_a_contact_log(self):
        try:
            # Link the contact log through case creation
            data = {
                'lead': '1',
                'complainant': self.member_one.pk,
                'caseType': 5,
                'related_contact_logs': {self.cl_one.pk},
                'school': 'School of Nursing',
                'status': 'OPEN',
                'campus': 'Saskatoon'
            }

            self.client.post("/addCase/", data)

            # Unlink the contact log manually
            self.cl_one.relateCase = None
            self.cl_one.full_clean()
            self.cl_one.save()

            # Re-link the contact log through case creation
            data = {
                'lead': '1',
                'complainant': self.member_one.pk,
                'caseType': 5,
                'related_contact_logs': {self.cl_one.pk},
                'school': 'School of Nursing',
                'status': 'OPEN',
                'campus': 'Saskatoon'
            }

            self.client.post("/addCase/", data)

            # Assert true if this all exectuted without error
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    # Function: test_linking_an_invalid_contact_log
    # Purpose:  Ensure that a valid contact log has to be linked to a case.
    #           An invalid contact log will throw an error.
    def test_linking_an_invalid_contact_log(self):
        try:
            self.cl_one.relatedCase = self.nonexistant_case
            self.cl_one.full_clean()
            self.cl_one.save()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    # Function: test_ensure_that_only_unlinked_contact_logs_are_shown_in_api
    # Purpose:  Make sure that in API lookups, only UNLINKED contact logs are
    #           shown for the unlinked query.
    def test_ensure_that_only_unlinked_contact_logs_are_shown_in_api(self):
        # Link cl_one first
        self.cl_one.relatedCase = self.case_one
        self.cl_one.full_clean()
        self.cl_one.save()

        # Now ensure only one contact log is listed in the list which will fill the select box
        request = self.client.get('/api-root/contact_log/search/?relatedCase_filter=1')
        self.assertEquals(request.json()['count'], 1)
