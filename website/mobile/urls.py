# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from mobile.views.blog import IndexView

urlpatterns = patterns('mobile.views.blog',
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^(?P<slug>[\w\-]+)/$', 'post'),
)
