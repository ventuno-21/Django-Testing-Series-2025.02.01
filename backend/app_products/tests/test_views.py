from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from app_products.models import Product
from django.urls import reverse
from django.db import IntegrityError


class TestAllProductsPage(TestCase):
    def setUp(self):
        Product.objects.create(name="p1", price=15, stock_count=10)
        Product.objects.create(name="p2", price=5, stock_count=15)
        Product.objects.create(name="p3", price=10, stock_count=3)

    def test_all_products_uses_correct_template(self):
        response = self.client.get(reverse("app_products:all"))
        self.assertTemplateUsed(response, "app_products/products.html")

    def test_all_products_context(self):
        response = self.client.get(reverse("app_products:all"))
        self.assertEqual(len(response.context["products"]), 3)
        self.assertContains(response, "p1")
        self.assertContains(response, "p2")
        self.assertNotContains(response, "No products available")

    def test_all_products_with_no_products(self):
        Product.objects.all().delete()
        response = self.client.get(reverse("app_products:all"))
        self.assertEqual(len(response.context["products"]), 0)
        self.assertContains(response, "No products available")


class TestProductsPage(SimpleTestCase):

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
