"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_asgi_application()


################### Chapter XVII topic 17.5: Forging the Real-time Link: Routing WebSockets and Creating Consumers ##################


import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import myapp.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
http_application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": http_application, 
    "websocket": AuthMiddlewareStack( 
        URLRouter(
            myapp.routing.websocket_urlpatterns 
        )
    ),
})
