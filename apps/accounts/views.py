"""
Файл представлений для приложения Accounts
"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
)

from .forms import CustomUserCreationForm
from .models import Profile


class AboutMeView(TemplateView):
    """
    Представление для отображения информации о пользователе
    """

    template_name = "accounts/about-me.html"


class MyLogoutView(LogoutView):
    """
    Представление для обработки выхода пользователя из системы.
    """

    next_page = reverse_lazy("accounts:login")


class RegisterView(CreateView):
    """
    РПредставление для регистрации пользователя
    """

    form_class = CustomUserCreationForm
    template_name = "accounts/registration.html"
    success_url = reverse_lazy("accounts:about-me")

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        Profile.objects.create(user=self.object)
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response
