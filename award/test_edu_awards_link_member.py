from django.test import TestCase
from models import Person, EducationAward
from models import EducationAward
from django.core.exceptions import ValidationError
from django.db import DataError

#Test class for Educational Awards Editing and Linking members
class TestEduAwardLinkMember(TestCase):
    tempPerson1 = Person()
    tempPerson2 = Person()
    eduAward1 = EducationAward()
    eduAward2 = EducationAward()

    #set up method for tests
    def setUp(self):
        # Set up a Member1 for testing
        self.tempPerson1.memberID = 1
        self.tempPerson1.firstName = 'Tim'
        self.tempPerson1.middleName = 'Middle'
        self.tempPerson1.lastName = 'Jones'
        self.tempPerson1.socNum = 123456789
        self.tempPerson1.city = 'Sample City'
        self.tempPerson1.mailAddress = 'Sample address'
        self.tempPerson1.mailAddress2 = 'Sample Address 2'
        self.tempPerson1.pCode = 's7k5j8'
        self.tempPerson1.hPhone = '(306)812-1234'
        self.tempPerson1.cPhone = '(306)812-1234'
        self.tempPerson1.hEmail = 'sample@sample.com'
        self.tempPerson1.campus = 'SASKATOON'
        self.tempPerson1.jobType = 'FTO'
        self.tempPerson1.committee = 'Sample Commitee'
        self.tempPerson1.memberImage = 'image.img'
        self.tempPerson1.bDay = '2012-03-03'
        self.tempPerson1.hireDate = '2012-03-03'
        self.tempPerson1.gender = 'MALE'
        self.tempPerson1.membershipStatus = 'RESOURCE'
        self.tempPerson1.programChoice = 'Sample Program'
        self.tempPerson1.full_clean()
        self.tempPerson1.save()

        # Set up a Member 2 for testing
        self.tempPerson2.memberID = 1
        self.tempPerson2.firstName = 'Tim'
        self.tempPerson2.middleName = 'Middle'
        self.tempPerson2.lastName = 'Jones'
        self.tempPerson2.socNum = 123456789
        self.tempPerson2.city = 'Sample City'
        self.tempPerson2.mailAddress = 'Sample address'
        self.tempPerson2.mailAddress2 = 'Sample Address 2'
        self.tempPerson2.pCode = 's7k5j8'
        self.tempPerson2.hPhone = '(306)812-1234'
        self.tempPerson2.cPhone = '(306)812-1234'
        self.tempPerson2.hEmail = 'sample@sample.com'
        self.tempPerson2.campus = 'SASKATOON'
        self.tempPerson2.jobType = 'FTO'
        self.tempPerson2.committee = 'Sample Commitee'
        self.tempPerson2.memberImage = 'image.img'
        self.tempPerson2.bDay = '2012-03-03'
        self.tempPerson2.hireDate = '2012-03-03'
        self.tempPerson2.gender = 'MALE'
        self.tempPerson2.membershipStatus = 'RESOURCE'
        self.tempPerson2.programChoice = 'Sample Program'
        self.tempPerson2.full_clean()
        self.tempPerson2.save()

        self.eduAward1.description = 'Test'
        self.eduAward1.awardAmount = 5000
        self.eduAward1.clean()
        self.eduAward1.save()

        self.eduAward1 = EducationAward()
        self.eduAward2.description = 'Test2'
        self.eduAward2.awardRecipient = None
        self.eduAward2.awardedMember = None
        self.eduAward2.award_amount = 5000
        self.eduAward2.clean()
        self.eduAward2.save()

    #Tests successfully linking a member and dependent to an existing award
    def test_linking_existing_member_to_award(self):
        self.eduAward1.awardedMember = self.tempPerson1
        self.eduAward1.awardRecipient = 'Tim Jr.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward1.clean()
        self.eduAward1.save()
        self.assertTrue(True)


    #Tests that it is not possible to link a dependents to more than one award
    def test_member_with_dependent_with_award_cannot_be_linked_to_award(self):
        self.eduAward1.awardedMember = self.tempPerson1
        self.eduAward1.awardRecipient = 'Tim Jr.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward1.clean()
        self.eduAward1.save()
        with self.assertRaisesMessage(ValidationError,'Cannot assign recipient to more than one award'):
            self.eduAward2.awardedMember = self.tempPerson1
            self.eduAward2.awardRecipient = 'Tim Jr.'
            self.eduAward1.awardType = 'Internal'
            self.eduAward1.yearAwarded = 2017
            self.eduAward2.clean()
            self.eduAward2.save()

    #Tests that an award can be linked to a member with a different dependent
    def test_member_with_different_dependent_can_be_linked_to_award(self):
        self.eduAward1.awardedMember = self.tempPerson1
        self.eduAward1.awardRecipient = 'Tim Jr.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward1.clean()
        self.eduAward1.save()
        self.eduAward2.awardedMember = self.tempPerson1
        self.eduAward2.awardRecipient = 'Tim Jr2.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward2.clean()
        self.eduAward2.save()

    # Test 5: Ensure dependents with the same name can be given awards,
    # as long as they have different related members.
    def test_same_dependent_names_different_related_members(self):
        self.eduAward1.awardedMember = self.tempPerson1
        self.eduAward1.awardRecipient = 'Tim Jr.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward1.clean()
        self.eduAward1.save()
        self.eduAward2.awardedMember = self.tempPerson2
        self.eduAward2.awardRecipient = 'Tim Jr.'
        self.eduAward1.awardType = 'Internal'
        self.eduAward1.yearAwarded = 2017
        self.eduAward2.clean()
        self.eduAward2.save()
        self.assertTrue(True)


    #Tests that if a member is selected, a recipient also has to be entered
    def test_award_is_not_saved_with_member_selected_no_recipient(self):
        with self.assertRaisesMessage(ValidationError, 'Cannot assign an award with only a member '):
            self.eduAward1.awardedMember = self.tempPerson1
            self.eduAward1.awardType = 'Internal'
            self.eduAward1.yearAwarded = 2017
            self.eduAward1.clean()
            self.eduAward1.save()

    #Tests that if a recipient is entered a member also has to be selected
    def test_award_is_not_saved_with_member_selected_no_recipient(self):
        with self.assertRaisesMessage(ValidationError, 'Cannot assign an award without an associated member'):
            self.eduAward2.awardRecipient = 'Tim Jr2.'
            self.eduAward2.awardedMember = None
            self.eduAward1.awardType = 'Internal'
            self.eduAward1.yearAwarded = 2017
            self.eduAward2.clean()
            self.eduAward2.save()