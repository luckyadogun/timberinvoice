from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS_DEV'), 
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
