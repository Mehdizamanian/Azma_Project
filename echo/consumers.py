"""
consumers.py  is like the views.py in an app file in websocket
"""

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

  def connect(self):
     self.accept()

  def receive(self, text_data):
    self.send(text_data=text_data+"sent by server")

  def disconnect(self, close_code):
    pass