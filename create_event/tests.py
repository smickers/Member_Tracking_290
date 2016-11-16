from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from models import Event
from django.db import DataError
import datetime

# Test 1 -