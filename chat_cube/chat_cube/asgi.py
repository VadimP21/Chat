"""
Конфигурация ASGI для проекта chat_cube.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_cube.settings")

application = get_asgi_application()
