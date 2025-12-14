"""
Django settings for proyecto_principal project.
"""

from pathlib import Path

# ***************************************************************
# 1. PATH CONFIGURATION (Soluciona NameError: name 'BASE_DIR' is not defined)
# ***************************************************************

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Sube dos niveles para llegar a la carpeta 'primera-pagina'
BASE_DIR = Path(__file__).resolve().parent.parent


# ***************************************************************
# 2. SECURITY WARNING: keep the secret key used in production secret!
# ***************************************************************

# CAMBIAR ESTA CLAVE por una única y segura en producción
SECRET_KEY = 'django-insecure-tu_clave_secreta_aqui_para_el_proyecto-final'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ***************************************************************
# 3. APPLICATION DEFINITION
# ***************************************************************

INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'ckeditor',
    'ckeditor_uploader',

    # My apps
    'accounts',
    'blog',
    'mensajeria',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_principal.urls'


# ***************************************************************
# 4. TEMPLATES CONFIGURATION (Incluye la carpeta global 'templates')
# ***************************************************************

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Incluye la carpeta global 'templates' en la raíz del proyecto
        'DIRS': [BASE_DIR / 'templates'], 
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

WSGI_APPLICATION = 'proyecto_principal.wsgi.application'


# ***************************************************************
# 5. DATABASE CONFIGURATION
# ***************************************************************

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ***************************************************************
# 6. AUTHENTICATION (Redirecciones de login/logout)
# ***************************************************************
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login' # o 'home' si prefieres
LOGIN_URL = '/accounts/login/' # URL donde está el formulario de login


# ***************************************************************
# 7. PASSWORD VALIDATION
# ***************************************************************

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


# ***************************************************************
# 8. INTERNATIONALIZATION
# ***************************************************************

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ***************************************************************
# 9. STATIC & MEDIA FILES (Archivos CSS/JS e imágenes/archivos subidos)
# ***************************************************************

STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']  # Opcional, si usas carpeta static global

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CKEDITOR CONFIGURATION
CKEDITOR_UPLOAD_PATH = 'uploads/'


# ***************************************************************
# 10. DEFAULT PRIMARY KEY FIELD TYPE
# ***************************************************************

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'