# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:08:23 2018

@author: shen1994
"""

from django import forms

from .models import MenuService
from .models import MenuApplication
from .models import MenuMessage

class MenuServiceForm(forms.ModelForm):
    class Meta:
        model = MenuService
        fields = ("title", "body")
        
class MenuApplicationForm(forms.ModelForm):
    class Meta:
        model = MenuApplication
        fields = ("title", "body")
        
class MenuMessageForm(forms.ModelForm):
    class Meta:
        model = MenuMessage
        fields = ("title", "body")
        