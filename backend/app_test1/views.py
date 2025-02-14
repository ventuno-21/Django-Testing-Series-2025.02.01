from django.shortcuts import redirect, render
from django.views import View
from app_test1.models import Writer
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("app_test1:writers")
        return render(request, "app_test1/main.html")


class Home(View):
    def get(self, request):
        return render(request, "app_test1/home.html")


class About(View):
    def get(self, request, username):
        return render(request, "app_test1/about.html")


class WriterView(LoginRequiredMixin, View):
    def get(self, request):
        writers = Writer.objects.all()
        return render(request, "app_test1/writers.html", {"writers": writers})


def is_even(n):
    return n % 2 == 0
