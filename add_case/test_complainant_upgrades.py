from django.test import TestCase, Client
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import Case
from django.db import DataError
import datetime
from add_member.models import Person


# Test cases for S25: Ensure CN is removed from list of additional members, when adding a Case
class CaseTests(TestCase):
    person1 = Person()
    person2 = Person()
    person3 = Person()

    # Create our People
    def setUp(self):
        # TODO: Check this page out:
        # https://www.google.ca/webhp?sourceid=chrome-instant&rlz=1C1CHBF_enCA707CA707&ion=1&espv=2&ie=UTF-8#q=manage.py%20call%20django%20unit%20test
        self.person1.memberID = 4204444
        self.person1.firstName = 'Deborah'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Williams'
        self.person1.socNum = 123456789
        self.person1.city = 'Sample City'
        self.person1.mailAddress = 'Sample address'
        self.person1.mailAddress2 = 'Sample Address 2'
        self.person1.pCode = 's7k5j8'
        self.person1.hPhone = '(306)812-1234'
        self.person1.cPhone = '(306)812-1234'
        self.person1.hEmail = 'sample@sample.com'
        self.person1.campus = 'SASKATOON'
        self.person1.jobType = 'FTO'
        self.person1.committee = 'Sample Commitee'
        self.person1.memberImage = 'image.img'
        self.person1.bDay = '2012-03-03'
        self.person1.hireDate = '2012-03-03'
        self.person1.gender = 'MALE'
        self.person1.membershipStatus = 'RESOURCE'
        self.person1.programChoice = 'Sample Program'
        self.person1.full_clean()
        self.person1.save()

        self.person2.memberID = 5205555
        self.person2.firstName = 'Alpha'
        self.person2.middleName = 'Middle'
        self.person2.lastName = 'Kincaid'
        self.person2.socNum = 123456789
        self.person2.city = 'Sample City'
        self.person2.mailAddress = 'Sample address'
        self.person2.mailAddress2 = 'Sample Address 2'
        self.person2.pCode = 's7k5j8'
        self.person2.hPhone = '(306)812-1234'
        self.person2.cPhone = '(306)812-1234'
        self.person2.hEmail = 'sample@sample.com'
        self.person2.campus = 'SASKATOON'
        self.person2.jobType = 'FTO'
        self.person2.committee = 'Sample Commitee'
        self.person2.memberImage = 'image.img'
        self.person2.bDay = '2012-03-03'
        self.person2.hireDate = '2012-03-03'
        self.person2.gender = 'MALE'
        self.person2.membershipStatus = 'RESOURCE'
        self.person2.programChoice = 'Sample Program'
        self.person2.full_clean()
        self.person2.save()

        self.person3.memberID = 6206666
        self.person3.firstName = 'Tim'
        self.person3.middleName = 'Middle'
        self.person3.lastName = 'Jones'
        self.person3.socNum = 123456789
        self.person3.city = 'Sample City'
        self.person3.mailAddress = 'Sample address'
        self.person3.mailAddress2 = 'Sample Address 2'
        self.person3.pCode = 's7k5j8'
        self.person3.hPhone = '(306)812-1234'
        self.person3.cPhone = '(306)812-1234'
        self.person3.hEmail = 'sample@sample.com'
        self.person3.campus = 'SASKATOON'
        self.person3.jobType = 'FTO'
        self.person3.committee = 'Sample Commitee'
        self.person3.memberImage = 'image.img'
        self.person3.bDay = '2012-03-03'
        self.person3.hireDate = '2012-03-03'
        self.person3.gender = 'MALE'
        self.person3.membershipStatus = 'RESOURCE'
        self.person3.programChoice = 'Sample Program'
        self.person3.full_clean()
        self.person3.save()

    # Test that Complainant (CN) is dynamically removed from the list of Additional
    #  Members for a Case, once selected by a User.
    # INPUT: Deborah Williams as Complainant. All other input valid; no additional members.
    # EXPECTED RESULT: Deborah Williams does not appear as an option in the list of available
    #   Additional Members.
    def test_remove_cn_from_add_members(self):
        """Complainant (CN) should be removed from the list of available
        members to add to a Case, once selected in the 'Complainant' box."""
        with self.assertTrue(self):
            # Create the Case
            temp_case = Case()

            # Start up the Client
            client = Client()

            # Add details for the Case
            temp_case.lead = 123456789
            temp_case.complainant = self.person1
            temp_case.campus = "Saskatoon"
            temp_case.school = "School of Business"
            temp_case.department = "Business Certificate"
            temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
            temp_case.status = "OPEN"
            temp_case.additionalNonMembers = ""
            temp_case.docs = None
            temp_case.logs = None
            temp_case.date = "2016-10-20"
            temp_case.full_clean()
            temp_case.save()

    def test_remove_cn_from_add_members_when_add_members_exist(self):
        """CN should be removed when selected in the CN box. Additional
        members should be able to be selected."""

    def test_cn_cannot_be_add_member(self):
        """Can't have CN be selectable in list, validator should grab this."""

    def test_warning_if_js_disabled(self):
        """Should check if JS is disabled in browser. If true show warning,
        else show nothing."""

    def test_cn_cannot_be_add_member_despite_meddling(self):
        """Even if a user meddles with the HTML in the browser, the page
        should validate itself and know that CN != additional member."""
