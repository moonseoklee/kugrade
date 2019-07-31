from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .templates import grade
from .service import test
from django.template import Context
from django.utils.safestring import mark_safe
import json
def index(request):
    return render(request,"./templates/grade/login.html")

def chart(request):
    return render(request,'./templates/grade/chart.html')
def login(request):
    if request.method == "POST":        
        username = request.POST.get('username','')
        password = request.POST.get('password','') 
           
        a,b = test.login(username,password)
        c = {}
        
        c['info'] = mark_safe((a))
        c['score'] = mark_safe((b))
        
        
        return TemplateResponse(request,'./templates/grade/chart.html',c)
    return render(request,'./templates/grade/login.html')
