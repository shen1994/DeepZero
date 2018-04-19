# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:48:39 2018

@author: shen1994
"""

from django import forms

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "url", "description", "image")
        