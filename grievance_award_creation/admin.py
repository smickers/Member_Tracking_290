from django.contrib import admin
from models import GrievanceAward

#Registering GA so we can use it in the admin panel
admin.site.register(GrievanceAward)
