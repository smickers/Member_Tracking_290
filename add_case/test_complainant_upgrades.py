from django.test import TestCase
from django.core.exceptions import ValidationError
from add_case.models import Case, CasePrograms
from add_member.models import Person


# Test cases for S25: Ensure CN is removed from list of additional members, when adding a Case
class CaseTests(TestCase):
    person1 = Person()
    person2 = Person()
    person3 = Person()
    person4 = Person()
    temp_case = Case()
    prog = CasePrograms()

    # Create our People
    def setUp(self):
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

        self.person4.memberID = 7207777
        self.person4.firstName = 'Deborah'
        self.person4.middleName = 'Middle'
        self.person4.lastName = 'Williams'
        self.person4.socNum = 123456789
        self.person4.city = 'Sample City'
        self.person4.mailAddress = 'Sample address'
        self.person4.mailAddress2 = 'Sample Address 2'
        self.person4.pCode = 's7k5j8'
        self.person4.hPhone = '(306)812-1234'
        self.person4.cPhone = '(306)812-1234'
        self.person4.hEmail = 'sample@sample.com'
        self.person4.campus = 'SASKATOON'
        self.person4.jobType = 'FTO'
        self.person4.committee = 'Sample Commitee'
        self.person4.memberImage = 'image.img'
        self.person4.bDay = '2012-03-03'
        self.person4.hireDate = '2012-03-03'
        self.person4.gender = 'MALE'
        self.person4.membershipStatus = 'RESOURCE'
        self.person4.programChoice = 'Sample Program'
        self.person4.full_clean()
        self.person4.save()

        self.prog.name = "Computer Systems Technology - Diploma"
        self.prog.full_clean()
        self.prog.save()

    # Test that we can save a complainant to a case, and don't need additional members.
    def test_case_saved_with_cn_and_no_add_members_exist(self):
        """A CN is specified, with no additional members. Case is saved to DB."""
        temp_case = Case()
        temp_case.lead = 123456789
        temp_case.complainant = self.person1
        temp_case.campus = "Saskatoon"
        temp_case.school = "School of Business"
        temp_case.program = self.prog
        temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        temp_case.status = "OPEN"
        temp_case.docs = None
        temp_case.logs = None
        temp_case.date = "2016-10-20"
        temp_case.full_clean()
        temp_case.save()
        self.assertTrue(True)

    # Test that we can save a complainant AND additional members to a case.
    def test_case_saves_with_cn_and_add_members_exist(self):
        """A CN is specified, as are additional members. Case is saved
        to DB."""
        temp_case = Case()
        temp_case.lead = 123456789
        temp_case.complainant = self.person1
        temp_case.campus = "Saskatoon"
        temp_case.school = "School of Business"
        temp_case.program = self.prog
        temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        temp_case.status = "OPEN"
        temp_case.docs = None
        temp_case.logs = None
        temp_case.date = "2016-10-20"
        temp_case.full_clean()
        temp_case.save()
        temp_case.additionalMembers.add(self.person2, self.person3)
        # temp_case.save()
        self.assertTrue(True)

    # Test that the complianant cannot also be added to a case as an additional member.
    def test_cn_cannot_be_add_member(self):
        """Can't have CN be selectable in list, validator should grab this."""
        with self.assertRaisesRegexp(ValidationError, "Complainant cannot be added as an additional member."):
       #with self.assertRaisesRegexp(ValidationError, "Complainant cannot be added as an additional member."):
            temp_case = Case()
            temp_case.lead = 123456789
            temp_case.complainant = self.person1
            temp_case.campus = "Saskatoon"
            temp_case.school = "School of Business"
            temp_case.program = self.prog
            temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
            temp_case.status = "OPEN"
            temp_case.docs = None
            temp_case.logs = None
            temp_case.date = "2016-10-20"
            temp_case.full_clean()
            temp_case.save()
            temp_case.additionalMembers.add(self.person1)
            #temp_case.clean_additional_members()
            temp_case.save()


    # Test that a complainant and additional member that have the same name, can both
    #   be added to the case (as they will have different IDs in the system).
    def test_cn_and_add_member_same_name_diff_person(self):
        """CN and additional member are both named Deborah Williams, but have
        different memberIDs and IDs in the database. System should save person1 as CN
        and person4 as additional member."""
        temp_case = Case()
        temp_case.lead = 123456789
        temp_case.complainant = self.person1
        temp_case.campus = "Saskatoon"
        temp_case.school = "School of Business"
        temp_case.program = self.prog
        temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        temp_case.status = "OPEN"
        temp_case.docs = None
        temp_case.logs = None
        temp_case.date = "2016-10-20"
        temp_case.full_clean()
        temp_case.save()
        temp_case.additionalMembers.add(self.person4)
        temp_case.save()
        self.assertTrue(True)
