# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def add(request):
    a = request.GET["a"]
    b = request.GET["b"]
    print a,b
    result = int(a) + int(b)
    return HttpResponse(str(result))

def add2(request,a,b):
    print 2222
    result =int(a) + int(b)
    return HttpResponse(str(result))