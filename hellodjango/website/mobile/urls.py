# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from mobile.views import *

urlpatterns = patterns('mobile.views.hello',
    url(r'^hello/$','say_hello',name='mobile_say_hello'),
)
