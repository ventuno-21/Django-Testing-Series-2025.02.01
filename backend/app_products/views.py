from django.shortcuts import render
from .models import Product


# Create your views here.
def products(request):
    return render(request, "app_products/index.html")


def all_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "app_products/products.html", context)
