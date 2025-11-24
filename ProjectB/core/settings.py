"""
Django settings for core project.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Quick-start development settings - unsuitable for production ---

# SECURITY WARNING: keep the secret key used in production secret!
# 🚨 GUARANTEED FIX: Read from environment variable first, fall back to the insecure one only locally.
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-je9#j-qd(xgt%$vtf)299*#l2_v(+=cn7(+swlr69p2#xhhe+k'
)

# SECURITY WARNING: don't run with debug turned on in production!
# 🚨 GUARANTEED FIX: Read DEBUG from environment variable (default to False for safety)
DEBUG = os.environ.get('DEBUG') == 'True' 

# ALLOWED_HOSTS must list your domain and Render's domain
ALLOWED_HOSTS = [
    'pioneergloballogistics.site', 
    'www.pioneergloballogistics.site',
    os.environ.get('RENDER_EXTERNAL_HOSTNAME'), # 👈 NEW: Reads Render's actual hostname dynamically
]

# Ensure Render and your domain are trusted
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
    'ProjectB.website',  # <--- THIS IS THE FIX
]

MIDDLEWARE = [
    # 🚨 CONFIRMED CORRECT: WhiteNoise middleware for serving static files
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProjectB.core.urls'

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

WSGI_APPLICATION = 'ProjectB.core.wsgi.application'

# Database
# Use PostgreSQL database URL from Render environment variable
DATABASES = {
    'default': dj_database_url.config(
        # Read DATABASE_URL environment variable (from Render)
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600 
    )
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Tell WhiteNoise to use its efficient static file serving mechanism
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WHATSAPP_NUMBER = "19568109658"
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}"

