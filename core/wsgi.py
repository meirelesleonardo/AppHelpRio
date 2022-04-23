"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
##from core.settings.base import CORE_DIR
#from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

application = get_wsgi_application()


#application = WhiteNoise(application, root=os.path.join(CORE_DIR, 'apps/static'))
#application.add_files("/path/to/more/static/files", prefix="more-files/")