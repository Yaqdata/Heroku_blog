# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
import datetime

def say_hello(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    author = {
        'name': 'Yaq',
        'age': 24,
        'sex': 'male',
    }
    return render_to_response('current_datetime.html', {'current_date': now, 'msg': 121212,'author': author})

def next_current_datetime(request):
    now = datetime.datetime.now()
    print settings.MEDIA_URL
    return render_to_response('time/current_datetime.html', {'current_date': now})

def hours_ahead(request, hour):
    hour_offset = 111
    hour = int(hour)
    next_time = hour_offset + hour
    return render_to_response('time/hours_ahead.html', locals())

def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>now is %s.</body></html>' %now
    return HttpResponse(html)


