# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:48:48 2018

@author: shen1994
"""

from django.conf.urls import url
from . import views

app_name = 'deep_image'

urlpatterns = [        
    url(r'^image-retrieval/$', views.image_retrieval, name='image_retrieval'),
    url(r'^image-result/$', views.image_result, name='image_result'),
]