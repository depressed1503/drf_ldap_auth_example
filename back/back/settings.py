import os
from pathlib import Path
from dotenv import load_dotenv
import ldap
from django_auth_ldap.config import LDAPSearch


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-rpb$5)o^d1tqa7p+b33i+yy$5hjjg)f!za6d1&4p3u=r0ghg+9'
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = os.environ.get("DEBUG", 'True').lower() in ('true', '1', 't',)
HOST = os.environ.get("HOST", "acc-sechenov.ru")

DEBUG = True

ALLOWED_HOSTS = [
	'127.0.0.1',
	'localhost',
	HOST,
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'api',
	'rest_framework',
	'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'back.wsgi.application'

if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
	}
else:
	DATABASES = {
		"default": {
			"ENGINE": "django.db.backends.postgresql",
			"NAME": os.environ.get("DATABASE_NAME", "mydatabase"),
			"USER": os.environ.get("DATABASE_USER", "myuser"),
			"PASSWORD": os.environ.get("DATABASE_PASSWORD", "mypassword"),
			"HOST": os.environ.get("DATABASE_HOST", "localhost"),
			"PORT": os.environ.get("DATABASE_PORT", 5432),
		}
	}

AUTH_USER_MODEL = 'api.CustomUser'

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


MEDIA_URL = "/media/"
MEDIA_ROOT = "media/" if DEBUG else "/vol/media/"
STATIC_URL = "/api_static/"
STATIC_ROOT = "static/" if DEBUG else "/vol/static/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

if not DEBUG:
	SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = not DEBUG

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_HEADERS = ['X-CSRFToken', 'Content-Type', 'Authorization']
CORS_EXPOSE_HEADERS = ['X-CSRFToken']

# CSRF Settings
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_HTTPONLY = False  # Recommended for security
CSRF_COOKIE_DOMAIN = None if DEBUG else HOST
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SAMESITE = 'None'

# Session Settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_DOMAIN = None if DEBUG else HOST

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
	f'https://{HOST}',
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
	f'https://{HOST}',
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
        }
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} ({levelname})- {name}- {message}",
            "style": "{",
        }
    },
}


# LDAP settings
AUTHENTICATION_BACKENDS = [
    "api.backends.CustomLDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_LDAP_SERVER_URI = "ldap://localhost:1389"

AUTH_LDAP_BIND_DN = "admin"
AUTH_LDAP_BIND_PASSWORD = "adminpassword"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=users,dc=example,dc=org", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"
)
AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s,ou=users,dc=example,dc=org"
