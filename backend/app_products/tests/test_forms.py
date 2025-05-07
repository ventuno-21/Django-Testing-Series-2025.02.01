from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from app_products.models import Product
from django.urls import reverse
from django.db import IntegrityError


class ProductFormTest(TestCase):

    def test_create_product_when_submitting_valid_form(self):
        form_data = {"name": "p1", "price": 12, "stock_count": 10}
        response = self.client.post(reverse("app_products:all"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name="p1").exists())
        # self.assertContains(response, "p1")

    def test_dont_create_product_when_submitting_valid_form(self):
        form_data = {"name": "", "price": -12, "stock_count": -10}
        response = self.client.post(reverse("app_products:all"), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)

        form = response.context["form"]
        self.assertFormError(form, "name", "This field is required.")
        self.assertFormError(form, "price", "Price can not be negative!")
        self.assertFormError(form, "stock_count", "stock_count can not be negative!")

        self.assertFalse(Product.objects.exists())
