from django.db import models
from django.core.urlresolvers import reverse
import sys


class Member(models.Model):
    memberID = models.CharField(max_length=9,unique='true')
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def  addmember(memberID):
        assert isinstance(memberID, Member)
        if sys.getsizeof(memberID) == 9:
            Case.members.append(memberID)
        else:
            ValueError("memberID must be 9 digits")
        CaseMembers.memberNum.save()

#Comment to hopefully detect changes
class Case(models.Model):
    caseID = models.CharField(max_length=9,unique='true')

    def addCase(caseID):
        assert isinstance(caseID, Case)
        if sys.getsizeof(caseID) == 9:
            CaseMembers.caseNum = caseID
        else:
            ValueError("caseID must be 9 digits")


class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.CharField(max_length=9)
    caseMember = models.CharField(max_length=18, unique='true', null='true')

    def save (self):
        self.caseMember = self.caseNum + self.memberNum
        super(CaseMembers, self).save()

    def get_absolute_url(self):
        return reverse(viewname='cases:addMemberToCase')