from django.test import TestCase
from grievance_award_creation.models import GrievanceAward
from add_member.models import Person
from add_case.models import Case, CasePrograms

class CaseLinksToGrievanceAwards(TestCase):
    """
    Purpose: Test the connection between grievance award its case
    """

    def __init__(self, *args, **kwargs):
        super(CaseLinksToGrievanceAwards, self).__init__(*args, **kwargs)
        self.person1 = Person()
        self.person2 = Person()
        self.tempCase = Case()
        self.tempCase2 = Case()
        self.ga2 = GrievanceAward()
        self.ga = GrievanceAward()



    def setUp(self):
        """
        Setup method to initialize essential Objects
        :return: None
        """
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

        self.person2.memberID = 4204441
        self.person2.firstName = 'First2'
        self.person2.middleName = 'Middle2'
        self.person2.lastName = 'Last2'
        self.person2.socNum = 123456788
        self.person2.city = 'Sample City'
        self.person2.mailAddress = 'Sample address'
        self.person2.mailAddress2 = 'Sample Address 2'
        self.person2.pCode = 'S7K5J8'
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

        self.tempCase.lead = 123456789
        self.tempCase.complainant = self.person1
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.program = CasePrograms(name="Computer Systems Technology").save()
        self.tempCase.caseType = 7
        self.tempCase.status = "OPEN"
        self.tempCase.additionalNonMembers = ""
        self.tempCase.docs = None
        self.tempCase.logs = None
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()
        self.tempCase.additionalMembers.add(self.person1)
        self.tempCase.save()


        self.tempCase2.lead = 123456789
        self.tempCase2.complainant = self.person1
        self.tempCase2.campus = "Saskatoon"
        self.tempCase2.school = "School of Business"
        self.tempCase2.program = CasePrograms(name="Computer Systems Technology").save()
        self.tempCase2.caseType = 3
        self.tempCase2.status = "OPEN"
        self.tempCase2.additionalNonMembers = ""
        self.tempCase2.docs = None
        self.tempCase2.logs = None
        self.tempCase2.date = "2016-10-20"
        self.tempCase2.full_clean()
        self.tempCase2.save()
        self.tempCase2.additionalMembers.add(self.person1)
        self.tempCase2.save()

        self.ga.case = self.tempCase
        self.ga.awardAmount = 500.00
        self.ga.description = ""
        self.ga.date = '2016-12-01'
        self.ga.full_clean()
        self.ga.save()

        self.ga2.case = self.tempCase2
        self.ga2.awardAmount = 500.00
        self.ga2.description = ""
        self.ga2.date = '2016-12-01'
        self.ga2.full_clean()
        self.ga2.save()



    def test_grievance_award_can_be_associated_with_a_single_member_if_grievance_award_type_is_of_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        :return:
        """
        self.assertTrue(self.ga.recipient.all().count() == 1)




    # def test_grievance__award_cannot_be_associated_with_multiple_member_if_grievance_award_type_is_member(self):
    #     """
    #     Purpose: test to see if grievance award can only be associated with a single member if it is of type
    #     member
    #     :return:
    #     """
    #     pass
    # def test_grievance_award_can_be_associated_with_multiple_member_if_grievance_award_type_is_of_policy(self):
    #     """
    #     Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
    #     policy
    #     :return:
    #     """
    #     # if (self.ga.case is not None and self.ga.caseType='P'):
    #     #     self.assertEquals(list(self.ga.recipient), list(self.case.additionalMembers) + self.case.complainant)
    #     pass
    #
    # def test_grievance_award_cannot_be_associated_with_multiple_members_if_griev_aw_type_isnt_of_policy(self):
    #     """
    #     Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
    #     policy
    #     :return:
    #     """
    #     # if(self.ga.case is not None and self.ga.caseType='M'):
    #     #     self.assertTrue(self.ga.recipient.all().count == 1)
    #
    #     pass