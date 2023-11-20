from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(
        r"ws/chat/(?P<room_name>\w+)/(?P<profile_name>\w+)/$",
        ChatConsumer.as_asgi(),
        name="chat_consumer",
    )
    # re_path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi(), name="chat_consumer")
]
