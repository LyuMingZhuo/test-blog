from django.shortcuts import render
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts': posts})