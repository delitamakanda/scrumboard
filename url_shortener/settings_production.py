from url_shortener.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['.herokuapp', '*',]

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.environ.get('SMTP_PORT')
EMAIL_HOST_USER = os.environ.get('MAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MAIL_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = ''
EMAIL_TIMEOUT = 500
