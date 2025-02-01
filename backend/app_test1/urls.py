from django.urls import path
from . import views

app_name = "app_test1"
urlpatterns = [
    path("", views.Home.as_view(), name="homey"),
    path("about/<str:username>/", views.About.as_view(), name="abouty"),
]
