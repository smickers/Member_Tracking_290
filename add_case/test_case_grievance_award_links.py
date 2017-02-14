from django.test import TestCase
from grievance_award_creation.models import GrievanceAward


class CaseLinksToGrievanceAwards(TestCase):
    """
    Purpose: Test the connection between grievance award its case
    """

    def setUp(self):
        """
        Setup method to initialize essential Objects
        :return: None
        """
        """
        TODO: modify Case to have its case type to be an Integer. This enables us to use conditional statements
        based on the case type's numerical value.
        For example:
            GRIEVANCE AWARD case types should be mapped to value greater than 3
            and other case types less than 3
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
        self.person2.firstName = 'Firstt'
        self.person2.middleName = 'Middlee'
        self.person2.lastName = 'Lastt'
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

        # self.tempCase.lead = 123456789
        # self.tempCase.complainant = self.person1
        # self.tempCase.campus = "Saskatoon"
        # self.tempCase.school = "School of Business"
        # self.tempCase.program = self.program
        # self.tempCase.caseType = "GRIEVANCES - CLASSIFICATION"  --change to int
        # self.tempCase.status = "OPEN"
        # self.tempCase.additionalNonMembers = ""
        # self.tempCase.docs = None
        # self.tempCase.logs = None
        # self.tempCase.date = "2016-10-20"
        # self.tempCase.full_clean()
        # self.tempCase.save()
        # self.tempCase.additionalMembers.add(self.person1)
        # self.tempCase.save()

        # self.ga.grievanceType = "M"
        # self.ga.recipient = self.tempPerson
        # self.ga.case = self.tempCase
        # self.ga.awardAmount = 500.00
        # self.ga.description = ""
        # self.ga.date = '2016-12-01'
        # self.ga.full_clean()
        # self.ga.save()


    def test_grievance_award_can_be_associated_with_a_single_member_if_grievance_award_type_is_of_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        :return:
        """
        # if(self.ga.case is not None and self.ga.caseType='M'):
        #     self.assertTrue(self.ga.recipient.get(Person=self.person1) == self.tempCase.complainant)
        pass

    def test_grievance__award_cannot_be_associated_with_a_single_member_if_grievance_award_type_is_not_of_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        :return:
        """
        # if (self.ga.case is not None and self.ga.caseType='M'):
        #     self.assertFalse(self.ga.recipient.get(Person=self.person1) == self.tempCase.complainant)
        pass

    def test_grievance_award_can_be_associated_with_multiple_member_if_grievance_award_type_is_of_policy(self):
        """
        Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
        policy
        :return:
        """
        # if (self.ga.case is not None and self.ga.caseType='P'):
        #     self.assertEquals(list(self.ga.recipient), list(self.case.additionalMembers) + self.case.complainant)
        pass

    def test_grievance_award_cannot_be_associated_with_multiple_members_if_griev_aw_type_isnt_of_policy(self):
        """
        Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
        policy
        :return:
        """
        # if(self.ga.case is not None and self.ga.caseType='M'):
        #     self.assertTrue(self.ga.recipient.all().count == 1)

        pass

    def test_case_eval_cases_types_returns_the_instance_of_the_case_type_it_is_related_to(self):
        """
        Purpose: test to see that case eval type is a grievance award instance
        :return:
        """
        # if(self.tempCase.caseType > 2):
        #     self.assertTrue(isinstance(self.tempCase.eval_case_type(), GrievanceAward))
        pass