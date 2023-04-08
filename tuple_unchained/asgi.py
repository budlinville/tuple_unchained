"""
Asynchronous Server Gateway Interface
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuple_unchained.settings')

application = get_asgi_application()
