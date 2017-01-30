from django.contrib import admin
from .models import *
# Register your models here.

#Registering meeting so we can use it in the admin panel
admin.site.register(Meeting)
