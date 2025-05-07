from django.urls import path
from . import views

app_name = "app_test1"

urlpatterns = [
    path("", views.Home.as_view(), name="homey"),
    path("writers/", views.WriterView.as_view(), name="writers"),
    path("main/", views.Main.as_view(), name="main"),
    path("about/<str:username>/", views.About.as_view(), name="abouty"),
    path("post/", views.post_sth, name="post"),
]
