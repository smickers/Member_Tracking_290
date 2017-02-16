from django.test import TestCase
from models import Person, EducationAward
from models import EducationAward
from django.core.exceptions import ValidationError
from django.test import TestCase
from add_member.models import Person
from django.core.exceptions import ValidationError
from models import PDAward, Person
from forms import PDAwardForm

class MonetaryFormatTest(TestCase):

    tempPerson = Person()
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

    def test_new_valid_monetary_format_on_an_edu_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1250.00
        ea.full_clean()
        ea.save()

    def test_new_lower_bound_for_an_edu_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 0.01
        ea.full_clean()
        ea.save()

    def test_new_upper_bound_for_an_edu_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 999999.99
        ea.full_clean()
        ea.save()

    def test_new_upper_out_of_scope_for_edu_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 1000000.00
        ea.full_clean()
        ea.save()

    def test_new_lower_out_of_scope_for_edu_award(self):
        ea = EducationAward()
        ea.description = "SPFA Education Award - Fall 2015"
        ea.awardAmount = 0.00
        ea.full_clean()
        ea.save()

    def test_new_valid_monetary_format_for_a_pd_funding(self):
        pdAward1 = PDAward()
        pdAward1.awardName= "Excelence Award"
        pdAward1.memberAwarded = self.tempPerson
        pdAward1.awardCost = 100.00
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()

    def test_new_lower_bound_for_a_pd_funding(self):
        pdAward1 = PDAward()
        pdAward1.awardName = "Excelence Award"
        pdAward1.memberAwarded = self.tempPerson
        pdAward1.awardCost = 0.01
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()

    def test_new_upper_bound_for_a_pd_funding(self):
        pdAward1 = PDAward()
        pdAward1.awardName = "Excelence Award"
        pdAward1.memberAwarded = self.tempPerson
        pdAward1.awardCost = 999999.99
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()

    def test_new_upper_out_of_scope_for_a_pd_funding(self):
        pdAward1 = PDAward()
        pdAward1.awardName = "Excelence Award"
        pdAward1.memberAwarded = self.tempPerson
        pdAward1.awardCost = 1000000.00
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()

    def test_new_lower_out_of_scope_for_a_pd_funding(self):
        pdAward1 = PDAward()
        pdAward1.awardName = "Excelence Award"
        pdAward1.memberAwarded = self.tempPerson
        pdAward1.awardCost = 0.00
        pdAward1.startDate = "2017-02-01"
        pdAward1.endDate = "2017-02-01"
        pdAward1.full_clean()
        pdAward1.save()