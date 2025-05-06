from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from app_products.models import Product
from django.urls import reverse
from django.db import IntegrityError


class TestProductsPage(SimpleTestCase):

    def setUp(self):
        response = self.client.get(reverse("app_products:products"))

    def test_products_status_code(self):
        response = self.client.get(reverse("app_products:products"))
        self.assertEqual(response.status_code, 200)

    def test_products_correct_template(self):
        response = self.client.get(reverse("app_products:products"))
        self.assertTemplateUsed(response, "app_products/index.html")

    def test_products_containts(self):
        """
        Because we mention status_code=200, we can remove first test in this class
        because of redundancy
        """
        response = self.client.get(reverse("app_products:products"))
        self.assertContains(response, "Whole products", status_code=200)
