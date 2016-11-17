from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import Event
from django.db import DataError
import datetime

# Test 1 - Validate event name, empty name
# Input: ""
# Expected result: error thrown explaining event name is required

# Test 2 - Validate event name, valid name
# Input: "A"
# Expected result: Event created and added to DB

# Test 3 - Validate event name, name 20 characters
# Input: "01234567890126459789"
# Expected result: Event created and added to DB

# Test 4 - Validate event name, name 21 characters
# Input: "012345678901234567890"
# Expected result: Error thrown explaining event name limited to 20 characters

# Test 5 - Validate event description, desc 50 characters
# Input: "01234567890123456789012345678901234567890123456789"
# Expected result: Event created and added to DB

# Test 6 - Validate event description, desc 51 characters
# Input: "012345678901234567890123456789012345678901234567890"
# Expected result: Error thrown explaining event description is limited to 50 characters

# Test 7 - Validate event description, empty desc
# Input: ""
# Expected result: Event created and added to DB

# Test 8 - Validate event date, valid date
# Input: "2016-11-17"
# Expected result: Event created and added to DB

# Test 9 - Validate event date, invalid date
# Input: "2016-11-35"
# Expected result: Error thrown explaining a valid date must be entered

# Test 10 - Validate event date, invalid date v2
# Input: 'this is invalid'
# Expected result: Error thrown explaining a valid date must be entered

# Test 11 - Validate valid event location
# Input "HONALULU"
# Expected result: Event is created and added to DB

# Test 12 - Validate valid event location v2
# Input: "REGINA"
# Expected result: Event is created and added to DB

# Test 13: Validate an invalid event location
# Input: "this city name is way too long"
# Expected result: Error thrown explaining event location is too long

# Test 14 - Validate an invalid event location v2
# Input: ""
# Expected result: Error thrown explaining event location cannot be left empty.
