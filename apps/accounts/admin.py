"""
Админка для приложения Accounts
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password1", "password2"],
            },
        )
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "nick_name",
    )
    ordering = (
        "pk",
        "nick_name",
    )
    search_fields = ("nick_name",)

    def get_queryset(self, request):
        return Profile.objects.select_related("user")
