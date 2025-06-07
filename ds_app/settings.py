"""
Django settings for ds_app project.

Improved for production deployment on Render.
"""
import os
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DEBUG
# Set DEBUG=True locally by setting the DEBUG env var to "True".
DEBUG = os.getenv("DEBUG", "False") == "True"

# SECRET_KEY
# In production (DEBUG=False), require SECRET_KEY in env vars. In development, a default dev key is provided.
if DEBUG:
    SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")
else:
    try:
        SECRET_KEY = os.environ["SECRET_KEY"]
    except KeyError:
        raise ImproperlyConfigured("Missing SECRET_KEY environment variable!")

# ALLOWED_HOSTS
# Comma-separated list in the ALLOWED_HOSTS env var, or defaults covering Render and local
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "tradepharma-recursive.onrender.com,localhost,127.0.0.1"
).split(",")

# DATABASES
# Use Render's DATABASE_URL or fallback to local SQLite
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv(
            "DATABASE_URL",
            f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"
        ),
        conn_max_age=600,
    )
}

# Application definition
INSTALLED_APPS = [
    'ds_bot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'ds_app.urls'

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

WSGI_APPLICATION = 'ds_app.wsgi.application'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Third-party service keys (set these in Render Env Vars)
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Email configuration (example using SMTP; customize per provider)
EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend'
)
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 25))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False') == 'True'
