from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "stock_count")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Price can not be negative!")
        return price

    def clean_stock_count(self):
        stock_count = self.cleaned_data.get("stock_count")
        if stock_count < 0:
            raise forms.ValidationError("stock_count can not be negative!")
        return stock_count
