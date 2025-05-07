from .views import products, all_products
from django.urls import path


app_name = "app_products"

urlpatterns = [
    path("", products, name="products"),
    path("all/", all_products, name="all"),
]
