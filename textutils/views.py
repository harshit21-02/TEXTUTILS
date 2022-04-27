#I have created this

import enum
from pickle import GET
import re
from tkinter import ON
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default') 
    removpunctext=request.GET.get('removpunc','off') 
    capitaltext=request.GET.get('capitalize','off') 
    extratext=request.GET.get('extraspaces','off') 
    analyzed=""
    ctext=""
    final="" 
    if removpunctext == 'on':
        punctuations='''!@#$%^&*,./()<>?{}|\[]:";'-'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char 
    else:
        analyzed=analyzed+djtext  

    
    if capitaltext == 'on':
        for char in analyzed:
            ctext=ctext+char.upper()
    else:
        ctext=ctext+analyzed

    if extratext == 'on':
        for index,char in enumerate(ctext):
            if ctext[index]==" " and ctext[index+1]==" ":
                pass 
            else:
                final=final+char
    else:   
        for index,char in enumerate(ctext):
            if ctext[index]==" " and ctext[index+1]==" ":
                final=final+char
    params = {'purpose':'Your Analyzed Text: ','AnalyzedText':ctext} 
    return render(request,'analyze.html', params)


