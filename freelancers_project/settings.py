import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()  # This should be correctly loading the .env file

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = env.bool('DEBUG', default=False)  # Ensure DEBUG is False in production

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['deityomfreelancer.com', 'www.deityomfreelancer.com'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'freelancers_app',
    "crispy_forms",
    "crispy_bootstrap5"
]

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'freelancers_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'freelancers_project.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),  # Ensure this is correct; might need to be set to Hostinger DB host if not local
        'PORT': os.getenv('DB_PORT', default='5432'),  # Ensure the port is correct (default 5432 for PostgreSQL)
    }
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production, static files should be collected here

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication and User model
AUTH_USER_MODEL = 'freelancers_app.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings (for production)
SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS
SECURE_HSTS_SECONDS = 3600  # Enable HTTP Strict Transport Security
SECURE_HSTS_PRELOAD = True  # Enable preload for HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent sniffing of content types
SECURE_BROWSER_XSS_FILTER = True  # Enable the XSS filter
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS

# Ensure .env is in the correct directory and loaded
environ.Env.read_env(str(BASE_DIR / '.env'))  # Ensure .env is in the correct directory
