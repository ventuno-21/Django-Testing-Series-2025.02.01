from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.


def blog(request):
    context = {"posts": Post.objects.all()}
    return render(request, "app_blog/blog.html", context)


def single_post(request, id):
    context = {"post": get_object_or_404(Post, id=id)}
    return render(request, "app_blog/single_post.html", context)
