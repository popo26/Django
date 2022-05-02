from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # = from blog.models import Post

# Create your views here.

def index(request):
    # return HttpResponse("<h1>Hello Django</h1>")
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context=context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, "blog/detail.html", context)

