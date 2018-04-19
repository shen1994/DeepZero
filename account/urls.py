# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/login-error$', views.login_error, name='login_error'),
    url(r'^service-post/$', views.service_post, name='service_post'),
    url(r'^application-post/$', views.application_post, name='application_post'),
    url(r'^message-post/$', views.message_post, name='message_post'),
]