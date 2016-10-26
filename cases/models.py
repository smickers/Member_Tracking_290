from django.db import models
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
        CaseMembers.members.save()


class Case(models.Model):
    caseID  = models.CharField(max_length=9,unique='true')

    def addCase(caseID):
        assert isinstance(caseID, Case)
        if sys.getsizeof(caseID) == 9:
            CaseMembers.caseNum = caseID
        else:
            ValueError("caseID must be 9 digits")
        CaseMembers.caseNum.save

class CaseMembers(models.Model):
    caseNum = models.ForeignKey(Case, on_delete=models.CASCADE, to_field='caseID')
    memberNum = models.ForeignKey(Member, on_delete=models.CASCADE, to_field='memberID')

