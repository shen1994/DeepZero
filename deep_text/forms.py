# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:01:00 2018

@author: shen1994
"""

from django import forms

from .models import TextChat

class TextChatForm(forms.ModelForm):
    class Meta:
        model = TextChat
        fields = ("question",)