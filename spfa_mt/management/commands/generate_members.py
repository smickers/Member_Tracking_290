from django.core.management.base import BaseCommand, CommandError
from add_member.models import Person as Member
import names
from random import randint

class Command(BaseCommand):
    """
        This will generate random members
        To run this command type:
            python manage.py generate_members
    """
    help = 'Creates dummy person to the db'

    def handle(self, *args, **options):
        for i in range(0, 100):
            tempPerson = Member()
            tempPerson.memberID = randint(111111111, 999999999)
            tempPerson.firstName = names.get_first_name(gender='female')
            tempPerson.middleName = names.get_last_name()
            tempPerson.lastName = names.get_last_name()
            tempPerson.socNum = randint(111111111, 999999999)
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
