"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xt5qf9u6le9jv%orea!s*5(fv(gyj1$0eu3=e6by#glzmp8xd$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = [('Admin1', 'test_user_python@mail.ru')]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
         'simple': {
            'format': '{levelname} {asctime} {message}'
        },
         'verbose1': {
            'format': '{levelname} {asctime} {pathname} {message}',
        },
        'verbose2': {
            'format': '{levelname} {asctime} {pathname} {exc_info} {message}'
        },
        'verbose3': {
            'format': '{levelname} {asctime} {module}  {message}'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'general.log': {
            'level': 'INFO',
            'formatter': 'verbose3',
            'filters': ['require_debug_false']
        },
        'errors.log': {
            'level': 'ERROR', 'CRITICAL'
            'formatter': 'verbose2'
        },
        'security.log': {
            'formatter': 'verbose3'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbouse1'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'general.log'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors.log'],
            'level': 'ERROR', 'CRITICAL'
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors.log'],
            'level': 'ERROR', 'CRITICAL'
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors.log'],
            'level': 'ERROR', 'CRITICAL'
            'propagate': False,
        },
        'django.db_backends': {
             'handlers': ['errors.log'],
            'level': 'ERROR', 'CRITICAL'
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security.log'],

        }
    }
}

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.templatetags',
    'django_filters',
    'django_apscheduler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'protect',
    'news.apps.NewsConfig',
]
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # ??????????????????, ???????? ?????????? ?????????????????? ???????????????????? ??????????! ???? ???????????????? ?????????????? ?????????? cache_files ???????????? ?????????? ?? manage.py!
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]



ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_FORMS = {'signup': 'news.forms.CommonSignupForm'}


WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


EMAIL_HOST = 'smtp.mail.ru' # ?????????? ?????????????? ????????????-?????????? ?????? ???????? ???????? ?? ?????? ????
EMAIL_PORT = 465 # ???????? smtp ?????????????? ???????? ????????????????????
EMAIL_HOST_USER = 'test_user_python' # ???????? ?????? ????????????????????????, ???????????????? ???????? ???????? ?????????? user@yandex.ru, ???? ???????? ???????? ???????????? user, ?????????? ??????????????, ?????? ?????? ???? ?????? ???????? ???? ????????????
EMAIL_HOST_PASSWORD = 'nottoday404' # ???????????? ???? ??????????
EMAIL_USE_SSL = True # ???????????? ???????????????????? ssl, ?????????????????? ?? ??????, ?????? ??????, ?????????????????? ???? ??????????????????, ???? ???????????????? ?????? ?????????? ??????????????????????
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@mail.ru'


