# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
import os

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../'))
STATIC_ROOT_DIR = os.environ.get('STATIC_ROOT_DIR', PROJECT_ROOT_DIR)
STATIC_URL = '/assets/static/'

STATIC_ROOT = os.path.join(STATIC_ROOT_DIR, 'assets', 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT_DIR, 'assets', 'media')

AVAILABLE_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'InActive'),
    ('archived', 'Archived'),
)


