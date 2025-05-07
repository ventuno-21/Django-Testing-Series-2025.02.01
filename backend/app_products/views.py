from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.urls import reverse


# Create your views here.
def products(request):
    return render(request, "app_products/index.html")


def all_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("app_products:all"))
        else:
            context = {"products": Product.objects.all(), "form": form}
            return render(request, "app_products/products.html", context)

    context = {"products": Product.objects.all(), "form": ProductForm()}
    return render(request, "app_products/products.html", context)
