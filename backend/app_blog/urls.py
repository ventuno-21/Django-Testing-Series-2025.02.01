from django.urls import path
from . import views

app_name = "app_blog"

urlpatterns = [
    path("", views.blog, name="blog"),
    path("<int:id>/", views.single_post, name="single_post"),
]
