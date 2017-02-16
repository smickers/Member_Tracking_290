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
TYPE_CHOICES = {
    "GRIEVANCES - INDIVIDUAL": "GRIEVANCES - INDIVIDUAL",
    "GRIEVANCES - GROUP": "GRIEVANCES - GROUP",
    "GRIEVANCES - POLICY": "GRIEVANCES - POLICY",
    "GRIEVANCES - CLASSIFICATION": "GRIEVANCES - CLASSIFICATION",
    "GRIEVANCES - COMPLAINTS": "GRIEVANCES - COMPLAINTS",
    "DISABILITY CLAIMS": "DISABILITY CLAIMS",
    "ARBITRATION": "ARBITRATION",
    "COMPLAINT": "COMPLAINT"
}

# List of available statuses for a Case:
STATUS_CHOICES = {
    "OPEN": "OPEN",
    "CLOSED": "CLOSED",
    "PENDING": "PENDING",
    "ACTION REQ'D - MGMT": "ACTION REQ'D - MGMT",
    "ACTION REQ'D SPFA": "ACTION REQ'D SPFA"
}

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

CONTACT_LOG_STATUSES = {
    'E': 'Email',
    'F': 'Face to face',
    'P': 'Phone',
    'M': 'Meeting',
    'T': 'Text'
}

CONTACT_LOG_FILE_EXTENSIONS = [
    'mp3',
    'msg',
    'xlsx',
    'doc',
    'docx',
    'pdf'
]