from django.db import models
from app_account.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(default=0)

    def get_discounted_price(self, discounted_percentage):
        return self.price * (1 - discounted_percentage / 100)

    @property
    def in_stock(self):
        return self.stock_count > 0

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price can not be negative!")
        if self.price < 0:
            raise ValidationError("Stock quantity can not be negative!")
