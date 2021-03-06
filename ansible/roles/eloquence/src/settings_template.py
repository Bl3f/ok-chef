from pourparler.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
            "eloquence.blef.fr",
            "eloquence.udtq.fr", 
        ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/pourparler.sqlite3'),
    }
}

INSTALLED_APPS += [
                'website',
        ]

STATIC_ROOT = '/static'
MEDIA_DIR = "/media/"
MEDIA_ROOT = "/media/"
MEDIA_URL = "img/"
