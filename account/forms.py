# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:32:50 2018

@author: shen1994
"""

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    