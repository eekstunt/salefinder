"""
Django settings for salefinder_development project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%blqk%9cavb6@$x3ifl6u^qpa!0sy%1j#=-i^r@+)0!$$!2!$$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['206.189.215.12', 'salefinder.ddns.net', 'localhost']
# ALLOWED_HOSTS = ['LvadislavDevelopment.pythonanywhere.com']
# SECURE_SSL_REDIRECT = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dynamic_preferences',
    'django.contrib.sites',
    'preferences',
    'admin_reorder',

    'bot',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'salefinder_development.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'dynamic_preferences.processors.global_preferences',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'salefinder_development.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'db',
#        'USER': 'god',
#        'PASSWORD': 'digitalocean',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'


DYNAMIC_PREFERENCES = {
    # a python attribute that will be added to model instances with preferences
    # override this if the default collide with one of your models attributes/fields
    'MANAGER_ATTRIBUTE': 'preferences',

    'REGISTRY_MODULE': 'dynamic_preferences_registry',

    # Allow quick editing of preferences directly in admin list view
    # WARNING: enabling this feature can cause data corruption if multiple users
    # use the same list view at the same time, see https://code.djangoproject.com/ticket/11313
    'ADMIN_ENABLE_CHANGELIST_FORM': True,

    # Customize how you can access preferences from managers. The default is to
    # separate sections and keys with two underscores. This is probably not a settings you'll
    # want to change, but it's here just in case
    'SECTION_KEY_SEPARATOR': '__',

    # Use this to disable caching of preference. This can be useful to debug things
    'ENABLE_CACHE': False,

    # Use this to disable checking preferences names. This can be useful to debug things
    'VALIDATE_NAMES': True,
}


ADMIN_REORDER = (
    {
        'app': 'bot',
        'label': 'Информация',
        'models': (
            'bot.BotUser',
            'bot.Statistics'
        )
    },

    {
        'app': 'bot',
        'label': 'Посты',
        'models': (
            'bot.PostponedPost',
            'bot.Draft'
        )
    },

    {
        'app': 'dynamic_preferences',
        'label': 'Настройки',
        'models': (
            {
                'model': 'dynamic_preferences.GlobalPreferenceModel',
                'label': 'Тексты и цена премиума'
            },
            {
                'model': 'bot.Staff',
                'label': 'Сотрудники'
            }
        )
    },

    {
        'app': 'bot',
        'label': 'Поддержка',
        'models': (
            {
                'model': 'bot.FeedbackDialogue',
                'label': 'Список диалогов'
            },
        )
    }

    # # Keep original label and models
    # 'sites',

    # # Rename app
    # {'app': 'auth', 'label': 'Authorisation'},

    # # Reorder app models
    # {'app': 'auth', 'models': ('auth.User', 'auth.Group')},

    # # Exclude models
    # {'app': 'auth', 'models': ('auth.User', )},

    # # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},

    # # models with custom name
    # {'app': 'auth', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
)


BOT_TOKEN = '610861789:AAENhJSeznde-u6YVSTMYjfJdMfUXp_H7d8'
PROVIDER_TOKEN = '390540012:LIVE:4393'

MIN_MAN_SIZE, MAX_MAN_SIZE = 38, 48
MIN_WOMAN_SIZE, MAX_WOMAN_SIZE = 36, 44

ADMIN = 'admin'

SETTINGS_EXPORT = [
    'MIN_MAN_SIZE', 'MAX_MAN_SIZE',
    'MIN_WOMAN_SIZE', 'MAX_WOMAN_SIZE'
]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
