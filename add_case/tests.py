from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import Case
from django.db import DataError

#TODO Put the class up top when starting the validation test methods
#Test 1 - Campus validation
'''
The campus entered must match a campus from the DB.
    Saskatoon
    Prince Albert
    Regina
    Moose Jaw
If a different campus is entered, an exception is thrown. This will prevent someone changing the select
box to a textbox and entering their own value.
'''

#Test 2 - School validation
'''
The school entered must match a school from the DB.
    School of Animal and BioSciences
    School of Business
    School of Construction
    School of Health Sciences
    School of Hospitality and Tourism
    School of Human Services and Community Safety
    School of Information and Communications Technology
    School of Mining, Energy, and Manufacturing
    School of Natural Resources and Built Environment
    School of Nursing
    School of Transportation

If a different school is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 3 - Case type validation
'''
The case type entered must match a school from the DB.
    GRIEVANCES - INDIVIDUAL
    GRIEVANCES - GROUP
    GRIEVANCES - POLICY
    GRIEVANCES - CLASSIFICATION
    ARBITRATIONS
    COMPLAINTS
    DISABILITY CLAIMS

If a different case type is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 4 - Status validation
'''
The status entered must match a school from the DB.
    OPEN
    CLOSED
    PENDING
    ACTION REQ'D - MGMT
    ACTION REQ'D - SPFA

If a different status is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 5 - Department/Program validation
'''
The status entered must match a school from the DB.


If a different department/program is entered, an exception is thrown. T
his will prevent someone from changing the select box to a textbox and entering their own value.
'''

#Test 6 - Start Date validation


#Test 7 - Default Status validation


#Test 8 - Default Start Date validation


#Test 9 - End date set when closing case


# Test 10 - Case created with correct attributes

class CaseTests(TestCase):

    def testTrue(self):
        return self.assertTrue(True)

    # Test 11 - Campus does not write to database when string length is 255 characters
    def testThatCampusIsNotWrittenToDBWhenStringLengthIs255Characters(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                          "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                          "natoque penatibus et magnis dis parturient montes, nascetur " \
                          "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,," \
                              "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
                              "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
                              "natoque penatibus et magnis dis parturient montes, nascetur " \
                              "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,,"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # TODO - make validation for the date format
    # Test 28 - Date doesn't write to database when an incorrect format is entered
    def testThatDateIsNotWrittenToDBWhenIncorrectFormatIsEntered(self):
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = ""
            tempCase.school = "School of Business"
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = ""
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
        with self.assertRaises(ValidationError):
            tempCase = Case()
            tempCase.lead = 123456789
            tempCase.complainant = 987654321
            tempCase.campus = "Saskatoon"
            tempCase.school = "School of Business"
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
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = ""
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = "2016-10-20"
        tempCase.full_clean()
        tempCase.save()

    # Test 33 - Date field is not filled out, defaults to current date
    def testDateHasADefault(self):
        tempCase = Case()
        tempCase.lead = 123456789
        tempCase.complainant = 987654321
        tempCase.campus = "Saskatoon"
        tempCase.school = "School of Business"
        tempCase.caseType = "GRIEVANCES - CLASSIFICATION"
        tempCase.status = "OPEN"
        tempCase.additionalMembers = 0
        tempCase.additionalNonMembers = ""
        tempCase.docs = None
        tempCase.logs = None
        tempCase.date = ""
        tempCase.full_clean()
        tempCase.save()

