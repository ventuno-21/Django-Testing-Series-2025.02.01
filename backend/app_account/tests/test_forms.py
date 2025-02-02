from django.test import TestCase
from app_account.forms import UserRegistrationForm
from app_account.models import User


class TestRegistrationFOrm(TestCase):
    # setUpTestData will run before each class once
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="user1", email="user1@user1.com", password="user1"
        )

    def test_valid_data(self):
        form = UserRegistrationForm(
            data={
                "username": "ventuno",
                "email": "ventuno@ventuno.com",
                "password1": "ventuno21",
                "password2": "ventuno21",
            }
        )
        self.assertTrue(form.is_valid())

    def test_exist_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_exist_email(self):
        form = UserRegistrationForm(
            data={
                "username": "ventuno",
                "email": "user1@user1.com",
                "password1": "ventuno21",
                "password2": "ventuno21",
            }
        )
        # clean_email will raise a validationError because the email was registered before
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error("email"))

    def test_unmatched_passwords(self):
        form = UserRegistrationForm(
            data={
                "username": "ventuno",
                "email": "ventuno@ventuno.com",
                "password1": "ventuno21",
                "password2": "ventuno24",
            }
        )
        self.assertEqual(len(form.errors), 1)
        # for has_error we dont mention the fields, because in forms we didnt add any field for cleaning our passwords
        self.assertTrue(form.has_error)
