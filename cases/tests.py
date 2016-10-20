from unittest import TestCase
#from django.test import TestCase
from models import Case, Member


class TestAddMember(TestCase):
    def setUp(self):
        Case.objects.create(caseID=111111111)
        Member.objects.create(memberID=000111111, firstName='Homer', lastName='Simpson')
        Member.objects.create(memberID=000222222, firstName='Marge', lastName='Simpson')
        Member.objects.create(memberID=000000001, firstName="Larry", lastName="LowBoundary")
        Member.objects.create(memberID=999999999, firstName="Hilary", lastName="HighBoundary")
        Member.objects.create(memberID=123, firstName="Tony", lastName="TooLow")
        Member.objects.create(memberID=12345678910, firstName="Henry", lastName="HighBoundary")
        Case.objects.save()
        Member.objects.save()

    def test_can_add_member(self):
        """Can add a Member to the Case"""
        self.setUp()
        homsim = Member.objects.get(memberID=000111111)
        case1 = Case.objects.get(caseID=111111111)
        self.assertContains(case1.members.addmember(homsim.memberID))
        self.tearDown()

    def test_can_add_many_members(self):
        """Can add multiple Members to the Case"""
        self.setUp()
        homsim = Member.objects.get(memberID=000111111)
        marsim = Member.objects.get(memberID=000222222)
        case1 = Case.objects.get(caseID=111111111)
        self.assertContains(case1.members.addmember(homsim.memberID, marsim.memberID))
        self.tearDown()

    def test_can_add_boundary_members(self):
        """Can add Members at the memberID boundary to the Case"""
        self.setUp()
        larlow = Member.objects.get(memberID=000000001)
        hilhig = Member.objects.get(memberID=999999999)
        case1 = Case.objects.get(caseID=111111111)
        self.assertContains(case1.members.addmember(larlow.memberID, hilhig.memberID))
        self.tearDown()

    def test_cannot_add_outside_boundary_members(self):
        """Cannot add Members exceeding the memberID boundary to the Case"""
        self.setUp()
        toolow = Member.objects.get(memberID=123)
        toohig = Member.objects.get(memberID=12345678910)
        case1 = Case.objects.get(caseID=111111111)
        self.assertFalse(self.assertContains(
            case1.members.addmember(toolow.memberID, toohig.memberID)))
        self.tearDown()

    def test_cannot_add_members_to_case_doesnt_exist(self):
        """Cannot add Members to a Case that doesn't exist"""
        self.setUp()
        case2 = Case.objects.get(caseID=22222222)
        homsim = Member.objects.get(memberID=000111111)
        marsim = Member.objects.get(memberID=000222222)
        self.assertFalse(self.assertContains(
            case2.members.addmember(homsim.memberID, marsim.memberID)
        ))
        self.tearDown()

    def test_cannot_add_nonexistent_member_to_case(self):
        self.setUp()
        case1 = Case.objects.get(caseID=111111111)
        barsim = Member.objects.get(memberID=000333333)
        self.assertFalse(self.assertContains(
            case1.members.addmember(barsim.memberID)
        ))
        self.tearDown()

    def test_cannot_add_nonexistent_member_with_group_to_case(self):
        self.setUp()
        case1 = Case.objects.get(caseID=111111111)
        barsim = Member.objects.get(memberID=000333333)
        homsim = Member.objects.get(memberID=000111111)
        self.assertFalse(self.assertContains(
            case1.members.addmember(barsim.memberID, homsim.memberID)
        ))
        self.tearDown()
