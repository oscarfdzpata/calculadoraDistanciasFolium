"""
WSGI config for geoLocalizacion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#original
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoLocalizacion.settings')
#local
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoLocalizacion.local')
#Produccion
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoLocalizacion.production')

#application = get_wsgi_application()  #lo comentamos para que sirvan los staticos el dj-static
from dj_static import  Cling
application = Cling(get_wsgi_application())

