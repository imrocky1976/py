from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import datetime, timedelta

# Create your views here.

def index(request):
    resp = {"msg": "Hello, world. You're at the polls index."}
    for k, v in request.META.items():
        if isinstance(v, str):
            resp[k] = v
    return JsonResponse(resp, json_dumps_params={"sort_keys": True})

@login_required
def current_datetime(request):
    now = datetime.now()
    messages.warning(request, "Your playlist was added successfully.")
    #html = "<html><body>current datetime: {}</body></html>".format(now)
    #return HttpResponse(html)

    #t = get_template('current_datetime.html')
    #html = t.render({'author': 'shihj', 'now': now})
    #return HttpResponse(html)

    # 直接用Template 需要自己提供html文本
    #t = Template('<html>...</html>')
    #html = t.render(Context({'author': 'shihj', 'now': now}))
    #return HttpResponse(html)

    return render(request, 'current_datetime.html', {'author': 'shihj', 'now': now})

@login_required
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.now()
    ahead = now + timedelta(hours=offset)

    #html = "<html><body>In {} hours, it will be {}</body></html>".format(offset, ahead)
    #return HttpResponse(html)

    #return render_to_response(
    #    'time_ahead.html', 
    #    {'author': 'shihj', 'hour_offset': offset, 'next_time': ahead}
    #)
    return render(request, 'time_ahead.html', {'author': 'shihj', 'hour_offset': offset, 'next_time': ahead})