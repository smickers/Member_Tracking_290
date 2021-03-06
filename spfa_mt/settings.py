"""
Django settings for helloworld project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECURE_SSL_REDIRECT = False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd!18#flrv@bnv#12)*$n#mup9=!k4rmn#4k!q*9q*kr#3#cl7s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['testserver', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'spfa_mt',
    'add_com.apps.AddComConfig',
    'award.apps.AwardConfig',
    'add_member.apps.AddMemberConfig',
    'meeting.apps.MeetingConfig',
    'add_case.apps.AddCaseConfig',
    'create_event.apps.CreateEventConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact_log.apps.ContactlogConfig',
    'bootstrap3',
    'haystack',
    'drf_haystack',
    'rest_framework',
    'grievance_award_creation.apps.GrievanceAwardCreationConfig',
    'url_filter',
    'django_filters',
    # 'django-easy-pdf',
    # 'inputstream',
    # 'wkhtmltopdf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spfa_mt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'spfa_mt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gamma',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'PASSWORD': 'bitnami',
        'USER': 'root',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }, 
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.DjangoFilterBackend',),
    'DEFAULT_RENDERER_CLASSES':(
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
DATE_FORMAT = 'j, N Y'
USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'files/'

# this will cause haystack to update its indexes in realtime
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


"""
THIS SECTION IS WHERE WE DEFINE
THE CONSTANTS TO BE UTILIZED BY OUR PROJECT
"""
FILE_EXT_TO_ACCEPT = ['xls', 'xlsx', 'pptx', 'docx', 'csv', 'pdf',
                      'txt', 'msg', 'ppt', 'png']
FILE_EXT_TO_ACCEPT_STR = ',.'.join(FILE_EXT_TO_ACCEPT)

MAX_FILE_SIZE = 524288000

MEDIA_ROOT = 'media/'

MEDIA_URL = '/media/'

FILE_UPLOAD_HANDLERS = ["file_handler.filehandler.UploadValidator",
                        "django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler"]

WKHTMLTOPDF_CMD = "C:/Python27/Lib/site-packages/wkhtmltopdf"