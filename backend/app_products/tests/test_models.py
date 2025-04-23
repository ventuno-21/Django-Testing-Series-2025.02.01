from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from app_products.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name="p1", price=100, stock_count=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        self.product.stock_count = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discount_price(self):
        self.assertEqual(self.product.get_discounted_price(10), 90)
        self.assertEqual(self.product.get_discounted_price(0), 100)

    def test_negative_price_validation(self):
        self.product.price = -5
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_count_validation(self):
        self.product.stock_count = -5
        with self.assertRaises(ValidationError):
            self.product.clean()
