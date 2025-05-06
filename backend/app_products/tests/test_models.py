from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from app_products.models import Product
from django.db import IntegrityError


class ProductModelTestv2(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        instead of setUp() method we can use setUpTestData()
        setUp => will run once for each method of class
        setUpTestData => will run once for whole class
        """
        cls.product = Product(name="p1", price=100, stock_count=10)

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

    def test_negative_price_constraint(self):
        product = Product(name="negative product price", price=-10, stock_count=3)

        with self.assertRaises(IntegrityError):
            product.save()

    def test_negative_stock_count_constraint(self):
        product = Product(name="negative stock qty", price=10, stock_count=-3)

        with self.assertRaises(IntegrityError):
            product.save()


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

    def test_negative_price_constraint(self):
        product = Product(name="negative product price", price=-10, stock_count=3)

        with self.assertRaises(IntegrityError):
            product.save()

    def test_negative_stock_count_constraint(self):
        product = Product(name="negative stock qty", price=10, stock_count=-3)

        with self.assertRaises(IntegrityError):
            product.save()
