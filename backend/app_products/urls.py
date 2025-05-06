from .views import products
from django.urls import path


app_name = "app_products"

urlpatterns = [
    path("", products, name="products"),
]
