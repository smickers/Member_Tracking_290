from django.test import TestCase
from grievance_award_creation.models import GrievanceAward
from add_member.models import Person
from add_case.models import Case, CasePrograms
from django.core.urlresolvers import reverse

class CaseLinksToGrievanceAwards(TestCase):
    """ Test the connection between grievance award its case"""

    def __init__(self, *args, **kwargs):
        """Initialize the object required for the test"""
        super(CaseLinksToGrievanceAwards, self).__init__(*args, **kwargs)
        self.person1 = Person()
        self.person2 = Person()
        self.person3 = Person()
        self.tempCase = Case()
        self.tempCase2 = Case()
        self.ga2 = GrievanceAward()
        self.ga = GrievanceAward()

    def setUp(self):
        """Setup method to initialize essential Objects"""

        self.case_prog = CasePrograms(name="Computer Systems Technology")
        self.case_prog.save()

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

        self.person3.memberID = 4204442
        self.person3.firstName = 'First2'
        self.person3.middleName = 'Middle2'
        self.person3.lastName = 'Last2'
        self.person3.socNum = 123456788
        self.person3.city = 'Sample City'
        self.person3.mailAddress = 'Sample address'
        self.person3.mailAddress2 = 'Sample Address 2'
        self.person3.pCode = 'S7K5J8'
        self.person3.hPhone = '(306)812-1234'
        self.person3.cPhone = '(306)812-1234'
        self.person3.hEmail = 'sample@sample.com'
        self.person3.campus = 'SASKATOON'
        self.person3.jobType = 'FTO'
        self.person3.committee = 'Sample Commitee'
        self.person3.memberImage = 'image.img'
        self.person3.bDay = '2012-03-03'
        self.person3.hireDate = '2012-03-03'
        self.person3.gender = 'MALE'
        self.person3.membershipStatus = 'RESOURCE'
        self.person3.programChoice = 'Sample Program'
        self.person3.full_clean()
        self.person3.save()

        self.tempCase.lead = 123456789
        self.tempCase.complainant = self.person1
        self.tempCase.campus = "Saskatoon"
        self.tempCase.school = "School of Business"
        self.tempCase.department = "Learning Technologies"

        self.tempCase.program = self.case_prog
        self.tempCase.caseType = 7
        self.tempCase.status = "OPEN"
        self.tempCase.additionalNonMembers = ""

        self.tempCase.docs = None
        self.tempCase.logs = None
        self.tempCase.date = "2016-10-20"
        self.tempCase.full_clean()
        self.tempCase.save()

        self.tempCase2.lead = 123456789
        self.tempCase2.complainant = self.person1
        self.tempCase2.campus = "Saskatoon"
        self.tempCase2.school = "School of Business"
        self.tempCase2.department = "Learning Technologies"
        self.tempCase2.program = self.case_prog
        self.tempCase2.caseType = 5
        self.tempCase2.status = "OPEN"
        self.tempCase2.additionalNonMembers = ""
        self.tempCase2.docs = None
        self.tempCase2.logs = None
        self.tempCase2.date = "2016-10-20"
        self.tempCase2.full_clean()
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
        """
        self.assertTrue(isinstance(self.ga.recipient, Person))


    def test_grievance_award_cannot_be_associated_with_multiple_member_if_grievance_award_type_is_member(self):
        """
        Purpose: test to see if grievance award can only be associated with a single member if it is of type
        member
        """

        # Send a get request to the edit case page referencing the tempCase object
        response = self.client.get(reverse('add_case:case_edit', kwargs={'pk': self.tempCase.pk}))
        # Get the initial values. This will return a dictionary. We will modify the value of the additional member field
        # later
        oldresponsevalues = response.context['form'].initial
        # create a temporary person list
        person_list = list()
        # append person2 an person3's primary key to the list
        person_list.append(self.person2.pk)
        person_list.append(self.person3.pk)
        # modify the old response values to have an updated list of additional Members
        oldresponsevalues['additionalMembers'] = person_list
        # do a post request to the case edit page and send the newly updated response values
        response = self.client.post(reverse('add_case:case_edit', kwargs={'pk': self.tempCase.pk}), oldresponsevalues)
        # check if the response contains an error regarding the additional members
        self.assertContains(response, "You can only select 1 member")
        # check if the recipient only return an object with an instance of Person. This means that there's only one
        #   person returned
        self.assertTrue(isinstance(self.ga.recipient, Person))

    def test_grievance_award_can_be_associated_with_multiple_member_if_grievance_award_type_is_of_policy(self):
        """
        Purpose: test to see if grievance award can only be associated with a multiple member if it is of type
        policy
        """
        # ensure that the case that the ga object references has a case type of Policy
        self.assertTrue(self.ga2.case.get_caseType_display() == "GRIEVANCES - POLICY")
        # Send a get request to the edit case page referencing the tempCase2 object
        response = self.client.get(reverse('add_case:case_edit', kwargs={'pk': self.tempCase2.pk}))
        # Get the initial values. This will return a dictionary. We will modify the value of the additional member field
        # later
        oldresponsevalues = response.context['form'].initial
        # create a list and append the existing members to the list of new members (person2, person3)
        temp_list = list()
        temp_list += list(oldresponsevalues['additionalMembers']) + [self.person2.pk, self.person3.pk]
        # modify the old response values to have an updated list of additional Members
        oldresponsevalues['additionalMembers'] = temp_list
        # do a post request to the case edit page and send the newly updated response values
        response = self.client.post(reverse('add_case:case_edit', kwargs={'pk': self.tempCase2.pk}), oldresponsevalues)
        # check if the response does not contain an error regarding the additional members
        self.assertNotContains(response, "You can only select 1 member if a grievance type is INDIVIDUAL", status_code=302)
        # check if the recipient property returns a person list with a length of 3. This confirms that the recipient
        #   property recognizes that the case type of which the grievance award is referencing to is not a type of
        #   "INDIVIDUAL"
        self.assertEqual( len(self.ga2.recipient), 3)