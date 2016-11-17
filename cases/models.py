from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.core.urlresolvers import reverse
from add_member.models import Person
import sys
from django.contrib import admin

class Member(models.Model):
    memberID = models.CharField(max_length=9, unique='true')
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def addmember(memberID):
        assert isinstance(memberID, Member)
        if sys.getsizeof(memberID) == 9:
            Case.members.append(memberID)
        else:
            ValueError("memberID must be 9 digits")
        CaseMembers.memberNum.do_save()


#Comment to hopefully detect changes
# noinspection PyMethodParameters
class Case(models.Model):
    caseID = models.CharField(max_length=9, unique='true')

    def addCase(caseID):
        assert isinstance(caseID, Case)
        if sys.getsizeof(caseID) == 9:
            CaseMembers.caseNum = caseID
        else:
            ValueError("caseID must be 9 digits")


# noinspection PyGlobalUndefined
class CaseMembers(models.Model):
    caseNum = models.CharField(max_length=9)
    memberNum = models.TextField()
    caseMember = models.CharField(max_length=18, unique='true', null='true', )

    def member_split(self):
        members = self.memberNum.split(',')
        print(members)
        for mem in members:
            tempCaseMem = CaseMembers(caseNum=self.caseNum, memberNum=mem,
                                      caseMember=self.caseNum + mem)
            tempCaseMem.save()

    # noinspection PyGlobalUndefined
    #Function: save
    #Purpose: Save the memberID and caseID to the caseMembers table
    #params: self - instance of CaseMembers
    def save(self):
        caseCheck = False
        memberCheck = True
        caseID = self.caseNum
        try:
            Case.objects.get(caseID=self.caseNum)
            caseCheck = True
        except ObjectDoesNotExist:
            print ("Case Does not exist")
        try:
            Person.objects.get(memberID=mem)
            memberCheck = True
        except Exception:
            print ("Member Does not exist")
        if memberCheck & caseCheck:
            caseMem.caseNum = caseID
            caseMem.memberNum = mem
            caseMem.caseMember = self.caseNum + mem
            caseMem.save()
            print("Member added to Case")

    #Function: get_absolute_url
    #Purpose: Reload the page when information is submited
    #Params: None
    @staticmethod
    def get_absolute_url():
        return reverse(viewname='cases:addMemberToCase')

    #cms = [save(mem) for mem in member_split()]


# class CaseMembersAdmin(admin.ModelAdmin):
#         def save_model(self, request, obj, form, change):
#                 data = obj.member
#
#                 caseMember = [x for x in data.split(', ') if x and not x.isspace()]
#                 for member in caseMember:
#                     CaseMembers.objects.create(caseMember=member, caseNum=CaseMembers.caseNum)