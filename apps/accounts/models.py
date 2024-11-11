"""
Модели для приложения accounts
"""
import os

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


def validate_image(fieldfile_obj):
    """
    Функция валидации изображений
    :param fieldfile_obj: объект изображения
    :return: если объем изображенния > 2 MB возвращает ValidationError
    """
    filesize = fieldfile_obj.file.size
    if filesize > 2 * 1024 * 1024:
        raise ValidationError("Максимальный вес файла 2 MB")


def get_profile_avatar_path(instance: "Profile", filename: str) -> str:
    """
    Функция для определения пути сохранения файла для profile_avatar
    :param instance: Profile
    :param filename: имя файла
    :return: str: путь до файла profile_avatar
    """
    ext = os.path.splitext(filename)[1]
    return "avatars/{0}/{1}".format(instance.user.username, ext)


class CustomUser(AbstractUser):
    """
    Класс пользователя, предназначенный для аутентификации пользователя на ресурсе
    """

    class Meta:
        db_table = "auth_user"

    email = models.EmailField(
        unique=True,
    )


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    profile_nick_name = models.CharField(max_length=40, blank=True)
    profile_telephone_number = models.CharField(
        max_length=18,
        validators=[
            RegexValidator(
                r"^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$",
                message="Номер телефона должен быть в формате +7 (999) 999-99-99",
            )
        ],
    )

    profile_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_profile_avatar_path,
        validators=[validate_image],
    )

    def __str__(self):
        return f"Profile(user={self.user})"


"""
Модели для приложения private_messanger

"""


class ContactsBook(models.Model):
    """
    Класс Адресной книги пользователя
    """
    contacts_book_owner = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Contact(models.Model):
    """
    Класс записи в адресной книге
    """
    contact_profile = models.ForeignKey(Profile, related_name="contacts", on_delete=models.CASCADE)
    contact_book = models.ForeignKey(ContactsBook, related_name="contacts", on_delete=models.CASCADE)


class Message(models.Model):
    """
    Родительский класс для Сообщений
    """
    message_sender = models.ForeignKey(Profile, related_name="private_messages", on_delete=models.DO_NOTHING)
    message_text = models.CharField(max_length=255, blank=True)
    message_image = models.ImageField(
        null=True,
        blank=True,
    )
    message_time_stamp = models.DateTimeField(auto_now_add=True)


class PrivateMessage(Message):
    """
    Класс Личного сообщения, унаследован от Message
    """
    message_recipient = models.ForeignKey(Profile, related_name="private_messages", on_delete=models.DO_NOTHING)
    message_is_read = models.BooleanField(default=False)


"""
Модели для приложения Channel
"""


def validate_image(fieldfile_obj):
    """
    Функция валидации изображений
    :param fieldfile_obj: объект изображения
    :return: если объем изображенния > 2 MB возвращает ValidationError
    """
    filesize = fieldfile_obj.file.size
    if filesize > 2 * 1024 * 1024:
        raise ValidationError("Максимальный вес файла 2 MB")


def get_channel_avatar_path(instance: "Channel", filename: str) -> str:
    """
    Функция для определения пути сохранения файла для channel_avatar
    :param instance: Chanel
    :param filename: имя файла
    :return: str: путь до файла channel_avatar
    """
    ext = os.path.splitext(filename)[1]
    return "channels/{0}/{1}".format(instance.channel_owner.user.username, ext)


class Channel(models.Model):
    """
    Модель Канала пользователя
    """
    channel_name = models.CharField(max_length=200)
    channel_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_channel_avatar_path,
        validators=[validate_image],
    )
    channel_owner = models.ForeignKey(Profile, related_name="channels", on_delete=models.DO_NOTHING)
    channel_members = models.ManyToManyField(Profile, blank=True, related_name="channels")
    channel_admins = models.ManyToManyField(Profile, blank=True, related_name="channels")


class ChannelsMessage(Message):
    """
    Модель сообщения в Канале
    """
    message_channels = models.ForeignKey(Channel, related_name="messages", on_delete=models.DO_NOTHING)


"""
Модели для приложения Chat
"""


def validate_image(fieldfile_obj):
    """
    Функция валидации изображений
    :param fieldfile_obj: объект изображения
    :return: если объем изображенния > 2 MB возвращает ValidationError
    """
    filesize = fieldfile_obj.file.size
    if filesize > 2 * 1024 * 1024:
        raise ValidationError("Максимальный вес файла 2 MB")


def get_chat_avatar_path(instance: "Chat", filename: str) -> str:
    """
    Функция для определения пути сохранения файла для chat_avatar
    :param instance: Chat
    :param filename: имя файла
    :return: str: путь до файла chat_avatar
    """
    ext = os.path.splitext(filename)[1]
    return "chats/{0}/{1}".format(instance.chat_owner.user.username, ext)


class Chat(models.Model):
    """
    Модель Чата пользователя
    """
    chat_name = models.CharField(max_length=200)
    chat_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_channel_avatar_path,
        validators=[validate_image],
    )
    chat_owner = models.ForeignKey(Profile, related_name="chats", on_delete=models.DO_NOTHING)
    chat_members = models.ManyToManyField(Profile, blank=True, related_name="channels")


class ChatMessage(Message):
    """
    Модель сообщения в Чате
    """
    message_chats = models.ForeignKey(Channel, related_name="messages", on_delete=models.DO_NOTHING)


class HistoryDisplay(models.Model):
    """
    Модель для отображения истории сообщений в чате,
    при удалении истории пользователем регистрируется время,
    и от него отображается история
    """
    history_display_profile = models.ForeignKey(Profile, related_name="histories", on_delete=models.DO_NOTHING)
    history_display_chat = models.ForeignKey(Chat, related_name="histories", on_delete=models.DO_NOTHING)
    history_display_time = models.DateTimeField()
