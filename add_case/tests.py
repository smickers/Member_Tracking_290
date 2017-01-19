from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from add_case.models import *
from django.db import DataError
import datetime
from add_member.models import Person


class CaseTests(TestCase):
    person1 = Person()
    program = CasePrograms()

    def setUp(self):
        self.person1.memberID = 4204444
        self.person1.firstName = 'First'
        self.person1.middleName = 'Middle'
        self.person1.lastName = 'Last'
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

        self.program.name = 'Business - Certificate'
        self.program.full_clean()
        self.program.save()

    # Test 11 - Campus does not write to database when string length is 255 characters
    def testThatCampusIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()
            tempCase.additionalMembers.add(self.person1)
            tempCase.save()


    # Test 12 - Campus writes to database when string length is 8 characters
    def testThatCampusIsWrittenToDBWhenStringLengthIs8Characters(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        tempCase.additionalMembers.add(self.person1)
        tempCase.save()

    # # Test 13 - Campus doesnt' write to database when length is 256 characters
    def testThatCampusIsNotWrittenWhenLengthIs256Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()
            tempCase.additionalMembers.add(self.person1)
            tempCase.save()

    # # Test 14 - Campus doesn't write to database when length is 512 characters
    def testThatCampusIsNotWrittenWhenLengthIs512Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"
            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()
    # Jan 17, 2017 - Test case is no longer needed. School is a select box now and model will still validate for length
    # # Test 15 - School writes to database when string length is 255 characters
    # def testThatSchoolIsWrittenToDBWhenStringLengthIs255Characters(self):
    #     tempCase = Case()
    #     tempCase.lead = 123456789
    #     tempCase.complainant = self.person1
    #     tempCase.campus = "Saskatoon"
    #     tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
    #                       "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
    #                       "natoque penatibus et magnis dis parturient montes, nascetur " \
    #                       "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
    #     tempCase.program = self.program
    #     tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
    #     tempCase.status = "OPEN"
    #     tempCase.additionalNonMembers = ""
    #     tempCase.docs = None
    #     tempCase.logs = None
    #     tempCase.date = "2016-10-20"
    #     tempCase.full_clean()
    #     tempCase.save()

    # Test 16 - School writes to database when string length is 18 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs18Characters(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 17 - School doesnt' write to database when length is 256 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs256Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 18 - School doesn't write to database when length is 512 characters
    def testThatSchoolIsWrittenToDBWhenStringLengthIs512Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 19 - Case type doesn't write to database when string length is 255 characters
    def testThatCaseTypeIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 20 - Case type writes to database when string length is 27 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs27Characters(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"

        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 21 - Case type doesnt' write to database when length is 256 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs256Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 22 - Case type doesn't write to database when length is 512 characters
    def testThatCaseTypeIsWrittenToDBWhenStringLengthIs512Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 23 - Status doesn't write to database when string length is 255 characters
    def testThatStatusIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                                "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                                "natoque penatibus et magnis dis parturient montes, nascetur " \
                                "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 24 - Status writes to database when string length is 4 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs4Characters(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"

        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 25 - Status doesnt' write to database when length is 256 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs256Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 26 - Status doesn't write to database when length is 512 characters
    def testThatStatusIsWrittenToDBWhenStringLengthIs512Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
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

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 27 - Date writes to database when correct format is entered (yyyy/mm/dd)
    def testThatDateIsWrittenToDBWhenCorrectFormatIsEntered(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"

        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 28 - Date doesn't write to database when an incorrect format is entered
    def testThatDateIsNotWrittenToDBWhenIncorrectFormatIsEntered(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "twentysixteen-october-twenty"
            tempCase.full_clean()
            tempCase.save()

    # Test 29 - Campus field is not filled out, error thrown
    def testCampusIsRequired(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = ""
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 30 - School field is not filled out, error thrown
    def testSchoolIsRequired(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = ""
            tempCase.program = self.program
            tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 31 - Case type field is not filled out, error thrown
    def testCaseTypeIsRequired(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = self.person1
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
            tempCase.program = self.program
            tempCase.caseType = ""
            tempCase.status = "OPEN"

            tempCase.additionalNonMembers = ""
            tempCase.docs = None
            tempCase.logs = None
            tempCase.date = "2016-10-20"
            tempCase.full_clean()
            tempCase.save()

    # Test 32 - Status field is not filled out, defaults to OPEN
    def testStatusHasADefault(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = ""
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()
        assert (tempCase.status == 'OPEN')

    # Test 33 - Date field is not filled out, defaults to current date
    def testDateHasADefault(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = self.person1
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.program = self.program
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"

        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.full_clean()
        tempCase.save()
        assert (tempCase.date == datetime.date.today())
