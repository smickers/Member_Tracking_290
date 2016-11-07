from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Person

from django.db import DataError


# region The base template
# Create your tests here.
# Base Person Object
# tempPerson = Person()
# tempPerson.memberID = 123456789
# tempPerson.firstName = 'First'
# tempPerson.middleName = 'Middle'
# tempPerson.lastName = 'Last'
# tempPerson.socNum = 123456789
# tempPerson.city = 'Sample City'
# tempPerson.mailAddress = 'Sample address'
# tempPerson.mailAddress2 = 'Sample Address 2'
# tempPerson.hPhone = 3061111234
# tempPerson.cPhone = 3061111234
# tempPerson.hEmail = 'sample@sample.com'
# tempPerson.campus = 'SASKATOON'
# tempPerson.jobType = 'FTO'
# tempPerson.committee = 'Sample Commitee'
# tempPerson.memberImage = 'image.img'
# tempPerson.bDay = '2012-03-03'
# tempPerson.pCode = 's7k5j8'
# tempPerson.gender = 'MALE'
# tempPerson.save()
# endregion



# region Tests for Creating a person
class PersonTestCase(TestCase):
    # Test 1 - check to see if the database accepts 9 digit id number
    def test9digitIdnumber(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.pCode = 's7k5j8'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 2- check to see if the database throws error if user tries to insert id number that's greater than 9 digits
    def test9digitIdnumber_less(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 1234567899
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 3 - check to see if the database throws error if user tries to insert id number that's empty
    def test9digitIdnumbererror(self):
        with self.assertRaises(IntegrityError):
            tempPerson = Person()
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.gender = 'MALE'
            tempPerson.save()

    # Test 4 - check to see if the database accepts 9 digit SIN number
    def testIfDbAcceepts9DigitSINNumber(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.pCode = 's7k5j8'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(tempPerson.socNum <= 999999999)

    # Test 5- check to see if the database throws error if user tries to create a person with no SIN number

    def testIfDbThrowsErrorIfNoSINNumber(self):
        with self.assertRaises(IntegrityError):
            tempPerson = Person()
            tempPerson.memberID = 1234567899
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.save()

    # Test 5- check to see if the database throws error if user tries to insert SIN number that's greater than 9 digits

    def testIfDbthrowserrorifusertriesToSaveSINnumbermorethan9(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 1234567899
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 7 - check to see if the first name field accepts first with less than or equal to 30 characters in length
    def testIfFirstNameFieldAcceptsFirstNameLessThanOREqual30Chars(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 8 - Check to see if the database throws an error if the first name is empty
    def testIfFirstNameFieldIfFirstNameIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 9- Check to see if the database throws an error if the first name is greater than 30
    def testIfDatabaseThrowsErrorifFirstNameisGreaterthan30characters(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 1234567899
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'Middle'
            tempPerson.firstName = 'abcdefghijklmnopqrstuvabcdeeeeaaaaaaaa'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 10- check to see if the middle name field accepts first with less than or equal to 30 characters in length
    def testIfMiddleNameFieldAcceptsMiddleNameLessThanOREqual30Chars(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.middleName = 'Middle'
        tempPerson.firstName = 'First'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)
        #

    # Test 11 - Check to see if the database throws an error if the middle name is empty
    def testIfDatabaseThrowsErrorifMiddleNameIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.hireDate = '2012-03-03'
            tempPerson.firstName = 'First'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 12- Check to see if the database throws an error if the middle name is greater than 30
    def testIfDatabaseThrowsErrorifMiddleNameIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.hireDate = '2012-03-03'
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.lastName = 'Last'
            tempPerson.middleName = 'abcdefghijklmnopqrstuvabcdeeeeaaaaaaaa'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 13 - check to see if the last name field accepts first with less than or equal to 30 characters in length
    def testIfDatabaseacceptsPersonIfitsLastNameisLessthanOrEqual30(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.lastName = 'Last'
        tempPerson.middleName = 'middle'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 14- Check to see if the database throws an error if the last name is empty
    def testIfDatabaseThrowsErroriflastNameIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'mid'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 15 Check to see if the database throws an error if the last name is greater than 30
    def testIfDatabaseThrowsErroriflastNameIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'abcdefghijklmnopqrstuvabcdeeeeaaaaaaaa'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 16 - check to see if the mailing address field accepts first with less than or equal to 50 characters in length
    def testIfDatabaseAcceptsMailingAddressWithLessThan50Characters(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.middleName = 'Middle'
        tempPerson.firstName = 'First'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 17- Check to see if the database throws an error if the mailing address is empty
    def testIfDatabaseThrowsErrorIFMailAddressIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 18 Check to see if the database throws an error if the mailing address is greater than 50
    def testIfDatabaseThrowsErrorIfMailingAddressIsGreaterThan50(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'asdffasdfgasdffasdfgasdffasdfgasdffasdfgasdffasdfgasdffasdfg'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 19 - check to see if the mailing address field accepts first with less than or equal to 50 characters in length
    def testIfDatabaseAcceptsMailingAddressWithLessThan50Characters(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 20- Check to see if the database throws an error if the mailing address is empty
    def testIfDatabaseThrowsErrorIfMailingAddressIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 21 Check to see if the database throws an error if the mailing address 2 is greater than 50
    def testIfDatabaseThrowsErrorIfMailingAddress2IsGreaterThan50(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.hireDate = '2012-03-03'
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'asdffasdfgasdffasdfgasdffasdfgasdffasdfgasdffasdfgasdffasdfg'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 22 - check to see if the city field accepts first with less than or equal to 20 characters in length
    def testIfDatabaseAcceptsCityFieldIfLessThan20Characters(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 23- Check to see if the database throws an error if the city is empty
    def testIfDatabaseThrowsAnErrorIfCityIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 24 Check to see if the database throws an error if the city is greater than 20
    def testIfDatabaseThrowsErrorIfCityIsGreaterThan20(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'abcdeabcdeabcdeabcdeabcde'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 25 - check to see if the postal code field is in the format: L#L_#L#
    def testIfDatabaseThrowsErrorIfPCodeIsInvalid(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.hireDate = '2012-03-03'
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'MALE'
            tempPerson.pCode = 'AAAA'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 25.b - check to see if the Database accepts valid postal code
    def testIfDatabaseAcceptsValidPostalCode(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'MALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 26- Check to see if the database throws an error if the postal code field is empty
    def testIfDatabaseThrowsAnErrorIfPCodeIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'MALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 27- Check to see if the Gender field value is only : 'MALE', 'FEMALE', 'UNSPECIFIED'
    def testIfDatabaseAcceptsMALEasGender(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.pCode = 's7k5j8'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 27- Check to see if the Gender field value is only : 'MALE', 'FEMALE', 'UNSPECIFIED'
    def testIfDatabaseAcceptsMALEasGender(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 28- Check to see if the Home phone field is in the format: (###)###-####
    def testIfDatabaseAcceptsMALEasGender(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 29- Check to see if the cell phone field is in the format: (###)###-####
    def testIfDatabaseAcceptsMALEasGender(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.hireDate = '2012-03-03'
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.pCode = 's7k5j8'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 30- Check to see if the email field is in a valid email format
    def testIfDatabaseThrowsAnErrorIfEmailGivenIsInvalid(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()
            self.assertTrue(Person.objects.count() == 1)

    # Test 31- Check to see if the database throws an error if the email field is empty
    def testIfDatabaseThrowsAnErrorIfEmailFieldIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.cPhone = '(306)111-1234'
            # tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()
            self.assertTrue(Person.objects.count() == 1)


    # Test 32- member image




    # Test 34- Check to see if the database throws an error if the hire date field is empty
    def testIfDatabaseThrowsErrorIfhiredatefieldIsEmpty(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 35- Check to see if Job type is one of the following: 'Full-time ongoing', 'Full-time end dated',
    # 'Part-time ongoing', 'Part-time end dated'
    def testIfDatabaseAcceptsFTOasAfulltimeongoingJobType(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    def testIfDatabaseAcceptsFTEDasAfulltimeEndDatedJobType(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTED'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.gender = 'FEMALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.pCode = 's7k5j8'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    def testIfDatabaseAcceptsPTOasAPartTimeOngoingJobType(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'PTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    def testIfDatabaseAcceptsPTEDasAPartTimeEndDatedJobType(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'PTED'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 36- Check to see if the database throws an error if the job type is invalid
    def testIfDatabaseThrowsErrorIfPersonsJobTypeIsInvalid(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'ABC'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    def testIfDatabaseThrowsErrorIfPersonsJobTypeIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            # tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.gender = 'FEMALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 37 - check to see if the program name field accepts first with less than or equal to 30 characters in length
    def testIfDatabaseAcceptsProgramWithLessThanOrEqualTO30Characters(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'PTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()


    # Test 38 - Check to see if the database throws an error if the program field is empty
    def testIFdatabaseThrowsANErrorWhenProgramFieldIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            # tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()


    # Test 39- Check to see if the database throws an error if the program field is greater than 30
    def testIfDatabaseAcceptsProgramWithLessThanOrEqualTO30Characters(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'PTO'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)

    # Test 40 - check to see if the campus name field accepts first with less than or equal to 20 characters in length
    def testIfDatabaseAcceptsNameWithLessThanOrEqualTo20CharactersInLength(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            # tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Check to see if Database throws an error if campus name is greater than 20 characters in length
    def testIfDBThrowsAnErrorIFNameISGreaterThan20CharactersInLength(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'samplesamplesamplesamplesamples'
            tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    # Test 41 - Check to see if the database throws an error if the campus field is empty
    def testIfDatabaseThrowsErrorIfPersonsCampusFieldIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            # tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            tempPerson.hireDate = '2012-03-03'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()
    #Check to see if database throws an error if hire date empty
    def testIfDatabaseThrowsErrorIfHireDateFieldIsEmpty(self):
        with self.assertRaises(ValidationError):
            tempPerson = Person()
            tempPerson.memberID = 123456789
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'mid'
            tempPerson.lastName = 'last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'city'
            tempPerson.mailAddress = 'Sample Address 1'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone = '(306)111-1234'
            tempPerson.cPhone = '(306)111-1234'
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'PTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-04'
            tempPerson.gender = 'FEMALE'
            # tempPerson.hireDate = '2012-03-03'
            tempPerson.pCode = 's7k5j8'
            tempPerson.membershipStatus = 'RESOURCE'
            tempPerson.programChoice = 'Sample Program'
            tempPerson.full_clean()
            tempPerson.save()

    #Check to see if database accepts a hire date
    def testIfDatabaseAcceptsDateForhireDate(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'mid'
        tempPerson.lastName = 'last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'city'
        tempPerson.mailAddress = 'Sample Address 1'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.hPhone = '(306)111-1234'
        tempPerson.cPhone = '(306)111-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'PTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-04'
        tempPerson.gender = 'FEMALE'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.pCode = 's7k5j8'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()
        self.assertTrue(Person.objects.count()==1)
# endregion





# region Test for Modifying person information
class ModifyPerson(TestCase):

    def setUp(self):
        tempPerson = Person()
        tempPerson.memberID = 123456789
        tempPerson.firstName = 'First'
        tempPerson.middleName = 'Middle'
        tempPerson.lastName = 'Last'
        tempPerson.socNum = 123456789
        tempPerson.city = 'Sample City'
        tempPerson.mailAddress = 'Sample address'
        tempPerson.mailAddress2 = 'Sample Address 2'
        tempPerson.pCode = 's7k5j8'
        tempPerson.hPhone = '(306)812-1234'
        tempPerson.cPhone = '(306)812-1234'
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.hireDate = '2012-03-03'
        tempPerson.gender = 'MALE'
        tempPerson.membershipStatus = 'RESOURCE'
        tempPerson.programChoice = 'Sample Program'
        tempPerson.full_clean()
        tempPerson.save()

    def testIfThereIsAMemberInsideTestDB(self):
        self.assertTrue(Person.objects.count() == 1)


    #Normal - Test 1
    def test_if_member_id_is_modifiable(self):
        person_to_edit =  Person.objects.filter(memberID=123456789)[0]
        person_to_edit.memberID = 987654321
        person_to_edit.save()
        self.assertTrue(Person.objects.get(pk=person_to_edit.pk).memberID == 987654321)



    #Exception - Test 2
    def test_if_db_throws_an_exception_if_member_id_is_left_blank(self):
        with self.assertRaises(ValidationError):
            person_to_edit = Person.objects.filter(memberID=123456789)[0]
            person_to_edit.memberID = None
            person_to_edit.full_clean()
            person_to_edit.save()


    #Boundary - Test 3
    def test_if_db_throws_an_exception_if_member_id_is_greater_than_nine_digits(self):
        with self.assertRaises(ValidationError):
            person_to_edit = Person.objects.filter(memberID=123456789)[0]
            person_to_edit.memberID = 9876543211
            person_to_edit.full_clean()
            person_to_edit.save()

    #Normal - Test 1
    def test_if_first_name_field_is_modifiable(self):
        person_to_edit =  Person.objects.filter(memberID=123456789)[0]
        person_to_edit.firstName = "New first"
        person_to_edit.save()
        self.assertTrue(Person.objects.get(pk=person_to_edit.pk).firstName == "New first")

    #Normal Test 4 - Test if user can modify existing member's first name

    def test_if_user_can_get_to_the_form_where_it_modifies_a_user(self):
        person_to_edit = Person.objects.filter(memberID=123456789)[0]
        client = Client()
        response = client.get('/member/update/' + str(person_to_edit.pk))
        print(response.status_code)
        #301 is http code for url redirection
        self.assertTrue(response.status_code == 301)
    #Normal Tests 5- Test if user can modify existing member's first name if first name supplied is less than 30 characters

    #Boundary Test 6 - Test if user cannot modify member info if supplied first name is greater than 30 characters

    #Exception Test 7 - Test if user cannot leave first name field empty

    #Exception Test 8 - Test if user can't leave middle name epty

    #Normal Test 9 - Test if user can modify middle name

    #Normal Test 10 - Test if user can modify existing member's middle name if middle name supplied is less than 30 characters

    #Exception Test 11 - Test if user cannot modify member info if supplied middle name is greater than 30 characters

    # Exception Test 12 - Test if user can't leave last name epty

    # Normal Test 13 - Test if user can modify last name

    # Normal Test 14 - Test if user can modify existing member's last name if last name supplied is less than 30 characters

    # Exception Test 15 - Test if user cannot modify member info if supplied last name is greater than 30 characters

    # Normal Test 16 - Test if member's existing SIN number is modifiable

    # Exception Test 17 - Test if




# endregion
