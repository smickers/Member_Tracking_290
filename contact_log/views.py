# SPFA MT CST Project
# November 7, 2016
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import contactLog, ContactLogFile, contactLogFileCounter
from .forms import ContactLogForm
from django.shortcuts import render

# View ContactLogCreate
# Purpose: Put together a form to allow the user to create a new
# contact log from.
class ContactLogCreate(CreateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogEdit(UpdateView):
    model = contactLog
    form_class = ContactLogForm

class ContactLogList(ListView):
    model = contactLog

def contactLogDetail(request, pk):
    cl = contactLog.objects.get(id=pk)
    print "Contact Log: " + cl.__str__()
    manager = contactLogFileCounter()
    try:
        #cl.file_name = "testing"
        print("Reading file [0]!")
        relatedFile = manager.get_files(cl.pk)
        print("Reading file!")
        #cl.file_name = file.fileName
        #cl.file_name = "Some junk"
        cl.file_name = relatedFile
        # if the grievance award has no files associated, empty the fields and dont display the html
    except:
        cl.file_name = "hello world"
        cl.file_desc = ""
        #cl.file_date_uploaded = ""

    return render(request, 'contact_log/contactlog_edit.html', {'object' : cl})