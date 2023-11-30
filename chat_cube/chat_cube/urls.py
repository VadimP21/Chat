"""
Основная точка входа в проект chat_cube, содержит стартовые urls
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
