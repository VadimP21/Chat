"""
Основная точка входа в приложение, содержит роуты приложения Chat
"""
from django.urls import path

from .views import Index, Room

app_name = "chat"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("<str:room_name>/", Room.as_view(), name="room"),
]
