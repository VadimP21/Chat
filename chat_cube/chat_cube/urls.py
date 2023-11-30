"""
Основная точка входа в проект chat_cube, содержит стартовые urls
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", include("apps.chat.urls")),
    path("accounts/", include("apps.accounts.urls")),
]
