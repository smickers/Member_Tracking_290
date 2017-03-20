from django.test import TestCase
from .models import Person
from .models import contactLog


# Test to implement contact logs to a member's details page
class TestImplementCLsToMemberDetails(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestImplementCLsToMemberDetails, self).__init__(*args, **kwargs)
        self.dw = Person()
        self.kk = Person()
        self.ww = Person()
        self.cl_1 = contactLog
