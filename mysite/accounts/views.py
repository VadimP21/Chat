from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
)

from .models import Profile


class AboutMeView(TemplateView):
    template_name = "accounts/about-me.html"


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/registration.html"
    success_url = reverse_lazy("accounts:about-me")

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response
