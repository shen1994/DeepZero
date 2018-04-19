# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:00:49 2018

@author: shen1994
"""

from django.conf.urls import url
from . import views

app_name = 'deep_text'

urlpatterns = [        
    url(r'^text-chat/$', views.text_chat, name='text_chat'),
]