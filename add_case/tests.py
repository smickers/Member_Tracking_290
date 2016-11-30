from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from models import Case
from add_member.models import Person
from django.db import DataError
import datetime


class CaseTests(TestCase):
    tempPerson = Person()

    def setUp(self):
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


    #test 1 - Test User enters a valid case
    def testUserEntersValidCompaintant(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 2 - Test User Enters invalid Compnainant
    def testUserEntersInValidCompaintant(self):
        with self.assertRaises(Person.DoesNotExist):
            person_holder = Person.objects.get(pk=500);
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()


    #STORIES FOR 26-6
    # Test 11 - Campus does not write to database when string length is 255 characters
    def testThatCampusIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 12 - Campus writes to database when string length is 8 characters
    def testThatCampusIsWrittenToDBWhenStringLengthIs8Characters(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 13 - Campus doesnt' write to database when length is 256 characters
    def testThatCampusIsNotWrittenWhenLengthIs256Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 14 - Campus doesn't write to database when length is 512 characters
    def testThatCampusIsNotWrittenWhenLengthIs512Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 15 - School writes to database when string length is 255 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs255Characters(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 16 - School writes to database when string length is 18 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs18Characters(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 17 - School doesnt' write to database when length is 256 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs256Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 18 - School doesn't write to database when length is 512 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs512Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 19 - Case type doesn't write to database when string length is 255 characters
    def testThatCaseTypeIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 20 - Case type writes to database when string length is 27 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs27Characters(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 21 - Case type doesnt' write to database when length is 256 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs256Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 22 - Case type doesn't write to database when length is 512 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs512Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 23 - Status doesn't write to database when string length is 255 characters
    def testThatStatusIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 24 - Status writes to database when string length is 4 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs4Characters(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 25 - Status doesnt' write to database when length is 256 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs256Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 26 - Status doesn't write to database when length is 512 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs512Characters(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 27 - Date writes to database when correct format is entered (yyyy/mm/dd)
    def testThatDateIsWrittenToDBWhenCorrectFormatIsEntered(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 28 - Date doesn't write to database when an incorrect format is entered
    def testThatDateIsNotWrittenToDBWhenIncorrectFormatIsEntered(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "twentysixteen-october-twenty"
            tempCase.full_clean()
            tempCase.save()

    # Test 29 - Campus field is not filled out, error thrown
    def testCampusIsRequired(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant =person_holder.pk
            tempCase.campus = ""
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 30 - School field is not filled out, error thrown
    def testSchoolIsRequired(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = ""
            tempCase.department = "Business Certificate"
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 31 - Case type field is not filled out, error thrown
    def testCaseTypeIsRequired(self):
        person_holder = Person.objects.get(firstName='First');
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = person_holder.pk
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.department = "Business Certificate"
            tempCase.caseType = ""
            tempCase.status = "OPEN"
            tempCase.additionalMembers = 0
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 32 - Status field is not filled out, defaults to OPEN
    def testStatusHasADefault(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = ""
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        assert (tempCase.status == 'OPEN')

    # Test 33 - Date field is not filled out, defaults to current date
    def testDateHasADefault(self):
        person_holder = Person.objects.get(firstName='First');
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = person_holder.pk
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.department = "Business Certificate"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.full_clean()
        tempCase.save()
        assert (tempCase.date == datetime.date.today())

