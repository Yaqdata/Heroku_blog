# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from mobile.views import *

urlpatterns = patterns('mobile.views.hello',
    url(r'^hello/$','say_hello',name='mobile_say_hello'),
    url(r'^current/time/$', 'current_time', name='mobile_current_time'),
    url(r'^current/datetime/$', 'current_datetime'),
    url(r'^next/current/datetime/$', 'next_current_datetime'),
    url(r'^hours/(?P<hour>\d+)/$', 'hours_ahead'),
    #url(r'^time/plus/(\d{1,2})/$', hours_ahead),# 限定增加数值
)
