from django.test import TestCase, Client
from django.urls import reverse
from app_account.models import User


class TestWriterView(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username="admin",
            email="admin@admin.com",
            password="admin",
        )
        self.client.login(username="admin", email="admin@admin.com", password="admin")

    def test_writers(self):
        """
        Because class writes inside views.py is used LOGINREQUIREDMIXIN
        therefore client should be login to access this page,
        In setUp method, we logged in a User
        """
        response = self.client.get(reverse("app_test1:writers"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_test1/writers.html")
