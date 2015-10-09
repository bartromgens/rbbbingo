"""
Django settings for the hebikwindmee project

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from website.local_settings import *
except ImportError as e:
    if "local_settings" not in str(e):
        print("settings error")
        raise e

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3', #bootstrap3 see: https://github.com/dyve/django-bootstrap3
    'website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

##############
# Bootstrap3 #
##############

BOOTSTRAP3 = {
    'jquery_url': 'http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js', #'//code.jquery.com/jquery.min.js',
    'base_url': STATIC_URL + 'website/bootstrap/', #'//netdna.bootstrapcdn.com/bootstrap/3.0.3/'
    'css_url': STATIC_URL + 'website/bootstrap/css/bootstrap_flatly.min.css',
    'theme_url': None,
    'javascript_url': STATIC_URL + 'website/bootstrap/js/bootstrap.min.js',
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
}