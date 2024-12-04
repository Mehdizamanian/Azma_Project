
"""
routing.py  is like the url.py in an app file in websocket
"""


from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer),
]