from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_test1.views import Home, About


class TestFirst(SimpleTestCase):
    def test_fail(self):
        self.assertFalse(1 == 5)

    def test_success(self):
        self.assertTrue(1 == 1)


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse("app_test1:homey")  # result url => /
        # print("reverse home page = ", url)
        resolver = resolve(url)
        # print("url resolve home page ==", resolver)
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_about(self):
        url = reverse("app_test1:abouty", args=("ventuno",))
        # print("reverse about page = ", url)
        resolver = resolve(url)
        self.assertEqual(resolve(url).func.view_class, About)
