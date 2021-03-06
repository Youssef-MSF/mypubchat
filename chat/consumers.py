# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
import requests


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print("Room name: ", self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        print("channel_name = : ", self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        image = text_data_json['image']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'image': image
            }
        )

        # Save the message in the db
        if message != "":
            requests.get(url='http://localhost:8080/LinkedClubs/HandleMessages?image=' + image + "&message=" + message)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        image = event['image']

        print("message: ", message)
        print("image: ", image)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'image': image
        }))
