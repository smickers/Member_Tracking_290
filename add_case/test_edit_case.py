from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import *
from django.db import DataError
import datetime
from add_member.models import Person

class CaseEditTest(TestCase):
    person1 = Person()
    person2 = Person()
    program = CasePrograms()
    tempCase = Case()
    program2 = CasePrograms()

    def setUp(self):
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

        self.person2.memberID = 7894561
        self.person2.firstName = 'The'
        self.person2.middleName = 'Second'
        self.person2.lastName = 'Person'
        self.person2.socNum = 987654321
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
        self.person2.gender = 'FEMALE'
        self.person2.membershipStatus = 'RESOURCE'
        self.person2.programChoice = 'Sample Program'
        self.person2.full_clean()
        self.person2.save()

        self.program.name = 'Business - Certificate'
        self.program.full_clean()
        self.program.save()

        self.program2.name = "CST"
        self.program2.full_clean()
        self.program2.save()

        self.tempCase.lead = 123456789
        self.tempCase.complainant = self.person1
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.program = self.program
        self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        self.tempCase.status = "OPEN"
        self.tempCase.additionalNonMembers = ""
        self.tempCase.docs = None
        self.tempCase.logs = None
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()
        self.tempCase.additionalMembers.add(self.person1)
        self.tempCase.save()

    def test_edit_lead(self):
        self.tempCase.lead = 4
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.lead == 4

    def test_edit_complainant(self):
        self.tempCase.complainant = self.person2
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.complainant == self.person2

    def test_edit_complainant_fail(self):
        with self.assertRaisesMessage(ValueError, 'Cannot assign "789456": "Case.complainant" must be a "Person" instance.'):
            self.tempCase.complainant = 789456
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_edit_campus(self):
        self.tempCase.campus = "Regina"
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.campus == "Regina"

    def test_edit_campus_fail(self):
        with self.assertRaisesMessage(ValidationError, '{\'campus\': [u"Value \'fdsafsad\' is not a valid choice."]}'):
            self.tempCase.campus = "fdsafsad"
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_edit_school(self):
        self.tempCase.school = "School of Information and Communications Technology"
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.school == "School of Information and Communications Technology"

    def test_edit_school_fail(self):
        with self.assertRaisesMessage(ValidationError, '{\'school\': [u"Value \'fdsafsad\' is not a valid choice."]}'):
            self.tempCase.school = "fdsafsad"
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_edit_program(self):
        self.tempCase.program = self.program2
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.program == self.program2

    def test_edit_program_fail(self):
        with self.assertRaisesMessage(ValueError, 'Cannot assign "\'This si a program\'": "Case.program" must be a "CasePrograms" instance.'):
            self.tempCase.program = "This si a program"
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_edit_case_type(self):
        self.tempCase.caseType = "ARBITRATION"
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.caseType == "ARBITRATION"

    def test_edit_case_type_fail(self):
        with self.assertRaisesMessage(ValidationError, '{\'caseType\': [u"Value \'UIOPUI\' is not a valid choice."]}'):
            self.tempCase.caseType = "UIOPUI"
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_edit_status(self):
        self.tempCase.status = "CLOSED"
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.status == "CLOSED"

    def test_edit_status_fail(self):
        with self.assertRaisesMessage(ValidationError, "{\'status\': [u\"Value \'tesatews\' is not a valid choice.\"]}"):
            self.tempCase.status = "tesatews"
            self.tempCase.full_clean()
            self.tempCase.save()

    def test_add_members(self):
        self.tempCase.additionalMembers.add(self.person2)
        self.tempCase.full_clean()
        self.tempCase.save()

    def test_remove_member(self):
        self.tempCase.additionalMembers.add(self.person2)
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.additionalMembers.get(pk=self.person2.pk) == self.person2

        self.tempCase.additionalMembers.remove(self.person2)
        self.tempCase.full_clean()
        self.tempCase.save()

        assert self.tempCase.additionalMembers.filter(pk=self.person2.pk).count() == 0

