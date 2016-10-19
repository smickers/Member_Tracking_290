from django.test import TestCase
#from add_case.models import Case

#Test 1 - Campus validation
'''
The campus entered must match a campus from the DB.
    Saskatoon
    Prince Albert
    Regina
    Moose Jaw
If a different campus is entered, an exception is thrown. This will prevent someone changing the select
box to a textbox and entering their own value.
'''

#Test 2 - School validation
'''
The school entered must match a school from the DB.
    School of Animal and BioSciences
    School of Business
    School of Construction
    School of Health Sciences
    School of Hospitality and Tourism
    School of Human Services and Community Safety
    School of Information and Communications Technology
    School of Mining, Energy, and Manufacturing
    School of Natural Resources and Built Environment
    School of Nursing
    School of Transportation

If a different school is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 3 - Case type validation
'''
The case type entered must match a school from the DB.
    GRIEVANCES - INDIVIDUAL
    GRIEVANCES - GROUP
    GRIEVANCES - POLICY
    GRIEVANCES - CLASSIFICATION
    ARBITRATIONS
    COMPLAINTS
    DISABILITY CLAIMS

If a different case type is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 4 - Status validation
'''
The status entered must match a school from the DB.
    OPEN
    CLOSED
    PENDING
    ACTION REQ'D - MGMT
    ACTION REQ'D - SPFA

If a different status is entered, an exception is thrown. This will prevent someone from changing the
select box to a textbox and entering their own value.
'''

#Test 5 - Department/Program validation
'''
The status entered must match a school from the DB.


If a different department/program is entered, an exception is thrown. T
his will prevent someone from changing the select box to a textbox and entering their own value.
'''

#Test 6 - Start Date validation


#Test 7 - Default Status validation


#Test 8 - Default Start Date validation


#Test 9 - End date set when closing case


#Test 10 - Case created with correct attributes



