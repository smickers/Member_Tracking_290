from django.db  import models



class ContactLog(models.Model):
    memberID = models.IntegerField(),
    date = models.DateTimeField(),
    description = models.TextField(max_length=150)



