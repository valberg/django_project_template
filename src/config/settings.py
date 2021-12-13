from pathlib import Path

from environs import Env

env = Env()
env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / "project"

SECRET_KEY = env.str("SECRET_KEY", default="something-very-secret")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "debug_toolbar",
    "allauth",
    "allauth.account",
    "utils",
    "accounting",
    "membership",
]

DATABASES = {"default": env.dj_db_url("DATABASE_URL")}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

WSGI_APPLICATION = "project.wsgi.application"

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "da-dk"

TIME_ZONE = "Europe/Copenhagen"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [PROJECT_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static"

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"

EMAIL_BACKEND = env.str(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="")
# Parse email URLs, e.g. "smtp://"
email = env.dj_email_url("EMAIL_URL", default="smtp://")
EMAIL_HOST = email["EMAIL_HOST"]
EMAIL_PORT = email["EMAIL_PORT"]
EMAIL_HOST_PASSWORD = email["EMAIL_HOST_PASSWORD"]
EMAIL_HOST_USER = email["EMAIL_HOST_USER"]
EMAIL_USE_TLS = email["EMAIL_USE_TLS"]

# Always show DDT in development for any IP, not just 127.0.0.1 or
# settings.INTERNAL_IPS. This is useful in a docker setup where the
# requesting IP isn't static.
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _x: DEBUG,
}

# We store all translations in one location
LOCALE_PATHS = [PROJECT_DIR / "locale"]

# Allauth configuration
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False