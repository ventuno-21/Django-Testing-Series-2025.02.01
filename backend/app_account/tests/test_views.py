from django.test import TestCase, Client
from django.urls import reverse
from app_account.models import User
from app_account.forms import UserRegistrationForm


class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse("app_account:user_register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_account/register.html")
        # self.failUnless(response.context["form"], UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(
            reverse("app_account:user_register"),
            data={
                "username": "ventuno",
                "email": "ventuno@ventuno.com",
                "password1": "ventuno21",
                "password2": "ventuno21",
            },
        )
        # status_code:302 is for redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("app_test1:homey"))
        # 1 user is added therefore in User model ONE user should be exist
        self.assertEqual(User.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        response = self.client.post(
            reverse("app_account:user_register"),
            data={
                "username": "user2",
                "email": "invalid email",
                "password1": "ventuno21",
                "password2": "ventuno21",
            },
        )
        self.assertEqual(response.status_code, 200)
        # Seems like failIf doesnt work anymore
        # self.failIf(response.context["form"].is_valid())
        """
        The error inside errors is exacty 
        what django send us if the emil address be invalid
        """
        self.assertFormError(
            form=response.context["form"],
            field="email",
            errors=["Enter a valid email address."],
        )
