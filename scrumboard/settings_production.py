import os

from scrumboard.settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = config('DEBUG', cast=bool)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# STATIC_ROOT = 'static'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = config('SMTP_PORT')
# EMAIL_HOST_USER = config('MAIL_USERNAME')
# EMAIL_HOST_PASSWORD = config('MAIL_PASSWORD')
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_TIMEOUT = 500

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
