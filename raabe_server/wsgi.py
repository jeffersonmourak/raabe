"""
WSGI config for raabe_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import local

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

dev = True

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raabe_server.settings")
if not dev:
	application = Cling(get_wsgi_application())

else:
	application = get_wsgi_application()
