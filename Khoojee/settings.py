"""
Django settings for Khoojee project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

import dj_database_url
import django_heroku
import dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV_FILE = os.path.join(BASE_DIR, ".env")

# Adding environment file for handling env variables for keys, location and other information
if os.path.isfile(DOTENV_FILE):
    dotenv.load_dotenv(DOTENV_FILE)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

if 'ON_HEROKU' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
else:

    SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'ON_HEROKU' in os.environ:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'Khoojee.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Khoojee.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Database
DATABASES = {'default': {}}

if 'ON_HEROKU' in os.environ:
    DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))
else:
    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USERNAME"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),

        }

    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# REDIS related settings
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

# for Heroku
CELERY_BROKER_URL = os.environ.get('REDISCLOUD_URL', 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0')
CELERY_RESULT_BACKEND = os.environ.get('REDISCLOUD_URL', 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0')

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

if 'ON_HEROKU' in os.environ:

    django_heroku.settings(locals())
    SERVER_ONE = str(os.environ['SERVER_ONE'])
    PROXY_SERVER = str(os.environ['PROXY_SERVER'])
    SERVER_TWO = str(os.environ['SERVER_TWO'])
    SERVER_THREE = str(os.environ['SERVER_THREE'])
    SERVER_FOUR = str(os.environ['SERVER_FOUR'])

else:
    SERVER_ONE = os.getenv("SERVER_ONE")
    PROXY_SERVER = os.getenv("PROXY_SERVER")
    SERVER_TWO = os.getenv("SERVER_TWO")
    SERVER_THREE = os.getenv("SERVER_THREE")
    SERVER_FOUR = os.getenv("SERVER_FOUR")
