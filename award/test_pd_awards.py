from django.test import TestCase
from add_member.models import Person
from django.core.exceptions import ValidationError
from models import PDAward, Person
from forms import PDAwardForm

#Class: TestPDAward
#This class is for testing PD Awards
class TestPDAward(TestCase):
    tempPerson = Person()
    form = PDAwardForm()

    def setUp(self):
        # Set up a Member for testing
        self.tempPerson.memberID = 1
        self.tempPerson.firstName = 'First'
        self.tempPerson.middleName = 'Middle'
        self.tempPerson.lastName = 'Last'
        self.tempPerson.socNum = 123456789
        self.tempPerson.city = 'Sample City'
        self.tempPerson.mailAddress = 'Sample address'
        self.tempPerson.mailAddress2 = 'Sample Address 2'
        self.tempPerson.pCode = 's7k5j8'
        self.tempPerson.hPhone = '(306)812-1234'
        self.tempPerson.cPhone = '(306)812-1234'
        self.tempPerson.hEmail = 'sample@sample.com'
        self.tempPerson.campus = 'SASKATOON'
        self.tempPerson.jobType = 'FTO'
        self.tempPerson.committee = 'Sample Commitee'
        self.tempPerson.memberImage = 'image.img'
        self.tempPerson.bDay = '2012-03-03'
        self.tempPerson.hireDate = '2012-03-03'
        self.tempPerson.gender = 'MALE'
        self.tempPerson.membershipStatus = 'RESOURCE'
        self.tempPerson.programChoice = 'Sample Program'
        self.tempPerson.full_clean()
        self.tempPerson.save()

    # test_valid_pd_creation
    # Test that a PD Award is created when all fields are valid
    def test_valid_pd_creation(self):
        self.pdAward1 = PDAward()
        self.pdAward1.awardName= "Excelence Award"
        self.pdAward1.memberAwarded = self.tempPerson
        self.pdAward1.awardCost = 100
        self.pdAward1.startDate = "2017-02-01"
        self.pdAward1.endDate = "2017-02-01"
        self.pdAward1.full_clean()
        self.pdAward1.save()

    # test_invalid_award_name
    # Test that a PD Award is not created when an invalid name is given
    def test_invalid_award_name(self):
        with self.assertRaisesMessage(ValidationError, "Ensure this value has at most 50 characters (it has 51)"):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = 'a' * 51
            self.pdAward1.memberAwarded = self.tempPerson
            self.pdAward1.awardCost = 100
            self.pdAward1.startDate = "2017-02-01"
            self.pdAward1.endDate = "2017-02-01"
            self.pdAward1.full_clean()
            self.pdAward1.save()

    # test_invalid_member
    # Test that a PD award is not created when an invalid member is given
    def test_invalid_member(self):
        with self.assertRaisesMessage(ValueError, 'Cannot assign "\'Hello\'": "PDAward.memberAwarded" must be a "Person" instance.'):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = "Excellence Award"
            self.pdAward1.memberAwarded = "Hello"
            self.pdAward1.awardCost = 100
            self.pdAward1.startDate = "2017-02-01"
            self.pdAward1.endDate = "2017-02-01"
            self.pdAward1.full_clean()
            self.pdAward1.save()

    # test_invali_cost
    # Test that a PD award is not created when an invalid cost is given
    def test_invalid_cost(self):
        with self.assertRaisesMessage(ValidationError, "Amount must be greater than $0 and less than $1,000,000."):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = "Excelence Award"
            self.pdAward1.memberAwarded = self.tempPerson
            self.pdAward1.awardCost = 1000000
            self.pdAward1.startDate = "2017-02-01"
            self.pdAward1.endDate = "2017-02-01"
            self.pdAward1.full_clean()
            self.pdAward1.save()

    # test_invalid_start_date
    # Test that a PD award is not created when an invalid start date is given
    def test_invalid_start_date(self):
        with self.assertRaisesMessage(ValidationError, "\'2017-02-31\' value has the correct format (YYYY-MM-DD) but it is an invalid date."):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = "Excelence Award"
            self.pdAward1.memberAwarded = self.tempPerson
            self.pdAward1.awardCost = 100
            self.pdAward1.startDate = "2017-02-31"
            self.pdAward1.endDate = "2017-03-01"
            self.pdAward1.full_clean()
            self.pdAward1.save()

    # test_invalid_end_date
    # Test that a PD award is not created when an invalid end date is given
    def test_invalid_end_date(self):
        with self.assertRaisesMessage(ValidationError, "\'2017-02-31\' value has the correct format (YYYY-MM-DD) but it is an invalid date."):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = "Excelence Award"
            self.pdAward1.memberAwarded = self.tempPerson
            self.pdAward1.awardCost = 100
            self.pdAward1.startDate = "2017-02-01"
            self.pdAward1.endDate = "2017-02-31"
            self.pdAward1.full_clean()
            self.pdAward1.save()

    # test_that_start_date_comes_before_end_date
    # Test that a PD award is not created when end date coems before start date
    def test_that_start_date_comes_before_end_date(self):
        with self.assertRaisesMessage(ValidationError,"End Date must be the same as or come after start date"):
            self.pdAward1 = PDAward()
            self.pdAward1.awardName = "Excellence Award"
            self.pdAward1.memberAwarded = self.tempPerson
            self.pdAward1.awardCost = 100
            self.pdAward1.startDate = "2017-02-02"
            self.pdAward1.endDate = "2016-01-01"
            self.pdAward1.full_clean()
            self.pdAward1.save()
