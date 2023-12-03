"""
Формы для приложения accounts
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
)

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Форма для создания CustomUser
    """

    class Meta:
        model = User
        fields = ("username",)
