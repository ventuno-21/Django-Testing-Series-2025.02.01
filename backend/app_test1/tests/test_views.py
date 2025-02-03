from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from app_account.models import User
from app_test1.views import Main

"""Difference between RequestFactory() & Client():
 RequestFactory returns a request, while Client returns a response
"""


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
        # print("response==", response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_test1/writers.html")


class TestMainView(TestCase):
    def setUp(self):
        """
        We can access to 'request'instance with RequestFactory()
        It does not support middleware , so we dont access to:
        session, authentication attributes
        """
        self.user = User.objects.create_user(
            username="admin",
            email="admin@admin.com",
            password="admin",
        )
        self.factory = RequestFactory()

    # If our user is_authenticated we use below method for testing
    def test_main_user_authenticated(self):
        request = self.factory.get(reverse("app_test1:main"))
        # Now we have to add our user to the above request
        request.user = self.user
        # print("request.user =====", request.user)
        # Now we send our request to our View, because it is CBV we  have to use as_view()
        response = Main.as_view()(request)
        self.assertEqual(response.status_code, 302)

    # And id our user is Anonymous we use below method for testing
    def test_main_user_anonymous(self):
        request = self.factory.get(reverse("app_test1:main"))
        request.user = AnonymousUser()
        response = Main.as_view()(request)
        self.assertEqual(response.status_code, 200)
