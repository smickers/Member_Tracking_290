from django.contrib import admin
from models import EducationAward

#Registering GA so we can use it in the admin panel
admin.site.register(EducationAward)
