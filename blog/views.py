from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):

    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "blog/index.html", context)


def post(request, id):
    post = Post.objects.get(pk=id)

    context = {
        "post":post
    }
    return render(request, "blog/post.html", context)