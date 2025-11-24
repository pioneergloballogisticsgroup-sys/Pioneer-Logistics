"""
Django settings for core project.
"""

from pathlib import Path
import os
import dj_database_url # 👈 NEW: Import for production database config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Quick-start development settings - unsuitable for production ---

# SECURITY WARNING: keep the secret key used in production secret!
# 🚨 IMPORTANT: You must set the SECRET_KEY as an Environment Variable on Render!
# The default insecure key is kept here for local testing fallback.
SECRET_KEY = 'django-insecure-je9#j-qd(xgt%$vtf)299*#l2_v(+=cn7(+swlr69p2#xhhe+k'

# SECURITY WARNING: don't run with debug turned on in production!
# 🚨 CHANGE 1: DEBUG must be False in production
DEBUG = False 

# 🚨 CHANGE 2: ALLOWED_HOSTS must list your domain and Render's domain
# Replace the placeholder Render URL below with the ACTUAL URL Render gives you (e.g., 'your-service.onrender.com')
ALLOWED_HOSTS = [
    'pioneergloballogistics.site', 
    'www.pioneergloballogistics.site',
    'pioneer-logistics-server.onrender.com' # 👈 Placeholder: Update this with your actual Render service URL
]

# CSRF_TRUSTED_ORIGINS is necessary for Render to proxy requests securely
CSRF_TRUSTED_ORIGINS = [
    'https://*.pioneergloballogistics.site',
    'https://*.onrender.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    # 🚨 CHANGE 3: WhiteNoise Middleware for serving static files efficiently
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
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
	'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# 🚨 CHANGE 4: Use PostgreSQL database URL from Render environment variable
DATABASES = {
    'default': dj_database_url.config(
        # Read DATABASE_URL environment variable (from Render)
        # Fall back to local SQLite if the variable isn't set
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600 
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# 🚨 CHANGE 5: Configure WhiteNoise storage for collected static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Tell WhiteNoise to use its efficient static file serving mechanism
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WHATSAPP_NUMBER = "19568109658"  # <-- change to your real WhatsApp number
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}"

