# """
# WSGI config for mysite project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_wsgi_application()


####################### deploy ###########################

import os

from django.core.wsgi import get_wsgi_application

# Import settings to access STATIC_ROOT
from django.conf import settings # <--- ADD THIS LINE

# Import WhiteNoise
from whitenoise import WhiteNoise # <--- CHANGE THIS IMPORT (from whitenoise.middleware to whitenoise)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# NEW: Configure WhiteNoise to serve static files from STATIC_ROOT
application = WhiteNoise(application, root=settings.STATIC_ROOT) # <--- CHANGE THIS LINE
# Optional: If you want to enable compression and caching (recommended for production)
# application.add_files(settings.STATIC_ROOT, prefix='static/') # This is often handled by CompressedManifestStaticFilesStorage