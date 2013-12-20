# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from mobile.views import *

urlpatterns = patterns('mobile.views.blog',
    url(r'^$', 'index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'post'),
)
