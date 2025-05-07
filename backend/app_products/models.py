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

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(price__gt=0), name="price_gt_0"),
            models.CheckConstraint(
                condition=models.Q(stock_count__gt=0), name="stock_gt_0"
            ),
        ]

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(price__gt=0), name="price_gt_0"),
            models.CheckConstraint(
                condition=models.Q(stock_count__gt=0), name="stock_gt_0"
            ),
        ]

    @property
    def in_stock(self):
        return self.stock_count > 0

    # def clean(self):
    #     """
    #     clean method will not be run if we save() an instance with negative price or stock_count
    #     therefore we should mention "constraints" in Meta class

    #     If we hange the type of stock_count to PostivieIntegreField,
    #     It will not be necessarly to write a contraints for it
    #     """
    #     if self.price < 0:
    #         raise ValidationError("Price can not be negative!")
    #     if self.stock_count < 0:
    #         raise ValidationError("Stock quantity can not be negative!")
