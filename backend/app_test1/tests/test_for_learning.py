from django.test import SimpleTestCase
from app_test1.views import is_even


class IsEvenTestCase(SimpleTestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(3))
