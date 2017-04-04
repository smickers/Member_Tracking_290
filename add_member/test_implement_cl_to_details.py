from django.test import SimpleTestCase
from .models import Person
from add_case.models import Case
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
        contactLog.objects.all().delete()
        Person.objects.all().delete()
        Case.objects.all().delete()
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
        self.cl_1.description = "First contact log for Deb."
        self.cl_1.contactCode = 'E'
        self.cl_1.full_clean()
        self.cl_1.save()

        self.cl_2.member = self.kk
        self.cl_2.date = '2017-02-12'
        self.cl_2.description = "First contact log for Kelly."
        self.cl_2.contactCode = 'M'
        self.cl_2.full_clean()
        self.cl_2.save()

        self.cl_3.member = self.dw
        self.cl_3.date = '2017-02-12'
        self.cl_3.description = "Second contact log for De2b."
        self.cl_3.contactCode = 'P'
        self.cl_3.full_clean()
        self.cl_3.save()

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
        self.assertContains(response, self.cl_2.description)

    # Test 4: User views a member's details page and sees multiple contact logs
    # NOTE: Using "Deborah Williams" as we know they have more than one contact log associated with them.
    def test_multiple_cl_visible_on_details_page(self):
        # Have the Client return the member's details page for the Deb Williams, passing in Deb's PK as an argument
        response = self.client.get(reverse('add_member:member_detail', args=[self.dw.pk]))
        # Ensure the response contains Deb's name, so we know we have the right page.
        self.assertContains(response, "Deborah Williams")
        # Ensure the contact log descriptions are visible, meaning they all appear on the page, and not just one.
        self.assertContains(response, self.cl_1.description)
        self.assertContains(response, self.cl_3.description)

    # Test 5: User views a member's details page and they do not have associated contact logs
    # NOTE: Using "Walky Walkerton" as we know they do not have any contact logs associated with them.
    def test_no_cl_shown_when_none_associated_to_member(self):
        # Have the Client return the member's details page for Walky Walkerton, passing in Walky's PK as an argument
        response = self.client.get(reverse('add_member:member_detail', args=[self.ww.pk]))
        # Ensure the response contains Walky's name, so we know we have the right page.
        self.assertTrue(response.context['person'].__str__(), "Walky Walkerton")
        self.assertTrue("Contact Log" in response.content)

    # Test 6: Test that select boxes are disabled when visiting from a url where a PK is passed in:
    def test_select_box_disabled_when_pk_passed_in(self):
        # Have the client return a contact log creation page, to create a new contact log specifically for Deb Williams
        response = self.client.get(reverse('contact_log_creation:contact_log_add_direct', args=[self.dw.pk]))
        # Ensure that the response indicates that the select box container for members is disabled
        self.assertContains(response, 'disabled')

    # Test 7: Test that select boxes are still enabled when visiting from a URL where a PK is not passed in:
    def test_select_box_enabled_when_no_pk_passed_in(self):
        # Have the client return a contact log creation page, to create a new contact log specifically for Deb Williams
        response = self.client.get(reverse('contact_log_creation:contact_log_add'))
        # Ensure that the response indicates that the select box container for members is disabled
        self.assertContains(response, 'disabled')