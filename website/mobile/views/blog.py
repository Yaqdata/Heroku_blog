# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from module.blog.models import Post

def base(request):
    top_clicks = 'xxx'

def index(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    print slug
    post = get_object_or_404(Post, slug=slug)
    print post.pk
    return render(request, 'blog/post.html', {'post': post})
