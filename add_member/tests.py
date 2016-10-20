from django.test import TestCase
from django.db import IntegrityError
from .models import Person
from django.db import DataError
# Create your tests here.

#Base Person Object
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
    # tempPerson.save()


class PersonTestCase(TestCase):
    #Test 1 - check to see if the database accepts 9 digit id number
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
        tempPerson.hPhone= 3061111234
        tempPerson.cPhone = 3061111234
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.save()
        self.assertTrue(Person.objects.count() == 1)
    #Test 2- check to see if the database throws error if user tries to insert id number that's greater than 9 digits
    def test9digitIdnumber_less(self):
        with self.assertRaises(ValueError):
            tempPerson = Person()
            tempPerson.memberID = 1234567899
            tempPerson.firstName = 'First'
            tempPerson.middleName = 'Middle'
            tempPerson.lastName = 'Last'
            tempPerson.socNum = 123456789
            tempPerson.city = 'Sample City'
            tempPerson.mailAddress = 'Sample address'
            tempPerson.mailAddress2 = 'Sample Address 2'
            tempPerson.hPhone= 3061111234
            tempPerson.cPhone = 3061111234
            tempPerson.hEmail = 'sample@sample.com'
            tempPerson.campus = 'SASKATOON'
            tempPerson.jobType = 'FTO'
            tempPerson.committee = 'Sample Commitee'
            tempPerson.memberImage = 'image.img'
            tempPerson.bDay = '2012-03-03'
            tempPerson.clean()
            tempPerson.save()

    #Test 3 - check to see if the database throws error if user tries to insert id number that's empty
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
            tempPerson.save()


    #Test 4 - check to see if the database accepts 9 digit SIN number
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
        tempPerson.hPhone = 3061111234
        tempPerson.cPhone = 3061111234
        tempPerson.hEmail = 'sample@sample.com'
        tempPerson.campus = 'SASKATOON'
        tempPerson.jobType = 'FTO'
        tempPerson.committee = 'Sample Commitee'
        tempPerson.memberImage = 'image.img'
        tempPerson.bDay = '2012-03-03'
        tempPerson.save()
        self.assertTrue(tempPerson.socNum <= 999999999)

    #Test 5- check to see if the database throws error if user tries to create a person with no SIN number

    def testIfDbAcceepts9DigitSINNumber(self):
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
            tempPerson.save()


    #Test 5- check to see if the database throws error if user tries to insert SIN number that's greater than 9 digits

    def testIfDbthrowserrorifusertriesToSaveSINnumbermorethan9(self):
        tempPerson = Person()
        tempPerson.memberID = 1234567899
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
        tempPerson.save()

    #Test 7 - check to see if the first name field accepts first with less than or equal to 30 characters in length
    def testIfFirstNameFieldAcdeptsFirstNameLessThanOREqual30Chars(selfs):
        tempPerson = Person()
        tempPerson.memberID = 1234567899
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
        tempPerson.save()

    #Test 8 - Check to see if the database throws an error if the first name is empty
    def testIfFirstNameFieldIfFirstNameIsEmpty(self):
        with self.assertRaises(IntegrityError):
            tempPerson = Person()
            tempPerson.memberID = 1234567899
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
            tempPerson.save()


    #Test 9- Check to see if the database throws an error if the first name is greater than 30
    def testIfDatabaseThrowsErrorifFirstNameisGreaterthan30characters(self):
        tempPerson = Person()
        tempPerson.memberID = 1234567899
        tempPerson.middleName = 'Middle'
        tempPerson.firstName = 'abcdefghijklmnopqrstuvabcdeeee'
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
        tempPerson.save()


    # Test 10- check to see if the middle name field accepts first with less than or equal to 30 characters in length


    # Test 11 - Check to see if the database throws an error if the middle name is empty


    # Test 12- Check to see if the database throws an error if the middle name is greater than 30


    # Test 13 - check to see if the last name field accepts first with less than or equal to 30 characters in length


    # Test 14- Check to see if the database throws an error if the last name is empty


    # Test 15 Check to see if the database throws an error if the last name is greater than 30


    # Test 16 - check to see if the mailing address field accepts first with less than or equal to 50 characters in length


    # Test 17- Check to see if the database throws an error if the mailing address is empty


    # Test 18 Check to see if the database throws an error if the mailing address is greater than 50


    # Test 19 - check to see if the mailing address field accepts first with less than or equal to 50 characters in length


    # Test 20- Check to see if the database throws an error if the mailing address is empty


    # Test 21 Check to see if the database throws an error if the mailing address is greater than 50


    # Test 22 - check to see if the city field accepts first with less than or equal to 20 characters in length


    # Test 23- Check to see if the database throws an error if the city is empty


    # Test 24 Check to see if the database throws an error if the city is greater than 20


    # Test 25 - check to see if the postal code field is in the format: L#L_#L#


    # Test 26- Check to see if the database throws an error if the postal code field is empty


    # Test 27- Check to see if the Gender field value is only : 'Male', 'Female', 'Unspecified'


    # Test 28- Check to see if the Home phone field is in the format: (###) ### - ####


    # Test 29- Check to see if the cell phone field is in the format: (###) ### - ####


    # Test 30- Check to see if the email field is in a valid email format


    # Test 31- Check to see if the database throws an error if the email field is empty


    # Test 32- member image


    # Test 33- Test to see if the hire date is in the format: DD/MM/YYYY


    # Test 34- Check to see if the database throws an error if the hire date field is empty


    # Test 35- Check to see if Job type is one of the following: 'Full-time ongoing', 'Full-time end dated',
        # 'Part-time ongoing', 'Part-time end dated'

    # Test 36- Check to see if the database throws an error if the job type is empty


    # Test 37 - check to see if the program name field accepts first with less than or equal to 30 characters in length


    # Test 38 - Check to see if the database throws an error if the program field is empty


    # Test 39- Check to see if the database throws an error if the program field is greater than 30


    # Test 40 - check to see if the campus name field accepts first with less than or equal to 20 characters in length


    # Test 41 - Check to see if the database throws an error if the campus field is empty


    # Test 42- Check to see if the database throws an error if the position field is greater than 20

