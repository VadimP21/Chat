from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    nick_name = models.CharField(max_length=40)
