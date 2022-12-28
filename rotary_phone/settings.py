from pathlib import Path
from os import getenv, path
from loguru import logger

from dotenv import load_dotenv
import dj_database_url
import django_redis

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = path.dirname(path.abspath(__file__))
dotenv_path = path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

SECRET_KEY = getenv("DJANGO_SECRET_KEY")

DEBUG = bool(getenv("DJANGO_DEBUG", "True") == "True")

DEFAULT_HOST = ["127.0.0.1"]
DJANGO_ALLOWED_HOST = getenv("DJANGO_ALLOWED_HOST", default="127.0.0.1").split(",")
ALLOWED_HOSTS = list(DEFAULT_HOST) + [
    host for host in DJANGO_ALLOWED_HOST if host not in DEFAULT_HOST
]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "django_celery_results",
    "crispy_forms",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework",
]

LOCAL_APPS = [
    "main.home.apps.HomeConfig",
    "main.authuser.apps.AuthuserConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rotary_phone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            path.join(BASE_DIR, "templates"),
            path.join(
                BASE_DIR,
                "templates",
                "base",
            ),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rotary_phone.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = getenv("DATABASE_URL")

DATABASES = dict()
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=False)
DATABASES["custom"] = dj_database_url.config(conn_max_age=600, ssl_require=False)

DATABASES["default"]["PASSWORD"] = getenv("DJANGO_DB_PASSWORD")
DATABASES["default"]["OPTIONS"] = {
    "options": f'-c search_path={getenv("DJANGO_SCHEMA_NAME")}'
}

DATABASES["custom"]["OPTIONS"] = {
    "options": f'-c search_path={getenv("DJANGO_CUSTOM_SCHEMA")}'
}
DATABASES["custom"]["PASSWORD"] = getenv("DJANGO_DB_PASSWORD")


CACHE_TTL = 60 * int(getenv("CACHE_TTL_SECS", 1500))
REDIS_CLIENT_CLASS = getenv("REDIS_CLIENT_CLASS")
REDIS_BACKEND = getenv("REDIS_BACKEND")

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = int(getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = getenv("REDIS_PASSWORD")
REDIS_USERNAME = getenv("REDIS_USERNAME", "default")
REDIS_KEY_PREFIX = getenv("DJANGO_PROJECT")
REDIS_DB = getenv("REDIS_DB", 1)

REDIS_LOCATION = (
    f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
)

logger.info(REDIS_LOCATION)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    path.join(BASE_DIR, "static"),
    "/var/www/static/",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, "media")

FILE_DIR = path.join(BASE_DIR, "files")
DATA_DIR = path.join(BASE_DIR, "data")
BACKUP_DIR = path.join(getenv("BACKUP_DIR", DATA_DIR), "backup")

DJANGO_SU_EMAIL = getenv("DJANGO_SU_EMAIL")
DJANGO_SU_NAME = getenv("DJANGO_SU_NAME")
DJANGO_PORT = getenv("DJANGO_PORT", 8000)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth model
AUTH_USER_ALLOW_SIGNUP = True
AUTH_USER_MODEL = "authuser.User"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# login
LOGIN_REDIRECT_URL = "home:home_list_view"
LOGOUT_REDIRECT_URL = "/login"

CSRF_COOKIE_SECURE = True

# SLASH

APPEND_SLASH = False

# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # General
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    # Pagination
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": int(getenv("DJANGO_PAGINATION_LIMIT", 10)),
    # Render
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    # Permission/Authentication
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # Throttling
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "100000/day"},
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Rotary Phone API",
    "DESCRIPTION": "Timepass project on django",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}


TASK_DEFAULT_QUEUE = getenv("TASK_DEFAULT_QUEUE", "na")
