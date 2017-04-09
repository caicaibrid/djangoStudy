# coding:utf-8

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from modelStudy.models import People


def login(request):
    obj = People.objects.all()
    return render(request,"login.html",{"result":obj})

def addUser(request):
    name = request.GET.get("name", None)
    age = request.GET.get("age", None)
    if name and age:
        obj = People.objects.all()
        for obj in obj:
            if obj.name == name:
                request.session["error"] = str(name)+"已存在";
                return HttpResponseRedirect("/login/")
        People.objects.create(name=name, age=age)
    return HttpResponseRedirect("/login/")