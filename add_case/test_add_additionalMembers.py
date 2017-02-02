from django.test import TestCase
from django.core.exceptions import ValidationError
from add_case.models import *
from add_member.models import Person


class TestAddMember(TestCase):
    temp_case = Case()
    person1 = Person()
    person2 = Person()
    boundary_person2 = Person()
    boundary_person1 = Person()
    program = CasePrograms()

    #   method :    setUP
    #   purpose:    create Person and Case objects for testing.
    def setUp(self):
        self.program.name = "Computer Systems Technology - Diploma"
        self.program.full_clean()
        self.program.save()

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
        self.temp_case.complainant = self.person1
        self.temp_case.campus = "Saskatoon"
        self.temp_case.school = "School of Business"
        self.temp_case.program = self.program
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

#
    def test_can_add_member(self):
        """Can add a Member to the Case"""
        self.temp_case.additionalMembers.add(self.person2)
        self.assertTrue(self.temp_case.additionalMembers.count() == 1)

    def test_can_add_many_members(self):
        """Can add multiple Members to the Case"""
        self.temp_case.additionalMembers.add(self.person2, self.person1)
        self.assertTrue(self.temp_case.additionalMembers.count() == 2)

    # won't work since person 1 is a complainant. They cannot also be an additional member.
    # def test_can_add_boundary_members(self):
    #     """Can add Members at the memberID boundary to the Case"""
    #     self.temp_case.additionalMembers.add(self.boundary_person1, self.boundary_person2)
    #     self.assertTrue(self.temp_case.additionalMembers.count() == 2)

    def test_cannot_add_outside_boundary_members(self):
        """Cannot add Members exceeding the memberID boundary to the Case"""
        boundary_person = Person()
        with self.assertRaises(ValidationError):
            boundary_person.memberID = 9999999999
            boundary_person.firstName = 'Sample'
            boundary_person.middleName = 'Person'
            boundary_person.lastName = 'Last'
            boundary_person.socNum = 123456789
            boundary_person.city = 'Sample City'
            boundary_person.mailAddress = 'Sample address'
            boundary_person.mailAddress2 = 'Sample Address 2'
            boundary_person.pCode = 's7k5j8'
            boundary_person.hPhone = '(306)812-1234'
            boundary_person.cPhone = '(306)812-1234'
            boundary_person.hEmail = 'sample@sample.com'
            boundary_person.campus = 'SASKATOON'
            boundary_person.jobType = 'FTO'
            boundary_person.committee = 'Sample Commitee'
            boundary_person.memberImage = 'image.img'
            boundary_person.bDay = '2012-03-03'
            boundary_person.hireDate = '2012-03-03'
            boundary_person.gender = 'MALE'
            boundary_person.membershipStatus = 'RESOURCE'
            boundary_person.programChoice = 'Sample Program'
            boundary_person.full_clean()
            boundary_person.save()
            self.temp_case.additionalMembers.add(boundary_person)

    def test_cannot_add_members_to_case_doesnt_exist(self):
        """Cannot add Members to a Case that doesn't exist"""
        # User wants a to add a member to a Case that has lead info of '3434'
        # Since a Case with 'sapmleleadinfo' lead doesnt exist, an error will be thrown
        with self.assertRaises(Case.DoesNotExist):
            # Case collection will be queried for Case with a lead info of '4343'
            add_person_to_this_case = Case.objects.get(complainant=None)
            add_person_to_this_case.additionalMembers.add(self.person1)

# cannot add a member that does not exist, to a case:
    def test_cannot_add_nonexistent_member_to_case(self):
        # User wants to add a Person with a name of Doris in the DB
        #   Since Doris isn't in the Person collection, an error will be thrown
        with self.assertRaises(Person.DoesNotExist):
            # Person collection will be queried for a person with the name 'Doris'
            person_to_add = Person.objects.get(firstName='Doris')
            self.temp_case.additionalMembers.add(person_to_add)

# cannot add a member to a case that does not exist:
    def test_cannot_add_member_to_nonexistent_case(self):
        with self.assertRaises(Case.DoesNotExist):
            ghost_case = Case.objects.get(complainant=None)
            person_to_add = self.person1
            ghost_case.additionalMembers.add(person_to_add)

    # some that can be used later
        # self.temp_case.additionalMembers.add(self.person2)
        # self.temp_case.additionalMembers.add(self.person2)
        # #person 2 is duplicate thus no need to add it again
        # self.assertTrue(self.temp_case.additionalMembers.count() == 1)
