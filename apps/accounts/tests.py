"""
Тесты для приложения Accounts
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("accounts:register")
        self.about_me_url = reverse("accounts:about-me")
        self.logout_url = reverse("accounts:logout")

        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )

    def tearDown(self) -> None:
        self.user.delete()

    def test_about_me_view(self):
        response = self.client.get(self.about_me_url)
        self.assertEquals(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
