from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@xuqxjbnnew=e9@3g&8nhxp=ykvn9^^ne0qg1a@3s9*j3m6!#o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# site id
SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'dj_rest_auth',
    # 'dj_rest_auth.registration',
    
    # all auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # google Auth
    'allauth.socialaccount.providers.google',
    
    # github Auth
    'allauth.socialaccount.providers.github',
    
    # facebook Auth
    'allauth.socialaccount.providers.facebook',
    
    # Apple Auth
    'allauth.socialaccount.providers.apple',
    
    # Twitter / X
    # 'allauth.socialaccount.providers.twitter',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
    
]

ROOT_URLCONF = "All_Auth.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
#     )
# }

# REST_AUTH = {
#     'USE_JWT': True,
# }

# REST_AUTH = {
#     'JWT_AUTH_COOKIE': 'my-app-auth',
#     'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
# }

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "All_Auth.wsgi.application"

ACCOUNT_LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
LOGIN_REDIRECT_URL = "/"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'All_Auth/static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://cb54-119-155-3-23.ngrok-free.app']

"""Google"""
# client_ID = 113799018764-slrgqr9j42vsd7lsltvbtrrd75c1sh2p.apps.googleusercontent.com
# Client_Secret = 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

"""Github """
# Client_ID = 7c9c083e17a96a990223
# Client_Secret = cc9612e322e0a1a7e9eb181f6232d6aacc60fd5f

"""Facebook"""
# App_ID = 615302927467963
# App_Secrect = 65b4876393dd3d1bee5596bd4d230343

SOCIALACCOUNT_PROVIDERS = {
    # Google
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
    
    # Github
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
    
    # Facebook
    'facebook':{
        'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'], 
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False, 
        'VERSION': 'v2.4'
        },
    
    # Apple
    "apple": {
        "APP": {
            # Your service identifier (Bundle ID).
            "client_id": "com.makeyourplankapp",
            
            # The Key ID (visible in the "View Key Details" page).
            "secret": "SXMUJLRJD3",
            
             # Member ID/App ID Prefix -- you can find it below your name
             # at the top right corner of the page, or it’s your App ID
             # Prefix in your App ID.
            "key": "LFF95AFMZL",
            
            "settings": {
                # The private key you downloaded when generating the key.
                "certificate_key": """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQg8Kprz8FVbLXcP8jT
gDDFj4C9cur2sN/Fmn1ajR6QQYWgCgYIKoZIzj0DAQehRANCAARVLebLRtUYXVNO
lNTeb2/Iv1IpZYAqx8UrjAYRCPwxllyMjXPUJWuNnxTN5Uuic0nFNYSgvMdpR03P
rv0vCLKf
-----END PRIVATE KEY-----"""
            },
            
            'redirect_uri': ' https://cb54-119-155-3-23.ngrok-free.app/accounts/apple/login/callback/',
        }
    },
}