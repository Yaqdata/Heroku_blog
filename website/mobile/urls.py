# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from mobile.views.blog import IndexView, PostDetailView, CategoryView

urlpatterns = patterns('mobile.views.blog',
    url(r'^$', IndexView.as_view(), name="home"),
    #url(r'^(?P<slug>[\w\-]+)/$', 'post'),
    url(r'^category/(?P<alias>\w+)/$', CategoryView.as_view()),
    url(r'^post/(?P<slug>\w+)/$', PostDetailView.as_view()),
)
