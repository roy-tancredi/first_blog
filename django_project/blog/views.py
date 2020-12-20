from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        "author": "Gosiak",
        "title": "First post",
        "content": "Some great content",
        "date_posted": "December 19, 2020"
    },
    {
        "author": "Roy Tancredi",
        "title": "Second post",
        "content": "Some great content",
        "date_posted": "December 20, 2020"
    }

]


def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "about"})


def base(request):
    return render(request, "blog/base.html")
