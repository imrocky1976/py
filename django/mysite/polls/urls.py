from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^time/$', views.current_datetime, name='time'),
    re_path(r'^time/plus/(?P<offset>\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
    #extra_context={'next': '/polls/time'}
    re_path(r'^accounts/login/$', LoginView.as_view()),
    re_path(r'^accounts/logout/$', LogoutView.as_view())
]