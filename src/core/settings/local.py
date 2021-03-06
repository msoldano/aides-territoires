import environ

from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE, TEMPLATES

DEBUG = True


TEMPLATES[0]['OPTIONS']['debug'] = True
TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, 'django.template.context_processors.debug')

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE


# Create a .env.local file in django's root
environ.Env.read_env('.env.local')
env = environ.Env()

SECRET_KEY = env('SECRET_KEY', default='hg_1)(oo53y2ow1bvlr6k2mv#hk1lo4%6qf1pdf*02%$203kmt')

DATABASES = {
    'default': env.db(
        default='psql://aidesterritoires:aidesterritoires@localhost/aidesterritoires')
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['aidesterritoires.local'])

INTERNAL_IPS = env.list('INTERNAL_IPS', default=['127.0.0.1'])

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = env.bool('COMPRESS_OFFLINE', False)

MAILING_LIST_LIST_ID = env('MAILING_LIST_LIST_ID')
MAILING_LIST_FORM_ACTION = env('MAILING_LIST_FORM_ACTION')

# Celery configuration
CELERY_BROKER_URL = "memory://"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
