from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

from .views import AboutMeView, RegisterView, MyLogoutView

app_name = "accounts"

urlpatterns = [
    path("profile/", AboutMeView.as_view(), name="about-me"),
    path("registration/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True,
            next_page=reverse_lazy("accounts:about-me"),
        ),
        name="login",
    ),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]
