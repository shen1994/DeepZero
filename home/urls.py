# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:53:47 2018

@author: shen1994
"""

from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^menu/$', views.menu_process, name='menu_process'),
    url(r'menu/service_title/$', views.menu_service_title, name='menu_service_title'),
    url(r'menu/service_title/(?P<service_id>\d+)/$', views.service_title_detail, name='service_title_detail'),
    url(r'menu/application_title/$', views.menu_application_title, name='menu_application_title'),
    url(r'menu/application_title/(?P<application_id>\d+)/$', views.application_title_detail, name='application_title_detail'),
    url(r'menu/message_title/$', views.menu_message_title, name='menu_message_title'),
    url(r'menu/message_title/(?P<message_id>\d+)/$', views.message_title_detail, name='message_title_detail'),
    url(r'menu/service/(?P<service_id>\d+)/$', views.menu_service_content, name='menu_service_content'),
    url(r'menu/application/(?P<application_id>\d+)/$', views.menu_application_content, name='menu_application_content'),
    url(r'menu/message/(?P<message_id>\d+)/$', views.menu_message_content, name='menu_message_content'),
]