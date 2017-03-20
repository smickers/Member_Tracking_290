from django.test import SimpleTestCase
from .models import Person
from contact_log.models import contactLog
from django.urls import reverse


# Test to implement contact logs to a member's details page
# NOTE: First two tests will always pass as they test CL functionality, and not implementing fields in other fields.
class TestImplementCLsToMemberDetails(SimpleTestCase):
    # lets us use SimpleTestCase to do database queries
    allow_database_queries = True

    # Initialize the Test object required for the unit tests
    def __init__(self, *args, **kwargs):
        super(TestImplementCLsToMemberDetails, self).__init__(*args, **kwargs)
        self.dw = Person()
        self.kk = Person()
        self.ww = Person()
        self.cl_1 = contactLog()
        self.cl_2 = contactLog()
        self.cl_3 = contactLog()

    # Setup method to initialize all of the essential objects
    def setUp(self):
        self.dw.memberID = 4204444
        self.dw.firstName = 'Deborah'
        self.dw.middleName = 'Mary'
        self.dw.lastName = 'Williams'
        self.dw.socNum = 123456789
        self.dw.city = 'Saskatoon'
        self.dw.mailAddress = 'Sample address'
        self.dw.mailAddress2 = 'Sample Address 2'
        self.dw.pCode = 'S7K5J8'
        self.dw.hPhone = '(306)812-1234'
        self.dw.cPhone = '(306)812-1234'
        self.dw.hEmail = 'sample@sample.com'
        self.dw.campus = 'SASKATOON'
        self.dw.jobType = 'FTO'
        self.dw.committee = 'Sample Commitee'
        self.dw.memberImage = 'image.img'
        self.dw.bDay = '2012-03-03'
        self.dw.hireDate = '2012-03-03'
        self.dw.gender = 'MALE'
        self.dw.membershipStatus = 'RESOURCE'
        self.dw.programChoice = 'Sample Program'
        self.dw.full_clean()
        self.dw.save()

        self.kk.memberID = 4204444
        self.kk.firstName = 'Kelly'
        self.kk.middleName = 'Mason'
        self.kk.lastName = 'Kentucky'
        self.kk.socNum = 123456789
        self.kk.city = 'Regina'
        self.kk.mailAddress = 'Sample address'
        self.kk.mailAddress2 = 'Sample Address 2'
        self.kk.pCode = 'S7K5J8'
        self.kk.hPhone = '(306)812-1234'
        self.kk.cPhone = '(306)812-1234'
        self.kk.hEmail = 'sample@sample.com'
        self.kk.campus = 'REGINA'
        self.kk.jobType = 'PTED'
        self.kk.committee = 'Sample Commitee'
        self.kk.memberImage = 'image.img'
        self.kk.bDay = '2012-03-03'
        self.kk.hireDate = '2012-03-03'
        self.kk.gender = 'MALE'
        self.kk.membershipStatus = 'RESOURCE'
        self.kk.programChoice = 'Sample Program'
        self.kk.full_clean()
        self.kk.save()

        self.ww.memberID = 4204444
        self.ww.firstName = 'Walky'
        self.ww.middleName = 'E'
        self.ww.lastName = 'Walkerton'
        self.ww.socNum = 123456789
        self.ww.city = 'Prince Albert'
        self.ww.mailAddress = 'Sample address'
        self.ww.mailAddress2 = 'Sample Address 2'
        self.ww.pCode = 'S7K5J8'
        self.ww.hPhone = '(306)812-1234'
        self.ww.cPhone = '(306)812-1234'
        self.ww.hEmail = 'sample@sample.com'
        self.ww.campus = 'PA'
        self.ww.jobType = 'PTO'
        self.ww.committee = 'Sample Commitee'
        self.ww.memberImage = 'image.img'
        self.ww.bDay = '2012-03-03'
        self.ww.hireDate = '2012-03-03'
        self.ww.gender = 'MALE'
        self.ww.membershipStatus = 'RESOURCE'
        self.ww.programChoice = 'Sample Program'
        self.ww.full_clean()
        self.ww.save()

        self.cl_1.member = self.dw
        self.cl_1.date = '2017-02-12'
        self.cl_1.description = "Deborah's contact log."
        self.cl_1.contactCode = 'E'
        self.cl_1.full_clean()
        self.cl_1.save()

        self.cl_1.member = self.kk
        self.cl_1.date = '2017-02-12'
        self.cl_1.description = "Kelly's contact log."
        self.cl_1.contactCode = 'M'
        self.cl_1.full_clean()
        self.cl_1.save()

        self.cl_1.member = self.dw
        self.cl_1.date = '2017-02-12'
        self.cl_1.description = "Deborah's second contact log."
        self.cl_1.contactCode = 'P'
        self.cl_1.full_clean()
        self.cl_1.save()

    # Test 1 : Test that the contact logs are associated with people (so, test that setUp worked correctly)
    def test_cl_associated_with_members_in_db(self):
        test_one = self.assertTrue(isinstance(self.cl_1.member, Person))
        test_two = self.assertTrue(isinstance(self.cl_1.member, Person))
        test_three = self.assertTrue(isinstance(self.cl_1.member, Person))
        self.assertEqual(test_one, test_two)
        self.assertEqual(test_three, test_two)

    # Test 2: Test that a contact log cannot be created for someone who does not exist in the database:
    def test_cl_not_created_for_member_not_in_db(self):
        with self.assertRaisesMessage(Person.DoesNotExist, "Person matching query does not exist."):
            fake_cl = contactLog()
            fake_cl.member = Person.objects.get(firstName="Daffy")
            fake_cl.date = '2017-03-20'
            fake_cl.description = ""
            fake_cl.contactCode = 'P'
            fake_cl.full_clean()
            fake_cl.save()

    # Test 3: User views a member's details page and sees a contact log
    # NOTE: Using "Kelly Kentucky" as we know they only have a single contact log associated with them.
    def test_cl_visible_on_details_page(self):
        # Have the Client return the member's details page for the Kelly Kentucky, passing in Kelly's PK as an argument
        response = self.client.get(reverse('add_member:member_detail', args=[self.kk.pk]))
        # Ensure the response contains Kelly's name, so we know we have the right page.
        self.assertContains(response, "Kelly Kentucky")
        # Ensure that the contact log's description comes up, meaning that it appears on the page.
        self.assertContains(response, "Kelly's contact log.")

    # Test 4: User views a member's details page and sees multiple contact logs
    # NOTE: Using "Deborah Williams" as we know they have more than one contact log associated with them.
    def test_multiple_cl_visible_on_details_page(self):
        # Have the Client return the member's details page for the Deb Williams, passing in Deb's PK as an argument
        response = self.client.get(reverse('add_member:member_detail', args=[self.dw.pk]))
        # Ensure the response contains Deb's name, so we know we have the right page.
        self.assertContains(response, "Deborah Williams")
        # Ensure the contact log descriptions are visible, meaning they all appear on the page, and not just one.
        self.assertContains(response, "Deborah's contact log.")
        self.assertContains(response, "Deborah's second contact log.")

    # Test 5: User views a member's details page and they do not have associated contact logs
    # NOTE: Using "Wally Walkerton" as we know they do not have any contact logs associated with them.
    def test_no_cl_shown_when_none_associated_to_member(self):
        # Have the Client return the member's details page for Walky Walkerton, passing in Walky's PK as an argument
        response = self.client.get(reverse('add_member:member_detail', args=[self.ww.pk]))
        # Ensure the response contains Walky's name, so we know we have the right page.
        self.assertContains(response, "Walky Walkerton")
        self.assertContains(response, "No contact logs associated to Walky Walkerton")
