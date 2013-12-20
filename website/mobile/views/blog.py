# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from module.blog.models import Post

def index(request):
    posts = Post.objects.filter(published=True)
    print posts
    print posts[0].get_absolute_url()
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
