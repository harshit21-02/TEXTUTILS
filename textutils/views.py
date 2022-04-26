#I have created this
from pickle import GET
import re
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default') 
    removpunctext=request.GET.get('removpunc','off') 
    print(removpunctext)
    analyzed=""
    punctuations='''!@#$%^&*,./()<>?{}|\[]:";'-'''
    for char in djtext:
        if char not in punctuations:
            analyzed+=char 
        
    params = {'purpose':'Removed Punctuations','AnalyzedText':analyzed} 
    return render(request,'analyze.html', params)


