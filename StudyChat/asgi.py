import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudyChat.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle traditional HTTP requests
    "websocket": AuthMiddlewareStack(  # Handle WebSocket connections
        URLRouter(
            routing.websocket_urlpatterns  # Use the routing configuration we will set up later
        )
    ),
})
