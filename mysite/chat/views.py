import logging

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from chat.forms import IndexForm

logger = logging.getLogger(__name__)


class Index(View):
    """

    """
    def get(self, request):
        logger.info("Index_get")
        if not request.user.is_authenticated:
            return render(request, "accounts/registration.html")
        nick_name = request.user.profile.nick_name
        return render(request, "chat/index.html", {"nick_name": nick_name})

    def post(self, request):
        logger.info("Index_post")
        index_form = IndexForm(request.POST)
        if index_form.is_valid():
            nick_name = index_form.cleaned_data["nick_name"]
            room_name = index_form.cleaned_data["room_name"]
            current_user = request.user
            current_user.profile.nick_name = nick_name
            current_user.profile.save()
            return render(
                request,
                "chat/room.html",
                {
                    "room_name": room_name,
                },
            )
        return render(
            request,
            "chat/index.html",
        )


class Room(View):
    def get(self, request, room_name):
        logger.info(f"Room_get with {room_name} ")
        return render(
            request,
            "chat/room.html",
            {
                "room_name": room_name,
            },
        )

    def post(self, request, room_name):
        message = request.POST.get('message', None)
        if message:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'chat_{room_name}',
                {
                    'type': 'chat.message',
                    'message': message
                }
            )
            return HttpResponse('Message sent')
        return HttpResponse('Message not sent')

