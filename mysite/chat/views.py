import logging

from django.shortcuts import render
from django.views import View

logger = logging.getLogger(__name__)


class Index(View):
    def get(self, request):
        logger.info("Index_get")
        return render(request, "chat/index.html", {"profile_name": "Den ROB"})

    def post(self, request, room_name):
        logger.info("Index_post")

        return render(
            request,
            "chat/room.html",
            {
                "room_name": room_name,
            },
        )


class Room(View):
    def get(self, request, room_name, profile_name):
        logger.info(f"Room_get with {room_name}, {profile_name}")
        return render(
            request,
            "chat/room.html",
            {
                "room_name": room_name,
                "profile_name": profile_name,
            },
        )
