"""
Потребитель для приложения chat
"""
import json
import logging

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.room_name = None
        self.room_group_name = None
        self.nick_name = None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.user = self.scope["user"]
        self.nick_name = await self.get_profile_name()
        self.room_group_name = f"chat_{self.room_name}"
        logger.info(
            f"Connection in room_name: {self.room_name}, room_group_name: {self.room_group_name}, profile: {self.nick_name}"
        )
        print(self.scope)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(
            f"text_data:{text_data}, text_data_json: {text_data_json},"
            f" message: {message}"
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": f"{message}"}
        )

    # Receive message from room group
    async def chat_message(self, event):
        """
        It is handler for chat.message in {"type": "chat.message", "message": message}
        """
        message = event["message"]
        message += message
        print(f"message: {message}")

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({"message": f"{self.nick_name}: {message}"})
        )

    @database_sync_to_async
    def get_profile_name(self):
        return self.user.profile.nick_name
