from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from app_account.models import User
from app_test1.views import Main
from unittest.mock import patch
import requests

"""
Difference between RequestFactory() & Client():
 RequestFactory returns a request, while Client returns a response
"""


class PostViewTest(TestCase):

    @patch("app_test1.views.requests.get")
    def test_post_view_success(self, mock_get):
        mock_get.return_value.status_code = 200
        return_data = {"userId": 1, "id": 1, "title": "Test title", "body": "Test body"}
        # return_data = {
        #     "userId": 1,
        #     "id": 1,
        #     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        #     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
        # }
        mock_get.return_value.json.return_value = return_data

        # send a request to view
        response = self.client.get(reverse("app_test1:post"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, return_data)

        # Ensure that the mock API call was made once with the correct URL
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts/1")

    @patch("app_test1.views.requests.get")
    def test_post_sth_view_fail(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        response = self.client.get(reverse("app_test1:post"))
        self.assertEqual(response.status_code, 503)
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts/1")


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
