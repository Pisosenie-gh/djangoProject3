from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'j7f0yzi(eo9hgcs_ah=lczfy=-to%t+)c+mkwo&hir(k5m0&f7'


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
