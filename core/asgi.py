import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from echo import routing as echo_routing



#Wsgi
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()



#AsGI used for websocket
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket':AuthMiddlewareStack(
      URLRouter(
        echo_routing.websocket_urlpatterns
      )

    )
    
})