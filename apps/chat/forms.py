"""
Формы для приложения chat
"""
from django import forms


class IndexForm(forms.Form):
    """
    Форма для создания комнаты и задания ника для пользователя
    """

    room_name = forms.CharField(max_length=40)
    nick_name = forms.CharField(max_length=40)
