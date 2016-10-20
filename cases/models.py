from django.db import models
import sys
#import os.path

# Create your models here.


class Member(models.Model):
    memberID = models.IntegerField(max_length=9),
    firstName = models.CharField(max_length=20),
    lastName = models.CharField(max_length=30),

    def __str__(self):
        return self.firstName + " " + self.lastName

    def addmember(memberID):
        assert isinstance(memberID, Member)
        if sys.getsizeof(memberID) == 9:
            Case.members.append(memberID)
        else:
            ValueError("memberID must be 9 digits")
        Case.members.save()


class Case(models.Model):
    caseID = models.IntegerField(max_length=9),
    members = models.ForeignKey(Member, on_delete=models.CASCADE)



