from django.test import TestCase
from django.core.exceptions import ValidationError
from add_case.models import Case
from add_member.models import Person
from django.test import Client


class CaseTestsPrimComplaintant(TestCase):
    person1 = Person()


    def setUp(self):
        self.person1.memberID = 4204444
        self.person1.firstName = 'First'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Last'
        self.person1.socNum = 123456789
        self.person1.city = 'Sample City'
        self.person1.mailAddress = 'Sample address'
        self.person1.mailAddress2 = 'Sample Address 2'
        self.person1.pCode = 'S7K5J8'
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


    #Tests for a invalid primary complaintant. We will use "Not Exist" for both
    #   first and last name, which are not associated with a created test person
    def testInValidPrimaryComplaintant(self):
        # raises an error that the person does not exist
        with self.assertRaises(Person.DoesNotExist):
            tempCase = Case()
            # Assigning the complainant to a non existent member
            tempCase.complainant = Person.objects.get(firstName='Nonexistent member')
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Tests for a valid primary complaintant using "First" and "Last" as first and last names respectively.
    #   There should be a person existing with this first and last name

    def testValidPrimaryComplaintant(self):
        tempCase = Case()
        tempCase.complainant = self.person1
        tempCase.lead = 1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Tests for a blank primary complaintant. Complainant is a required field. Should fail
    def testBlankPrimaryComplaintant(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.complainant = None
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()
