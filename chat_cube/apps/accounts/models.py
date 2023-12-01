from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = "auth_user"


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    nick_name = models.CharField(max_length=40)
