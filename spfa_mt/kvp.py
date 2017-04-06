from datetime import date

# These are the key value pairs to be used my many different classes
# Non-School Departments @ Sask Polytech:
DEPARTMENT_CHOICES = {
    "Learning Technologies": "Learning Technologies",
    "ILDC": "ILDC",
    "Library": "Library",
    "PLAR": "PLAR",
    "Simulation Lab": "Simulation Lab",
    "Student Development": "Student Development",
    "Learning Services": "Learning Services",
    "Fitness Centre": "Fitness Centre"
}

# Sask Polytech Campuses:
CAMPUS_CHOICES = {
    'Saskatoon': 'Saskatoon',
    'Regina': 'Regina',
    'MJ': 'Moose Jaw',
    'PA': 'Prince Albert',
}

# Type of Case:
#   https://docs.djangoproject.com/en/1.10/ref/models/fields/
TYPE_CHOICES = (
    (7, "GRIEVANCES - INDIVIDUAL"),
    (6, "GRIEVANCES - GROUP"),
    (5, "GRIEVANCES - POLICY"),
    (4, "GRIEVANCES - CLASSIFICATION"),
    (3, "GRIEVANCES - COMPLAINTS"),
    (2, "DISABILITY CLAIMS"),
    (1, "ARBITRATION"),
    (0, "COMPLAINT")
)

# List of available statuses for a Case:
STATUS_CHOICES = (
        ("OPEN", "OPEN"),
        ("CLOSED", "CLOSED"),
        ("PENDING", "PENDING"),
        ("ACTION REQ'D - MGMT", "ACTION REQ'D - MGMT"),
        ("ACTION REQ'D SPFA", "ACTION REQ'D SPFA")
)

# Options for schools for each campus:
SCHOOL_CHOICES = {
    "School of Business": "School of Business",
    "School of Construction": "School of Construction",
    "School of Health Sciences": "School of Health Sciences",
    "School of Human Services and Community Safety": "School of Human Services and Community Safety",
    "School of Information and Communications Technology": "School of Information and Communications Technology",
    "School of Mining, Energy and Manufacturing": "School of Mining, Energy and Manufacturing",
    "School of Natural Resources and Built Environment": "School of Natural Resources and Built Environment",
    "School of Nursing": "School of Nursing",
    "School of Transportation": "School of Transportation",
    "Other": "Other",
}

# Define months so they're entered as three letters:
MONTHS = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

# bound field choices for STATUS field
INACTIVE = 0
ACTIVE = 1
# The status choices for a committee
COM_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

# Educational Award Types
EDU_AWARD_TYPES = [
    ('Internal', 'Internal'),
    ('External', 'External')
]

EDU_YEAR_CHOICES = [(r, r) for r in range(1980, date.today().year + 1)]
# Reversing the list so that the latest year is shown first
EDU_YEAR_CHOICES.reverse()

CONTACT_LOG_STATUSES = (('E', 'Email'),
                        ('F', 'Face to face'),
                        ('P', 'Phone'),
                        ('M', 'Meeting'),
                        ('T', 'Text'))
GENDER_CHOICE = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('UNDEFINED', 'Undefined'),
]

# bound fields choices for campus field
CAMPUS_CHOICE = [
    ('SASKATOON', 'SASKATOON'),
    ('REGINA', 'REGINA'),
    ('MOOSEJAW', 'MOOSE JAW'),
    ('PA', 'PRINCE ALBERT'),
]

# bound fields choices for position field
POSITION_CLASS_CHOICE = [
    ('FTO', 'Full-time ongoing'),
    ('FTED', 'Full-time end dated'),
    ('PTO', 'Part-time ongoing'),
    ('PTED', 'Part-time end dated'),
]

# bound fields choices for membership status field
MEMBERSHIP_STATUS = [
    ('RESOURCE', 'RESOURCE'),
    ('COMCHAIR', 'COMMITTEE CHAIR'),
    ('RECORDER', 'RECORDER'),
]

EMPLOYEE_STATUS = [
    ('A', 'ACTIVE'),
    ('T', 'TERMINATED'),
]

# CONTACT_LOG_FILE_EXTENSIONS = [
#     'mp3',
#     'msg',
#     'xlsx',
#     'doc',
#     'docx',
#     'pdf',
#     'txt'
# ]

SERVER_URL = '127.0.0.1:8000'