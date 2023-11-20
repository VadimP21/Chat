#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys
from multiprocessing import Process


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def redis_start():
    subprocess.call(
        ["docker", "run", "-p", "6379:6379", "--name", "chat-redis", "redis:7"],
        stdout=subprocess.PIPE,
        text=True,
    )
    subprocess.call(
        [
            "docker",
            "start",
            "chat-redis",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )


if __name__ == "__main__":
    main()
