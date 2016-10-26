from encodings.punycode import selective_find
from unittest import TestCase
from django.test import TestCase


from models import Case, Member, CaseMembers

class TestAddMember(TestCase):
    def setUp(self):
        Case.objects.create(caseID=111111111)
        Member.objects.create(memberID=000111111, firstName='Homer', lastName='Simpson')
        Member.objects.create(memberID=000222222, firstName='Marge', lastName='Simpson')
        Member.objects.create(memberID=000000001, firstName="Larry", lastName="LowBoundary")
        Member.objects.create(memberID=999999999, firstName="Hilary", lastName="HighBoundary")
        Member.objects.create(memberID=123, firstName="Tony", lastName="TooLow")
        Member.objects.create(memberID=1234567891, firstName="Henry", lastName="HighBoundary")


    def test_can_add_member(self):
        """Can add a Member to the Case"""
        homsim = Member.objects.get(memberID=000111111)
        case1 = Case.objects.get(caseID=111111111)

        case = CaseMembers(caseNum=case1, memberNum=homsim)
        self.assertEquals(case.memberNum.memberID, homsim.memberID)




    def test_can_add_many_members(self):
        """Can add multiple Members to the Case"""
        homsim = Member.objects.get(memberID=000111111)
        marsim = Member.objects.get(memberID=000222222)
        case1 = Case.objects.get(caseID=111111111)
        CaseMember1 = CaseMembers(caseNum=case1, memberNum=homsim)
        CaseMember2 = CaseMembers(caseNum=case1, memberNum=marsim)

        self.assertEquals(CaseMember1.memberNum.memberID, homsim.memberID)
        self.assertEquals(CaseMember2.memberNum.memberID, marsim.memberID)


    def test_can_add_boundary_members(self):
        """Can add Members at the memberID boundary to the Case"""
        larlow = Member.objects.get(memberID=000000001)
        hilhig = Member.objects.get(memberID=999999999)
        case1 = Case.objects.get(caseID=111111111)
        CaseMember1 = CaseMembers(caseNum=case1, memberNum=larlow)
        CaseMember2 = CaseMembers(caseNum=case1, memberNum=hilhig)

        self.assertEquals(CaseMember1.memberNum.memberID, larlow.memberID)
        self.assertEquals(CaseMember2.memberNum.memberID, hilhig.memberID)

    def test_cannot_add_outside_boundary_members(self):
        """Cannot add Members exceeding the memberID boundary to the Case"""
        with self.assertRaises(Exception):
            toolow = Member.objects.get(memberID=123)
            toohig = Member.objects.get(memberID=12345678910)


    def test_cannot_add_members_to_case_doesnt_exist(self):
        """Cannot add Members to a Case that doesn't exist"""

        homsim = Member.objects.get(memberID=000111111)
        marsim = Member.objects.get(memberID=000222222)
        with self.assertRaises(Exception):
            Case.objects.get(caseID=222222222)

        #self.assertFalse(self.assertContains(CaseMember1.caseNum, homsim.memberID))
        #self.assertEquals(CaseMember2.memberNum.memberID, marsim.memberID)


    def test_cannot_add_nonexistent_member_to_case(self):
        case1 = Case.objects.get(caseID=111111111)
        with self.assertRaises(Exception):
            barsim = Member.objects.get(memberID=000333333)



    def test_cannot_add_nonexistent_member_with_group_to_case(self):
        case1 = Case.objects.get(caseID=111111111)
        with self.assertRaises(Exception):
            barsim = Member.objects.get(memberID=000333333)
            homsim = Member.objects.get(memberID=000111111)

