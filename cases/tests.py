# from encodings.punycode import selective_find
# from unittest import TestCase
# from django.test import TestCase
#
#
# from models import Case, Member, CaseMembers
#
# class TestAddMember(TestCase):
#     def setUp(self):
#         Case.objects.create(caseID=111111111)
#         Member.objects.create(memberID=000111111, firstName='Homer', lastName='Simpson')
#         Member.objects.create(memberID=000222222, firstName='Marge', lastName='Simpson')
#         Member.objects.create(memberID=000000001, firstName="Larry", lastName="LowBoundary")
#         Member.objects.create(memberID=999999999, firstName="Hilary", lastName="HighBoundary")
#         Member.objects.create(memberID=123, firstName="Tony", lastName="TooLow")
#         Member.objects.create(memberID=1234567891, firstName="Henry", lastName="HighBoundary")
#
#
#     def test_can_add_member(self):
#         """Can add a Member to the Case"""
#         homsim = Member.objects.get(memberID=000111111)
#         case1 = Case.objects.get(caseID=111111111)
#
#         case = CaseMembers(caseNum=case1, memberNum=homsim)
#         self.assertEquals(case.memberNum.memberID, homsim.memberID)
#
#
#
#
#     def test_can_add_many_members(self):
#         """Can add multiple Members to the Case"""
#         homsim = Member.objects.get(memberID=000111111)
#         marsim = Member.objects.get(memberID=000222222)
#         case1 = Case.objects.get(caseID=111111111)
#         CaseMember1 = CaseMembers(caseNum=case1, memberNum=homsim)
#         CaseMember2 = CaseMembers(caseNum=case1, memberNum=marsim)
#
#         self.assertEquals(CaseMember1.memberNum.memberID, homsim.memberID)
#         self.assertEquals(CaseMember2.memberNum.memberID, marsim.memberID)
#
#
#     def test_can_add_boundary_members(self):
#         """Can add Members at the memberID boundary to the Case"""
#         larlow = Member.objects.get(memberID=000000001)
#         hilhig = Member.objects.get(memberID=999999999)
#         case1 = Case.objects.get(caseID=111111111)
#         CaseMember1 = CaseMembers(caseNum=case1, memberNum=larlow)
#         CaseMember2 = CaseMembers(caseNum=case1, memberNum=hilhig)
#
#         self.assertEquals(CaseMember1.memberNum.memberID, larlow.memberID)
#         self.assertEquals(CaseMember2.memberNum.memberID, hilhig.memberID)
#
#     def test_cannot_add_outside_boundary_members(self):
#         """Cannot add Members exceeding the memberID boundary to the Case"""
#         with self.assertRaises(Exception):
#             toolow = Member.objects.get(memberID=123)
#             toohig = Member.objects.get(memberID=12345678910)
#
#
#     def test_cannot_add_members_to_case_doesnt_exist(self):
#         """Cannot add Members to a Case that doesn't exist"""
#
#         homsim = Member.objects.get(memberID=000111111)
#         marsim = Member.objects.get(memberID=000222222)
#         with self.assertRaises(Exception):
#             Case.objects.get(caseID=222222222)
#
#         #self.assertFalse(self.assertContains(CaseMember1.caseNum, homsim.memberID))
#         #self.assertEquals(CaseMember2.memberNum.memberID, marsim.memberID)
#
#
#     def test_cannot_add_nonexistent_member_to_case(self):
#         case1 = Case.objects.get(caseID=111111111)
#         with self.assertRaises(Exception):
#             barsim = Member.objects.get(memberID=000333333)
#
#
#
#     def test_cannot_add_nonexistent_member_with_group_to_case(self):
#         case1 = Case.objects.get(caseID=111111111)
#         with self.assertRaises(Exception):
#             barsim = Member.objects.get(memberID=000333333)
#             homsim = Member.objects.get(memberID=000111111)
#
# -- old test-



from encodings.punycode import selective_find
from unittest import TestCase
from django.test import TestCase
from add_member.models import Person


from add_case.models import Case
from add_member.models import Person

