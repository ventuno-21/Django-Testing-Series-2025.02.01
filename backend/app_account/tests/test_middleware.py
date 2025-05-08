from django.test import TestCase, Client, override_settings
from django.urls import reverse
from app_account.models import User
from app_account.forms import UserRegistrationForm
from unittest.mock import patch


class MaintenaceModeTest(TestCase):

    @override_settings(MAINTENACE_MODE=False)
    def test_maintenace_mode_is_true(self):
        response = self.client.get(reverse("app_test1:homey"))

        self.assertContains(response, "This is a home page", status_code=200)

    @override_settings(MAINTENACE_MODE=True)
    def test_maintenace_mode_is_false(self):
        response = self.client.get(reverse("app_test1:homey"))

        self.assertContains(response, "Site is under maintenace", status_code=503)
