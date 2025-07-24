


from django.urls import re_path # Use re_path for regex-based URL patterns
from . import consumers # Import the consumers we will create next

# Define WebSocket URL patterns
websocket_urlpatterns = [
    # This pattern matches WebSocket connections to ws://your-site.com/ws/echo/
    # It routes them to our EchoConsumer.as_asgi()
    re_path(r'ws/echo/$', consumers.EchoConsumer.as_asgi()),
]