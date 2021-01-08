import os
from .common import * # noqa


# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", "storages",) # noqa

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# http://django-storages.readthedocs.org/en/latest/index.html
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

# https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
# Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
# 86400 = (60 seconds x 60 minutes x 24 hours)
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
}

# Social
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# easy thumbnails lib & S3
THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'