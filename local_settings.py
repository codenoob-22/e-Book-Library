import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'REGARGO',
        'USER': 'postgres',
        'PASSWORD': 'Smnssgsssc1!',
        'HOST': 'localhost'

    }
}

DEBUG = True