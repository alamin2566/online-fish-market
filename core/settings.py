from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv() 

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ------- COMMON CODE FOR HANDLE MEDA, STATIC and TEMPLATES ---------

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')

STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR , 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [STATIC_DIR, ]


MEDIA_DIR = os.path.join(BASE_DIR , 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


#  --------------------------==========-------------------------------

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',

    'django_filters',
    'apps.users',
    'apps.adminpanel',
    'apps.market',
    'apps.payment',
    # 'rest_framework',
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

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'


pghost = os.getenv('PGHOST')
if not pghost:
    print("PGHOST environment variable is not set. Please set it in your .env file.")
pgport = os.getenv('PGPORT')
if not pgport:
    print("PGPORT environment variable is not set. Please set it in your .env file.")
pgdatabase = os.getenv('PGDATABASE')
if not pgdatabase:
    print("PGDATABASE environment variable is not set. Please set it in your .env file.")
pguser = os.getenv('PGUSER')
if not pguser:
    print("PGUSER environment variable is not set. Please set it in your .env file.")
pgpassword = os.getenv('PGPASSWORD')
if not pgpassword:
    print("PGPASSWORD environment variable is not set. Please set it in your .env file.")


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': f"{pghost}",
    'PORT': f"{pgport}",
    'NAME': f"{pgdatabase}",
    'USER': f"{pguser}",
    'PASSWORD': f"{pgpassword}",
    'OPTIONS': {'sslmode': 'require'},
  }
}


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

# --=====> EXTRA <=====------


AUTH_USER_MODEL = 'users.User'
LOGIN_URL = "/auth/login/"
# ------======== ------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ================ CLOUDINARY SETTINGS ================

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'