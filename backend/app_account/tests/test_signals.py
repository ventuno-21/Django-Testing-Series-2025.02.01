from django.test import TestCase, Client
from django.urls import reverse
from app_account.models import User
from app_account.forms import UserRegistrationForm
from unittest.mock import patch


class UserSignalsTest(TestCase):

    @patch("app_account.signals.send_mail")
    def test_welcome_email_sent_on_user_creation(self, mock_send_mail):
        User.objects.create_user(
            username="user10", password="user10", email="user@user.com"
        )
        # Check send_mail function is called once the user is created
        mock_send_mail.assert_called_once_with(
            "Welcome!",
            "Thanks for signing up",
            "admin@gmail.com",
            ["user@user.com"],
            fail_silently=False,
        )

    @patch("app_account.signals.send_mail")
    def test_no_email_sent_when_user_updated(self, mock_send_mail):
        user = User.objects.create_user(
            username="user10", password="user10", email="user@user.com"
        )
        # reset the mock call to zero
        # The reset_mock method resets all the call attributes on a mock object
        mock_send_mail.reset_mock()

        # Update user email, in this case because we updateded the user, an email will not be sent to user
        user.email = "user1@user1.com"
        user.save()

        mock_send_mail.assert_not_called()