class TestAddMember(TestCase):
    temp_case = Case()
    person1 = Person()
    person2 = Person()
    boundary_person2 = Person()
    boundary_person1 = Person()

    def setUp(self):
        self.person1 = Person()
        self.person1.memberID = 4204444
        self.person1.firstName = 'First'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Last'
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

        self.person2 = Person()
        self.person2.memberID = 434313
        self.person2.firstName = 'Sample'
        self.person2.middleName = 'Person'
        self.person2.lastName = 'Last'
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

        self.temp_case.lead = 123456789
        self.temp_case.complainant = 987654321
        self.temp_case.campus = "Saskatoon"
        self.temp_case.school = "School of Business"
        self.temp_case.department = "Business Certificate"
        self.temp_case.caseType = "GRIEVANCES - CLASSIFICATION"
        self.temp_case.status = "OPEN"
        self.temp_case.additionalNonMembers = ""
        self.temp_case.docs = None
        self.temp_case.logs = None
        self.temp_case.date = "2016-10-20"
        self.temp_case.full_clean()
        self.temp_case.save()


        self.boundary_person1.memberID = 000000001
        self.boundary_person1.firstName = 'Sample'
        self.boundary_person1.middleName = 'Person'
        self.boundary_person1.lastName = 'Last'
        self.boundary_person1.socNum = 123456789
        self.boundary_person1.city = 'Sample City'
        self.boundary_person1.mailAddress = 'Sample address'
        self.boundary_person1.mailAddress2 = 'Sample Address 2'
        self.boundary_person1.pCode = 's7k5j8'
        self.boundary_person1.hPhone = '(306)812-1234'
        self.boundary_person1.cPhone = '(306)812-1234'
        self.boundary_person1.hEmail = 'sample@sample.com'
        self.boundary_person1.campus = 'SASKATOON'
        self.boundary_person1.jobType = 'FTO'
        self.boundary_person1.committee = 'Sample Commitee'
        self.boundary_person1.memberImage = 'image.img'
        self.boundary_person1.bDay = '2012-03-03'
        self.boundary_person1.hireDate = '2012-03-03'
        self.boundary_person1.gender = 'MALE'
        self.boundary_person1.membershipStatus = 'RESOURCE'
        self.boundary_person1.programChoice = 'Sample Program'
        self.boundary_person1.full_clean()
        self.boundary_person1.save()

        self.boundary_person2.memberID = 999999999
        self.boundary_person2.firstName = 'Sample'
        self.boundary_person2.middleName = 'Person'
        self.boundary_person2.lastName = 'Last'
        self.boundary_person2.socNum = 123456789
        self.boundary_person2.city = 'Sample City'
        self.boundary_person2.mailAddress = 'Sample address'
        self.boundary_person2.mailAddress2 = 'Sample Address 2'
        self.boundary_person2.pCode = 's7k5j8'
        self.boundary_person2.hPhone = '(306)812-1234'
        self.boundary_person2.cPhone = '(306)812-1234'
        self.boundary_person2.hEmail = 'sample@sample.com'
        self.boundary_person2.campus = 'SASKATOON'
        self.boundary_person2.jobType = 'FTO'
        self.boundary_person2.committee = 'Sample Commitee'
        self.boundary_person2.memberImage = 'image.img'
        self.boundary_person2.bDay = '2012-03-03'
        self.boundary_person2.hireDate = '2012-03-03'
        self.boundary_person2.gender = 'MALE'
        self.boundary_person2.membershipStatus = 'RESOURCE'
        self.boundary_person2.programChoice = 'Sample Program'
        self.boundary_person2.full_clean()
        self.boundary_person2.save()

    def test_can_add_member(self):
        """Can add a Member to the Case"""
        self.temp_case.additionalMembers.add(self.person2)
        self.assertTrue(self.temp_case.additionalMembers.count() == 1)

    def test_can_add_many_members(self):
        """Can add multiple Members to the Case"""
        self.temp_case.additionalMembers.add(self.person2, self.person1)
        self.assertTrue(self.temp_case.additionalMembers.count() == 2)

    def test_can_add_boundary_members(self):
        """Can add Members at the memberID boundary to the Case"""

        self.temp_case.additionalMembers.add(self.boundary_person1, self.boundary_person2)
        self.assertTrue(self.temp_case.additionalMembers.count() == 2)
    #
    #
    # def test_cannot_add_outside_boundary_members(self):
    #     """Cannot add Members exceeding the memberID boundary to the Case"""
    #

    def test_cannot_add_members_to_case_doesnt_exist(self):
        """Cannot add Members to a Case that doesn't exist"""
        # User wants a to add a member to a Case that has lead info of '3434'
        # Since a Case with 'sapmleleadinfo' lead doesnt exist, an error will be thrown
        with self.assertRaises(Case.DoesNotExist):
            # Case collection will be queried for Case with a lead info of '4343'
            add_person_to_this_case = Case.objects.get(lead=4343)
            add_person_to_this_case.additionalMembers.add(self.person1)

    def test_cannot_add_nonexistent_member_to_case(self):
        # User wants to add a Person with a name of Doris in the DB
        #   Since Doris isn't in the Person collection, an error will be thrown
        with self.assertRaises(Person.DoesNotExist):
            # Person collection will be queried for a person with the name 'Doris'
            person_to_add = Person.objects.get(firstName='Doris')
            self.temp_case.additionalMembers.add(person_to_add)

    # def test_cannot_add_nonexistent_member_with_group_to_case(self):

    # some that can be used later
        # self.temp_case.additionalMembers.add(self.person2)
        # self.temp_case.additionalMembers.add(self.person2)
        # #person 2 is duplicate thus no need to add it again
        # self.assertTrue(self.temp_case.additionalMembers.count() == 1)