from django.test import TestCase
from add_member.models import Person
from .models import contactLog
from rest_framework.test import APIRequestFactory


class ContactLogFilteringTests(TestCase):
    requestFactory = APIRequestFactory()
    person1 = Person()
    person2 = Person()
    aContactLogs = [contactLog(), contactLog(), contactLog(), contactLog(), contactLog(), contactLog(), contactLog()]

    def setUp(self):
        # Create some mock contact logs and members
        self.person1.memberID = 4204444
        self.person1.firstName = 'Deborah'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Williams'
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

        self.person2.memberID = 4204444
        self.person2.firstName = 'Deborah'
        self.person2.middleName = 'Middle'
        self.person2.lastName = 'Williams'
        self.person2.socNum = 123456789
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
        self.person2.gender = 'MALE'
        self.person2.membershipStatus = 'RESOURCE'
        self.person2.programChoice = 'Sample Program'
        self.person2.full_clean()
        self.person2.save()

        self.aContactLogs[0].member = self.person1
        self.aContactLogs[0].date = '2017-02-01'
        self.aContactLogs[0].description = 'Test'
        self.aContactLogs[0].contactCode = 'E'
        self.aContactLogs[0].clean()
        self.aContactLogs[0].save()

        self.aContactLogs[1].member = self.person1
        self.aContactLogs[1].date = '2017-02-02'
        self.aContactLogs[1].description = 'Hello'
        self.aContactLogs[1].contactCode = 'F'
        self.aContactLogs[1].clean()
        self.aContactLogs[1].save()

        self.aContactLogs[2].member = self.person1
        self.aContactLogs[2].date = '2017-02-03'
        self.aContactLogs[2].description = 'World'
        self.aContactLogs[2].contactCode = 'T'
        self.aContactLogs[2].clean()
        self.aContactLogs[2].save()

        self.aContactLogs[3].member = self.person1
        self.aContactLogs[3].date = '2017-02-15'
        self.aContactLogs[3].description = 'A CL'
        self.aContactLogs[3].contactCode = 'P'
        self.aContactLogs[3].clean()
        self.aContactLogs[3].save()

        self.aContactLogs[4].member = self.person1
        self.aContactLogs[4].date = '2016-02-01'
        self.aContactLogs[4].contactCode = 'P'
        self.aContactLogs[4].clean()
        self.aContactLogs[4].save()

        self.aContactLogs[5].member = self.person1
        self.aContactLogs[5].date = '2017-02-19'
        self.aContactLogs[5].description = 'Test'
        self.aContactLogs[5].contactCode = 'M'
        self.aContactLogs[5].clean()
        self.aContactLogs[5].save()

        self.aContactLogs[6].member = self.person2
        self.aContactLogs[6].date = '2016-04-05'
        self.aContactLogs[6].description = 'Goodbye'
        self.aContactLogs[6].contactCode = 'M'
        self.aContactLogs[6].clean()
        self.aContactLogs[6].save()

    def test_related_member_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter?member=1")
        self.assertEquals(len(request.data), 6)

    def test_date_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter?date=2017-01-01?condition=lt")
        self.assertEquals(len(request.data), 2)

    def test_description_filtering_and_empty_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter?description=")
        self.assertEquals(len(request.data), 1)

    def test_contact_code_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter/contactCode=M")
        self.assertEquals(len(request.data), 2)

    def test_OR_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter/contactCode=M?condition=OR?contactCode=P")
        self.assertEquals(len(request.data), 4)

    def test_AND_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter/contactCode=M?condition=AND?description=Goodbye")
        self.assertTrue(len(request.data), 1)

    def test_NOT_filtering(self):
        request = self.requestFactory.get("/api-root/contact_log/filter/contactCode=P?condition=NOT")
        self.assertEquals(len(request.data), 5)

    def test_AND_OR_chaining(self):
        request = self.requestFactory.get("/api-root/contact_log/filter/date=2017-01-01?condition=gt?condition=AND?contactCode=M?criteria=OR?member=2")
        self.assertEquals(len(request.data),2)
